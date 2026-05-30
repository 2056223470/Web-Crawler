import hashlib
import requests
import time

def get_millis():
    return int(round(time.time() * 1000))

def comeRequests(mode='GET',url='',data=None):
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
        'accept':'*/*',
        'referer': 'https://www.kugou.com/'
    }
    restore = requests.request(mode, url, json=data, headers=header)
    if restore.status_code == 200:
        return restore.json()
    else:
        print(restore.status_code,restore.text)
        return None

# 获得 酷狗 歌词 输入关联
def api_GetSearchTip(tips):
    timesp = str(get_millis())
    url = f'https://searchtip.kugou.com/getSearchTip?MusicTipCount=5&MVTipCount=2&albumcount=2&keyword={tips}&callback=&_={timesp}'
    req = comeRequests(url=url)
    print(req)

def api_song(music_name):
    data_1 = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0clienttime=1740142868855clientver=1000dfid=4XRhXm1KFlcg28UKYR2B97ROfilter=10inputtype=0iscorrection=1isfuzzy=0keyword={music_name}mid=283e67ab46491a317bab712907a00236page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid=283e67ab46491a317bab712907a00236NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    data_signature =  md5(data_1)
    url = f'https://complexsearch.kugou.com/v2/search/song?srcappid=2919&clientver=1000&clienttime=1740142868855&mid=283e67ab46491a317bab712907a00236&uuid=283e67ab46491a317bab712907a00236&dfid=4XRhXm1KFlcg28UKYR2B97RO&keyword={music_name}&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature={data_signature}'
    req = requests.get(url=url)
    print(req.text)



def md5(text):
    md5Obj = hashlib.md5()
    md5Obj.update(text.encode('utf-8'))
    return md5Obj.hexdigest()




if __name__ == '__main__':
    api_song('一路向北')
    # api_GetSearchTip('一路向北')


# 小纸条 ： 小B 我们晚上一起吃个饭呗  01067a9f54efdddcca287ebc4a1a9935

# 小纸条 传到 C 手中 修改了  小B 我们分手吧 01067a9f54efdddcca287ebc4a1a9935

# 小纸条 传到了 B 手中   988b7ce6a19f0b6d4571682aa7107086 ！= 01067a9f54efdddcca287ebc4a1a9935














    #   讲课 先 讲轨迹

















