# 爬取的结果感觉不是很理想，暂时没有优化方向

from requests_html import HTMLSession
import csv

class Spider_12306:
    def __init__(self, data, fs, ts):
        self.session = HTMLSession()
        self.fs = fs
        self.ts = ts
        self.data = data
        # 学生和动车都不勾选 ADULT
        self.str_url = 'https://kyfw.12306.cn/otn/leftTicket/queryR?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
        self.station_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9338'
        self.header = {
            # 暂时不知道这个cookie可以不可以通用，如果不可以可能需要用playwright先获取
            'Cookie': '_uab_collina=174028924463462129025124; JSESSIONID=C458539200A553AA03D122C448AE82E9; _jc_save_wfdc_flag=dc; BIGipServerpassport=854065418.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromDate=2025-04-04; _jc_save_toDate=2025-04-04; BIGipServerportal=3067347210.17183.0000; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u5317%u4EAC%2CBJP; BIGipServerotn=1893269770.64545.0000'
        }
    # 拼接查询url
    def get_url(self):
        end_url = self.str_url.format(self.data, self.fs, self.ts)
        print(end_url)
        return self.get_res(self.session, end_url)
    # 拿到车站表
    def get_station_name(self):
        # 车站名的表
        name_res = self.session.get(self.station_url)
        # 由一长串字符串组成的表，用“|”号拆开
        station_name = name_res.text.split("|")
        return station_name
    # 拿到查询的结果
    def get_res(self, session, url):
        try:
            res = session.get(url, headers=self.header)
            # print(res.text)
            station_name = self.get_station_name()
            return self.get_data(res, station_name)
        except Exception as e:
            print("出现了错误:", e)
    # 马上要进行数据的存储，但是返还的json是以代号显示，存入表中必须对照车站表进行车站代号->车站中文名的转化
    def get_data(self, res, station_name):
        data = []
        response = res.json()["data"]["result"]
        for i in response:
            result = i.split("|")
            dic = {}
            # 列车号
            dic["train_number"] = result[3]
            # 出发地,这里在提取具体的车站代号
            from_spot_E = result[6]
            from_spot_E_index = station_name.index(from_spot_E)
            from_spot_C_index = from_spot_E_index - 1
            dic["from_spot"] = station_name[from_spot_C_index]
            # 目的地，在提取车站代号
            to_spot_E = result[7]
            to_spot_E_index = station_name.index(to_spot_E)
            to_spot_C_index = to_spot_E_index - 1
            dic["to_spot"] = station_name[to_spot_C_index]
            # 发车时间
            dic["departure_time"] = result[8]
            # 各种座次的有无
            dic["seat_1"] = result[30]  # 商务座
            dic["seat_2"] = result[31]  # 一等座
            dic["seat_3"] = result[32]  # 二等座
            dic["seat_4"] = result[23]  # 高级软卧
            dic["seat_5"] = result[28]  # 软卧
            dic["seat_6"] = result[29]  # 动卧
            dic["seat_7"] = result[26]  # 硬卧
            dic["seat_8"] = result[27]  # 软座
            dic["seat_9"] = result[24]  # 硬座
            dic["seat_10"] = result[25] # 无座
            data.append(dic)
        print(data)
        return self.get_csv(data)

    # 数据格式依然是[{}]
    def get_csv(self, data):
        head = ("train_number", "from_spot", "to_spot", "departure_time", "seat_1", "seat_2", "seat_3", "seat_4", "seat_5", "seat_6", "seat_7", "seat_8", "seat_9", "seat_10")
        with open("../素材/12306/车站查询.csv", "w", encoding="utf-8-sig", newline='') as f:
            ws = csv.DictWriter(f, fieldnames=head)
            ws.writeheader()
            ws.writerows(data)
            print(f"{len(data)}条写入完成")


if __name__ == '__main__':
    # 分别传入查询日期，出发地，目的地
    spider = Spider_12306('2025-05-27', 'CSQ', 'BJP')
    spider.get_url()
