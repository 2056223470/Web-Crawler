# 目标网站url：https://so.yilianmeiti.com/t_8?keyword=%E6%84%9F%E5%86%92&page=1
# 纯协议，无参考价值
import csv
import logging

import requests
from lxml import etree

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

url = r"https://so.yilianmeiti.com/t_8?keyword={}&page={}"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://so.yilianmeiti.com",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}

cookies = {
    "Hm_lvt_0374efeb26a387fcb8fd7c5f8c78eac8": "1744453247",
    "Hm_lpvt_0374efeb26a387fcb8fd7c5f8c78eac8": "1744453388"
}

base_url = url.format("感冒", "1")

response = requests.get(base_url, headers=headers, cookies=cookies)
response.raise_for_status()

med_info_list = []

tree = etree.HTML(response.text)

Med_List = tree.xpath('/html/body/div[1]/div[3]/div[1]/ul/li')
for med in Med_List:
    med_info = {}
    med_info['name'] = med.xpath('/html/body/div[1]/div[3]/div[1]/ul/li[1]/h2/a/text()')[0]
    med_info['status'] = med.xpath('/html/body/div[1]/div[3]/div[1]/ul/li[1]/dl/dd/p[1]/text()')[0].split('：')[1]
    med_info['detail'] = med.xpath('/html/body/div[1]/div[3]/div[1]/ul/li[1]/dl/dd/p[2]/text()')[0]
    med_info_list.append(med_info)

head = {"name", "status", "detail"}
with open('../素材/药品/info.csv', 'w',encoding="utf-8-sig", newline='') as f:
    ws = csv.DictWriter(f, fieldnames=head)
    ws.writeheader()
    ws.writerows(med_info_list)
    logging.info(f"{len(med_info_list)}条写入完成")
