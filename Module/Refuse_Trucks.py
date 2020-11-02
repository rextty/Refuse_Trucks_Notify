from Module import tk_Notify
from entity import coordinate

import winsound
import datetime
import requests
import random
import time
import json


class Refuse_trucks:
    def __init__(self):
        self.tk = tk_Notify.Notify()

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

    def getRefuse_Trucks_Position(self):
        pass

    def start(self, coor: coordinate, routeId: str = '55', stationName: str = '未設站點名稱', checkDelay: int = 10) -> bool:
        while 1:
            rs = requests.post(url=self.url, data=self.data, headers=self.headers)
            jData = json.loads(rs.content.decode())
            for data in jData:
                if data['RouteID'] == routeId:
                    result = self.checkCoordinateInRange(coor,
                                                         data['CarLat'],
                                                         data['CarLon'])
                    if result:
                        winsound.MessageBeep(20)
                        self.tk.showNotify('垃圾車到點通知', f'垃圾車已到達: {stationName} 此站點')
                        return True
                    break
            time.sleep(checkDelay)

    @staticmethod
    def checkCoordinateInRange(coor: coordinate, checkLa: float, checkLo: float) -> bool:
        startLa = coor.getStartCoorLa
        startLo = coor.getStartCoorLo
        endLa = coor.getEndCoorLa
        endLo = coor.getEndCoorLo

        if startLa > endLa and endLo > startLo:
            return endLa <= checkLa <= startLa and checkLo <= coordinate2 <= endLo

    @staticmethod
    def checkCurrentTimeInRange(startTime: str, endTime: str) -> bool:
        """
        To check current time is in range.
        :param startTime: range start.
        :param endTime: range end.
        :rtype bool
        Time format use military time,
        and args ues space in string to separate,
        support year, month, day, hour, min, NO Second!!
        e.g. "2020 11 2 17 30"
        """
        if len(startTime.split(' ')) is not len(endTime.split(' ')):
            raise ValueError

        curTimeList = time.strftime('%Y %m %d %H %M', time.localtime()).split(' ')

        args = 5 - len(startTime.split(' '))

        tempTime = ''
        for index, x in enumerate(range(args)):
            tempTime += f'{curTimeList[index]} '

        startYear, startMonth, startDay, startHour, startMin = map(int, (tempTime + startTime).split(' '))
        endYear, endMonth, endDay, endHour, endMin = map(int, (tempTime + endTime).split(' '))
        curYear, curMonth, curDay, curHour, curMin = map(int, time.strftime('%Y %m %d %H %M', time.localtime()).split(' '))

        startDateTime = datetime.datetime(startYear, startMonth, startDay, startHour, startMin, 00)
        endDateTime = datetime.datetime(endYear, endMonth, endDay, endHour, endMin, 00)
        currDateTime = datetime.datetime(curYear, curMonth, curDay, curHour, curMin, 00)

        startTimestamp = time.mktime(startDateTime.timetuple())
        endTimestamp = time.mktime(endDateTime.timetuple())
        timesTimestamp = time.mktime(currDateTime.timetuple())

        return startTimestamp <= timesTimestamp <= endTimestamp


if __name__ == '__main__':
    obj = Main()
    obj.start()
