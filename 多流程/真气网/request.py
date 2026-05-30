import requests
import execjs
import os

# 读取JavaScript文件
js_path = os.path.join(os.path.dirname(__file__), '真气网.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js_code = f.read()

# 创建JavaScript运行环境
ctx = execjs.compile(js_code)

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.zq12369.com",
    "Pragma": "no-cache",
    "Referer": "https://www.zq12369.com/environment.php?date=2025-06-12&tab=rank&order=DESC&type=DAY",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

cookies = {
    "city": "%E6%9D%AD%E5%B7%9E"
}

url = "https://www.zq12369.com/api/newzhenqiapi.php"

# 调用JavaScript函数生成param参数
param = ctx.call('getParam', 'POST', {
    'date': '2025-06-12',
    'tab': 'rank',
    'order': 'DESC',
    'type': 'DAY'
})

data = {
    "param": param
}

response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)