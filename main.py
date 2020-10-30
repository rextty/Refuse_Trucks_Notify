from Module import tk_Notify
import winsound
import datetime
import requests
import random
import time
import json


class Main:
    def __init__(self):
        self.tk = tk_Notify.Notify()
        self.coordinateRange = [24.748443, 121.732561, 24.748210, 121.732792]
        self.coordinateRange = [24.745237, 121.747698, 24.744356, 121.748829]

        self.url = 'http://clean.ilepb.gov.tw/YLBarBageAPI/API/GetCollectInfoByCoor.ashx'
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '62',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'clean.ilepb.gov.tw',
            'Origin': 'http://clean.ilepb.gov.tw',
            'Referer': 'http://clean.ilepb.gov.tw/YLRtCQS/RefusetrucksLive.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.data = {
            'Lat': '24.749137720314668',
            'Lon': '121.74193843521877',
            'Range': '800',
            'Type': '1'
        }

    def start(self):
        while 1:
            if datetime.date.today().isoweekday() is 1 or 2 or 4 or 5:
                if self.checkTimeInRange('16 30', '17 05', time.strftime('%H %M', time.localtime())):
                    rs = requests.post(url=self.url, data=self.data, headers=self.headers)
                    jData = json.loads(rs.content.decode())
                    for data in jData:
                        if data["RouteID"] == '55':
                            result = self.checkCoordinateInRange(self.coordinateRange[0],
                                                                 self.coordinateRange[1],
                                                                 self.coordinateRange[2],
                                                                 self.coordinateRange[3],
                                                                 data["CarLat"], data["CarLon"])
                            if result:
                                winsound.MessageBeep(20)
                                self.tk.showNotify('垃圾車通知', '你差不多該出門了')
                                time.sleep(5)
                                winsound.MessageBeep(20)
                                self.tk.showNotify('垃圾車通知', '你差不多該出門了')
                                return 1
                            break
                    time.sleep(8)
                else:
                    time.sleep(5)
            else:
                break

    @staticmethod
    def checkCoordinateInRange(la1, lo1, la2, lo2, coordinate1, coordinate2):
        try:
            la1 = float(la1)
            lo1 = float(lo1)
            la2 = float(la2)
            lo2 = float(lo2)
            coordinate1 = float(coordinate1)
            coordinate2 = float(coordinate2)
        except ValueError as e:
            print(f'Type Error, should be float\n{e}')
        if la1 > la2 and lo2 > lo1:
            return la2 <= coordinate1 <= la1 and lo1 <= coordinate2 <= lo2

    def checkTimeInRange(self, startTime, endTime, times):
        if ' ' in startTime and ' ' in endTime and ' ' in times:
            currentY, currentM, currentD = int(time.strftime("%Y %m %d", time.localtime()).split(' ')[0]),\
                                           int(time.strftime("%Y %m %d", time.localtime()).split(' ')[1]),\
                                           int(time.strftime("%Y %m %d", time.localtime()).split(' ')[2])

            startTimeH, startTimeM = int(startTime.split(' ')[0]), int(startTime.split(' ')[1])
            endTimeH, endTimeM = int(endTime.split(' ')[0]), int(endTime.split(' ')[1])
            timesH, timesM = int(times.split(' ')[0]), int(times.split(' ')[1])

            startT = datetime.datetime(currentY, currentM, currentD, startTimeH, startTimeM, 00)
            endT = datetime.datetime(currentY, currentM, currentD, endTimeH, endTimeM, 00)
            timesT = datetime.datetime(currentY, currentM, currentD, timesH, timesM, 00)

            startTimestamp = time.mktime(startT.timetuple())
            endTimestamp = time.mktime(endT.timetuple())
            timesTimestamp = time.mktime(timesT.timetuple())

            return startTimestamp <= timesTimestamp <= endTimestamp
        else:
            return 'Type Error'


if __name__ == '__main__':
    obj = Main()
    obj.start()
