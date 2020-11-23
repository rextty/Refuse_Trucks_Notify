from Controller import Refuse_Trucks
from Entity import coordinate


class Main:
    def __init__(self):
        refuse = Refuse_Trucks.Refuse_Trucks()

        testCor = coordinate.coordinate([24.775568, 121.762138], [0.0, 0.0])

        refuse.start(coor=testCor, stationName="測試站點", dayList=[1, 2, 4, 5], startTime="00 00", endTime="23 59", deviation=50)


if __name__ == '__main__':
    obj = Main()
