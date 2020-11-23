from typing import Union
import requests
from fake_useragent import UserAgent
import json


class Spyder:
    def __init__(self):
        ua = UserAgent()

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
            'User-Agent': ua.random,
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.data = {
            'Lat': '24.749137720314668',
            'Lon': '121.74193843521877',
            'Range': '800',
            'Type': '1'
        }

    def getRefuse_Trucks_Position(self, routeId: str) -> Union[list, bool]:
        """
        Use requests to get the refuse trucks data from APIs.
        :param routeId: filter the route by id.
        :rtype bool
        """
        try:
            rs = requests.post(url=self.url, data=self.data, headers=self.headers)
            jData = json.loads(rs.content.decode())
            for data in jData:
                if data['RouteID'] == routeId:
                    if data['CarLat'] and data['CarLon']:
                        return [data['CarLat'], data['CarLon']]
                    else:
                        return False
                break
            return False
        except ConnectionError:
            print('Request has been reject, pls wait and retry')


if __name__ == '__main__':
    obj = Spyder()
    obj.getRefuse_Trucks_Position('55')
