# 初始url：https://www.99meiju.com/play/17686-1-0.html
# 然后从html中获取index.m3u8的链接,index的.m3u8中是mix.m3u8的url
# 获取并记录记录mix.m3u8的内容然后下载ts,mix.m3u8的内容是被分成.ts的视频url
# 在获取mix.m3u8的url的时候，出现了看不见的换行符的问题
# 在遇到非规范的返回格式的时候，最好检查字段拼接，是否存在空格或者换行符，可以使用.strip()去除首尾空字符，包括换行和空格
# 感觉出于网络原因，爬取的速度比较慢，计划使用协程挂载提升下载速度
# 添加协程的时候记得添加限制，强碱网站会使请求直接失败，还好没有直接被封ip
# 下载了298个片段，但是总长只有9分半左右

import os
from requests_html import HTMLSession
from lxml import etree
import logging
import asyncio
import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


BASE_URL = 'https://www.99meiju.com/play/17686-0-0.html'
class USA_movie_spider:
    def __init__(self):
        self.session = HTMLSession()

    def get_index_url(self, movie_info):
        """获取index.m3u8的url"""
        tree = etree.HTML(movie_info.text)
        now_url = tree.xpath('//*[@id="playblock"]/script[1]/text()')[0].split('"')[1]
        next_url = tree.xpath('//*[@id="playblock"]/script[1]/text()')[0].rsplit(';')[2].split('"')[1]
        return now_url, next_url

    def get_res(self, url):
        """发送请求的通用方法"""
        try:
            res_info = self.session.get(url)
            res_info.raise_for_status()  # 检查请求是否成功
            logging.info('请求正常')
            return res_info
        except Exception as e:
            logging.error(f"请求出现了问题: {e}")
        return None

    def get_index_m3u8(self, res_info):
        """截取index.m3u8文件最后的mix.m3u8的文件url片段"""
        # 假设 res_info 是 requests 响应对象，text 是属性而不是方法
        index_url = '/'.join(res_info.text.split('/')[-3:])
        return index_url

    def get_mix_ts(self, res):
        """分割mix.m3u8中的url并提取"""
        # 原代码中 split('#')[6:-9] 返回的是列表，列表没有 split 方法
        # 这里先将响应文本按 # 分割，然后处理每一段
        lines = res.text.split('#')[6:-9]
        mix_url_list = []
        for line in lines:
            parts = line.split(',')
            if len(parts) > 1:
                mix_url_list.append(parts[1])
        return mix_url_list

    async def download_ts_file_async(self, semaphore, session, url, base_path, index):
        """异步下载 .ts 文件"""
        async with semaphore:  # 使用信号量限制并发
            save_path = os.path.join(base_path, str(index) + '.ts')
            headers = {
                'accept': '*/*',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'no-cache',
                'origin': 'https://www.ikdmjx.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://www.ikdmjx.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
            } # 并没有验证这个头是不是必需的，防止挂掉加上的
            try:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    with open(save_path, 'wb') as f:
                        while True:
                            chunk = await response.content.read(8192)
                            if not chunk:
                                break
                            f.write(chunk)
                logging.info(f"第{index}段下载成功: {save_path}")
            except Exception as e:
                logging.error(f"第{index}段下载失败: {url}，错误: {e}") # 下载失败及时返回对应的url检查问题

    async def main(self):
        res1 = self.get_res(BASE_URL)
        if res1 is None:
            logging.error("无法获取 BASE_URL 的响应，程序终止")
            return
# ==================================================================================
        now_url, next_url = self.get_index_url(res1)
        res2 = self.get_res(now_url)
        if res2 is None:
            logging.error("无法获取 now_url 的响应，程序终止")
            return
# ==================================================================================
        index_url = self.get_index_m3u8(res2)
        # 拼接最后的mix.m3u8的url，也就是最后的.ts的表
        mix_url = now_url.replace("index.m3u8", index_url).strip() # 在这里出现了看不见的换行符，用.strip()解决
        try:
            res3 = self.get_res(mix_url)
            res3.raise_for_status()  # 检查请求是否成功
            # 手动设置编码
            res3.encoding = 'utf-8'
            if not res3.text:
                logging.warning("响应内容为空，可能需要检查请求头或代理设置")
        except Exception as e:
            logging.error(f"请求出现了问题: {e}")
            return
# =================================================================================
        mix_url_list = self.get_mix_ts(res3)
        print(mix_url_list)

        semaphore = asyncio.Semaphore(10)  # 创建一个信号量，最多允许10个协程同时运行
        async with aiohttp.ClientSession() as session:
            tasks = []
            for index, url in enumerate(mix_url_list):
                task = self.download_ts_file_async(semaphore, session, url.strip(), "../素材/美剧/", index)
                tasks.append(task)
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    spider = USA_movie_spider()
    asyncio.run(spider.main())
