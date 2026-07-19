#!/usr/bin/env python
# coding:utf-8
"""
豆瓣登录页滑块验证码示例：DrissionPage 驱动浏览器 + 超级鹰识别缺口坐标。

账号、密码、超级鹰 soft_id 请通过环境变量注入，勿写入代码仓库：
  DOUBAN_USERNAME / DOUBAN_PASSWORD
  CHAOJIYING_USERNAME / CHAOJIYING_PASSWORD / CHAOJIYING_SOFT_ID
"""

import os
import requests
from hashlib import md5
from DrissionPage import Chromium, ChromiumOptions
from DrissionPage.common import Settings


def main():
    username = os.getenv("DOUBAN_USERNAME", "your_douban_username")
    password = os.getenv("DOUBAN_PASSWORD", "your_douban_password")
    cjy_user = os.getenv("CHAOJIYING_USERNAME", username)
    cjy_pass = os.getenv("CHAOJIYING_PASSWORD", password)
    soft_id = os.getenv("CHAOJIYING_SOFT_ID", "your_soft_id")

    Settings.set_language('zh_cn')  # 设置为英文时，填入'en'
    # 设置器实例
    co = ChromiumOptions()
    # 设置路径（可按本机 Edge 安装位置修改）
    co.set_browser_path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
    # 设置无痕模式
    co.incognito()
    # 连接浏览器 并将设置器传入
    browser = Chromium(co)
    # 获取标签页对象
    tab = browser.latest_tab
    tab.set.window.max()
    tab.get('https://www.douban.com/')
    tab.wait(2)
    tab.ele('密码登录').click()
    tab.ele('.account-form-input').input(username)
    tab.ele('.account-form-input password').input(password)
    tab.ele('登录豆瓣').click()
    tab.wait(1)
    content = tab.ele('#tcaptcha_iframe_dy').ele('.tc-bg-img unselectable').attr('style')
    url = content.split('("')[1].split('")')[0]
    formUrlToSaveImg(url, 'douban.jpg')

    # 超级鹰提取坐标
    chaojiying = Chaojiying_Client(cjy_user, cjy_pass, soft_id)
    im = open('./douban.jpg', 'rb').read()
    result = chaojiying.PostPic(im, 9901)
    print(result)
    # 拖动滑块
    position = int(result["pic_str"].split(',')[0])
    print(position)
    x = 278 / 672 * position - 40
    print(x)
    tab.ele('#tcaptcha_iframe_dy').ele('.tc-fg-item tc-slider-normal').drag(int(x), 0, 3)


# 保存图片
def formUrlToSaveImg(url, filename):
    img_response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(img_response.content)


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64': base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    main()
