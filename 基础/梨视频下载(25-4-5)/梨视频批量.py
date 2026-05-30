# 第一版觉得爬太少，找到了https://www.pearvideo.com/category_loading.jsp接口，可以直接提取并且循环翻页
# 第二版觉得爬太慢，计划用异步先下载，咱未实施


import os
import re

from requests_html import HTMLSession
from lxml import etree
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ID_URL = 'https://www.pearvideo.com/category_loading.jsp'
BASE_URL = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd={}'
VID_URL = 'https://video.pearvideo.com/mp4/short/20250327/cont-1799106-16048118-hd.mp4'


# 先从主页的视频节点中，取href元素，获得对应的视频id
class L_VideoSpider:
    def __init__(self):
        self.session = HTMLSession()

    # 提取id表
    def id_extract(self, res):
        # 修改：将响应内容转换为字符串
        tree = etree.HTML(res.text)
        video_list = tree.xpath('//li[@class="categoryem"]//a[@class="vervideo-lilink actplay"]/@href')
        id_list = []
        for video in video_list:
            video_id = video.split('_')[1]
            id_list.append(video_id)
        return id_list

    def url_id(self, pages):
        for page in range(pages):
            params = {
                "reqType": "5",
                "categoryId": "1",
                "start": str((page-1)*24),
                "mrd": "0.23396210730730027",
            }
            headers = {
                "Accept": "text/html, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Referer": "https://www.pearvideo.com/category_1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
                "X-Requested-With": "XMLHttpRequest",

            }
            try:
                res = self.session.get(ID_URL, params=params, headers=headers)
                res.raise_for_status()
                return self.id_extract(res)
            except Exception as e:
                logging.error(f"获取首页出现错误{e}")
                # 修改：在出现异常时返回空列表而不是 None
                return []

    # 将视频id拼接到base_url上，mrd = Math.random()
    def get_video_info(self, id_list):
        global headers
        for video_id in id_list:
            video_url = BASE_URL.format(video_id, random.random())
            logging.info(f"发送请求至：{video_url}")
            headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Referer": f"https://www.pearvideo.com/video_{video_id}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
                "X-Requested-With": "XMLHttpRequest",

            }
            try:
                res = self.session.get(video_url, headers=headers)
                res.raise_for_status()
                # 这里不用return
                self.video_info_extract(res)
            except Exception as e:
                logging.error(f"出错了{e}")

    # base_url返回的json包则可以直接生成最后的vid_url
    def video_info_extract(self, res):
        video_image = res.json()['videoInfo']['video_image']
        srcUrl = res.json()['videoInfo']['videos']['srcUrl']
        logging.info(f"取得{video_image}和{srcUrl}")
        # 提取cont-1799041
        cont_match = re.search(r'cont-(\d+)', video_image)
        if cont_match:
            full_cont_id = cont_match.group(0)  # 得到"cont-1799041"
            # 修改正则表达式，精确匹配日期后的数字
            new_video_url = re.sub(r'/(\d+)(?=-)', f'/{full_cont_id}', srcUrl)
            logging.info(f"最终的url为：{new_video_url}")
            return self.download_video(new_video_url, '../素材/梨视频')
        else:
            logging.error("未找到对应的cont—id")

    def download_video(self, video_url, save_base_path):
        # 创建保存路径
        if not os.path.exists(save_base_path):
            os.makedirs(save_base_path)

        logging.info(f"正在下载视频文件: {video_url}")
        save_path = save_base_path + '/video_' + video_url.split('/')[-1].split('-')[1] + '.mp4'
        try:
            # 发送HTTP请求
            video_response = self.session.get(video_url, stream=True)
            video_response.raise_for_status()

            # 获取文件大小
            file_size = int(video_response.headers.get('Content-Length', 0))
            chunk_size = 8192 if file_size < 10 * 1024 * 1024 else 16384

            # 保存视频文件到本地
            with open(save_path, 'wb') as file:
                for chunk in video_response.iter_content(chunk_size=chunk_size):
                    file.write(chunk)

            logging.info(f"视频文件已保存到: {os.path.abspath(save_path)}")
        except Exception as e:
            logging.error(f"下载失败: {e}")

    def main(self):
        # url_id会调用id_extract，最终返回id_list传入get_video_info,
        # 后者又会调用video_info_extract，返回最终正确的视频下载路径
        # 下载路径继续传入下载函数，保存到本地
        self.get_video_info(self.url_id(pages=5)) # 想爬多少页就写多少，一页是24个视频

if __name__ == '__main__':
    spider = L_VideoSpider()
    spider.main()
