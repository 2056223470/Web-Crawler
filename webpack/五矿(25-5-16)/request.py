# 整个流程是：
# 1.Python创建一个临时的JavaScript文件
# 2.这个临时文件导入并调用params.js中的函数
# 3.使用Node.js执行这个临时文件
# 4.获取执行结果
# 5.清理临时文件
# 6.使用获取到的结果发送HTTP请求
# 这种方式的优点是：
# 1.可以方便地在Python中调用JavaScript代码
# 2.不需要修改原始的JavaScript代码
# 3.可以动态传递参数
# 4.可以捕获执行结果和错误信息
import subprocess
import os
import json
import requests

def run_js_file(function_name, **kwargs):
    """
    运行JavaScript文件中的特定方法
    :param function_name: 要调用的JavaScript函数名
    :param kwargs: 要传递给函数的参数
    :return: 函数执行结果
    """
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    js_file_path = os.path.join(current_dir, 'params.js')
    
    # 将参数转换为JavaScript对象字符串
    params_str = json.dumps(kwargs)
    
    # 创建一个临时的JavaScript文件来调用指定函数
    temp_js = os.path.join(current_dir, 'temp.js')
    with open(temp_js, 'w', encoding='utf-8') as f:
        f.write(f'''
const params = require('./params.js');
const result = params.{function_name}({params_str});
process.stdout.write(JSON.stringify(result));
''')
    
    try:
        # 使用Node.js执行临时JavaScript文件，设置编码为utf-8
        startupinfo = None
        if os.name == 'nt':  # Windows系统
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
        result = subprocess.run(['node', temp_js],
                              capture_output=True,
                              text=True,
                              encoding='utf-8',
                              startupinfo=startupinfo)
        
        # 如果有错误，打印错误信息
        if result.stderr:
            print("错误信息：")
            print(result.stderr)
            return None
            
        # 返回结果
        return result.stdout.strip()
            
    except Exception as e:
        print(f"执行出错：{str(e)}")
        return None
    finally:
        # 删除临时文件
        if os.path.exists(temp_js):
            os.remove(temp_js)

def request_wukuang(params):
    cookies = {
        '__jsluid_s': '82d94b902c05a9a68855f03fa44e7ef5',
        'SUNWAY-ESCM-COOKIE': 'af7a4983-fda0-4c96-9f0d-dbc215cd1784',
        'JSESSIONID': '117B065655DE7B69EC56310DF4B3CA2B',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://ec.minmetals.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    }

    json_data = {
        'param': params
    }

    response = requests.post(
        'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    print(response.text)

if __name__ == "__main__":
    # 示例1：调用params函数
    sign = "cc3ad69e118a9e7a2def803e50cd3a73"
    params = run_js_file('params', sign=sign)
    if params:
        print("生成的params:", params)
        result = request_wukuang(params)
    
    # 示例2：调用其他函数（假设params.js中有其他函数）
    # other_result = run_js_file('otherFunction', param1='value1', param2='value2')
    # print("其他函数结果:", other_result)