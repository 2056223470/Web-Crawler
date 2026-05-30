import csv

from requests_html import HTMLSession
from lxml import etree
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = 'https://www.ypppt.com'
First_URL = BASE_URL + '/moban'


class ppt_spider:
    def __init__(self):
        self.session = HTMLSession()

    def get_info_url(self, page):
        tree = etree.HTML(page.text)
        all_info_url = tree.xpath('/html/body/div[2]/ul/li/a[2]')
        if all_info_url:
            return [BASE_URL + info_url.xpath('./@href')[0] for info_url in all_info_url]
        else:
            return None

    def get_first_page(self):
        try:
            page = self.session.get(First_URL)
            page.raise_for_status()
            logging.info("第一步成功获取")
            return self.get_info_url(page)
        except Exception as e:
            logging.error(f"第一步出错了：{e}")
            return []

    def get_download_url(self, res):
        tree = etree.HTML(res.text)
        logging.info("第二步正确解析页面")
        download_url = tree.xpath('/html/body/div[2]/div[2]/div/div[1]/div[2]/a')[0]
        return BASE_URL + download_url.xpath('./@href')[0]

    def get_mid_page(self, all_url):
        all_download_url = []
        for download_url in all_url:
            try:
                res = self.session.get(download_url)
                res.raise_for_status()
                all_download_url.append(self.get_download_url(res))
                logging.info("第二步成功获取")
            except Exception as e:
                logging.error(f"第二步出错了{e}")
        if all_download_url:
            return all_download_url

    def ppt_info(self, res):
        ppt_info = {}
        logging.info("开始提取")
        tree = etree.HTML(res.text)
        # 获取ppt的标题，比例，页数，效果，地址
        ppt_info['标题'] = tree.xpath('/html/body/div/div/div[2]/div[2]/h1/text()')[0].split('-')[0]
        ppt_info['比例'] = tree.xpath('/html/body/div/div/div[2]/div[2]/ul/li[3]/text()')[0]
        ppt_info['页数'] = tree.xpath('/html/body/div/div/div[2]/div[2]/ul/li[4]/text()')[0]
        ppt_info['效果'] = tree.xpath('/html/body/div/div/div[2]/div[2]/ul/li[8]/text()')[0]
        ppt_info['下载地址'] = tree.xpath('/html/body/div/div/ul/li[1]/a/@href')[0]
        return ppt_info

    def get_end_page(self, all_url):
        all_ppt = []
        for end_url in all_url:
            try:
                res = self.session.get(end_url)
                res.raise_for_status()
                logging.info("第三步成功获取")
                all_ppt.append(self.ppt_info(res))
            except Exception as e:
                logging.error(f"第三步出错了{e}")
        if all_ppt:
            return all_ppt

    def main(self):
        # 保存的格式是[{}]
        all_ppt_info = self.get_end_page(self.get_mid_page(self.get_first_page()))
        head = ("标题", "比例", "页数", "效果", "下载地址")
        with open("../素材/优品ppt/ppt的信息表.csv", "w", encoding="utf-8-sig", newline='') as f:
            ws = csv.DictWriter(f, fieldnames=head)
            ws.writeheader()
            ws.writerows(all_ppt_info)
            logging.info(f"{len(all_ppt_info)}条写入完成")

if __name__ == '__main__':
    ppt_spider = ppt_spider()
    ppt_spider.main()