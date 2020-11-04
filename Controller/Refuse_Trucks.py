from Module import Refuse_Trucks_Spyder
from Entity import coordinate

from typing import List
import threading
import winsound
import datetime
import ctypes
import time


class Refuse_Trucks:
    """
    Refuse Trucks controller.
    """
    def __init__(self):
        self.spyder = Refuse_Trucks_Spyder.Spyder()

    def start(self, coor: coordinate,
              routeId: str = '55',
              stationName: str = '未設站點名稱',
              checkDelay: int = 10,
              dayList: List[int] = None,
              startTime: str = None,
              endTime: str = None,
              deviation: int = None):
        """
        To setup a checker,
        and you can setting param for more condition.
        :param coor: Is for coordinate entity.
        :param routeId: RouteId is the refuse trucks route code, 55 for my area.
        :param stationName: A nickname to know where is the refuse trucks at if in the area, the default is "No set station name"
        :param checkDelay: Just a second for request interval, avoid to burden server, e.g. 10
        :param dayList: A list for day condition, e.g. [1, 3, 4, 7]
        :param startTime: Range of time start coordinate e.g. "2020 11 2 16 40".
        :param endTime: Range of time end coordinate e.g. "2020 11 2 17 10".
        :param deviation: A weights for coordinate, also it's a switcher,
        if you want to know more about this args pls see function "checkCurrentTimeInRange" annotation.
        """

        print(f'Start checking... Station Name: {stationName}')
        thread = threading.Thread(target=self.__startListen,
                                  args=(coor,
                                        routeId,
                                        stationName,
                                        checkDelay,
                                        dayList,
                                        startTime,
                                        endTime,
                                        deviation))
        thread.start()

    def __startListen(self, coor, routeId, stationName, checkDelay, dayList, startTime, endTime, deviation):
        """
        Use threading to start a checker.
        """
        while 1:
            if dayList:
                if not self.checkDay(dayList):
                    return False

            if startTime and endTime:
                if not self.checkCurrentTimeInRange(startTime, endTime):
                    time.sleep(2)
                    continue

            position = self.spyder.getRefuse_Trucks_Position(routeId)

            if position:
                result = self.checkCoordinateInRange(coor, position, deviation)

                if result:
                    winsound.MessageBeep(20)
                    ctypes.windll.user32.MessageBoxW(0, f'垃圾車已到達: {stationName} 此站點', '垃圾車到點通知', 0)
                    return True
            time.sleep(checkDelay)

    @staticmethod
    def checkCoordinateInRange(coor: coordinate, checkCoor: List[float], deviation: int) -> bool:
        """
        To check coordinate is in range.
        :param coor: range start and end.
        :param checkCoor: check range.
        :param deviation: A weights for coordinate, also it's a switcher, if you give a number than it's will
        switch to another check coordinate mode "Dot mode", is mean the param "coor" you just give a area center coordinate to "startCoor",
        then it will add the deviation weights to calc the check area, value suggest is 40 ~ 60, cause it's coordinate.
        :rtype bool
        Coordinate format use google map pushpin to get,
        e.g. ([24.748443, 121.732561], [24.748210, 121.732792])
        """
        checkLa, checkLo = map(float, checkCoor)

        if deviation:
            deviation = deviation / 100000
            startLa = coor.getStartCoorLa() + deviation
            startLo = coor.getStartCoorLo() - deviation
            endLa = coor.getStartCoorLa() - deviation
            endLo = coor.getStartCoorLo() + deviation
        else:
            startLa = coor.getStartCoorLa()
            startLo = coor.getStartCoorLo()
            endLa = coor.getEndCoorLa()
            endLo = coor.getEndCoorLo()

        if startLa > endLa and endLo > startLo:
            return endLa <= checkLa <= startLa and startLo <= checkLo <= endLo

    @staticmethod
    def checkCurrentTimeInRange(startTime: str, endTime: str) -> bool:
        """
        To check current time is in range.
        :param startTime: range start, e.g. "2020 11 2 16 40".
        :param endTime: range end, e.g. "2020 11 2 17 10".
        :rtype bool
        Time format use military time,
        and args ues space in string to separate,
        support year, month, day, hour, min, NO Second!!
        e.g. "10 10 00 00" "10 10 23 59", this condition is for Double Ten Day.
        e.g. "16 30" "17 10", this condition is for pre day's 16:30 to 17:10.
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

    @staticmethod
    def checkDay(dayList: List[int]) -> bool:
        """
        To check today is in dayList range.
        :param dayList: List of day, e.g. [1, 2, 3, 4, 5, 6, 7].
        :rtype bool
        dayList format ues number for day,
        e.g. [1, 3, 5, 7], this condition is for odd day.
        e.g. [2, 4, 6], this condition is for even day.
        """
        for day in dayList:
            if day is datetime.date.today().isoweekday():
                return True
        return False


if __name__ == '__main__':
    obj = Refuse_Trucks()
    dropCor = coordinate.coordinate([24.748447, 121.732522], [0.0, 0.0])
    obj.start(dropCor, dayList=[1, 2, 3, 4, 5, 6, 7], startTime="00", endTime="59", deviation=50)
