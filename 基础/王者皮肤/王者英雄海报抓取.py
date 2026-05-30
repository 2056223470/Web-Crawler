from requests_html import HTMLSession

import os

import concurrent.futures


class Wangzhe_Spider:

    # 创建文件夹
    os_path = os.getcwd()+"/王者皮肤/"
    if not os.path.exists(os_path):
        os.makedirs(os_path)
    def __init__(self):
        # 英雄图片的url = https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/177/177-bigskin-3.jpg
        self.hero_img_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
        # 由上可知需要获得每一个英雄括号内容URL = https://pvp.qq.com/web201605/js/herolist.json
        self.hero_img_info_url = 'https://pvp.qq.com/web201605/js/herolist.json'

    # 不需要重复做的事情单独返回作为参数传入
    def get_hero_img_info(self):
        # 实例化
        session = HTMLSession()
        # 发送请求
        res = session.get(self.hero_img_info_url)
        # print(res.json())
        return res

    # 将需要重复做的事情封装起来，添加到进程池中
    def get_hero_img_url(self,i):
        # 实例化
        session = HTMLSession()
        hero_path = self.os_path + "/" + i["cname"] + "/"
        if not os.path.exists(hero_path):
            os.makedirs(hero_path)
        #切割皮肤字符串，一来得到皮肤数量二来得到皮肤名字
        skin_total = i["skin_name"].split("|")
        # 用枚举法获得索引与对应的皮肤名 你index+1 不然你的皮肤序号会和你的皮肤名称对不上 你再来试试
        for index,item in enumerate(skin_total):
            hero_img_url = self.hero_img_url.format(i["ename"],i["ename"],index+1)
            res_hero = session.get(hero_img_url).content
            # 存入
            with open(hero_path + "{}.png".format(item),"wb") as f:
                f.write(res_hero)
            print("{}:{}上传完毕".format(i["cname"],item))

if __name__ == '__main__':
    Wangzhe_Spider = Wangzhe_Spider()
    data = Wangzhe_Spider.get_hero_img_info()
    # 利用线程池提高爬取效率
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for i in data.json():
            executor.submit(Wangzhe_Spider.get_hero_img_url,i)
