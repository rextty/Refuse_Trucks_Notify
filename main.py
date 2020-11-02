from Controller import Refuse_Trucks
from Entity import coordinate


class Main:
    def __init__(self):
        refuse = Refuse_Trucks.Refuse_Trucks()

        takeCor = coordinate.coordinate([24.742533, 121.748329], [24.741387, 121.750880])
        dropCor = coordinate.coordinate([24.748711, 121.731357], [24.747038, 121.733112])

        refuse.start(coor=takeCor, stationName="收垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10")
        refuse.start(coor=dropCor, stationName="出門", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10")

        # Take Normal version
        takeCorNormal = coordinate.coordinate([24.742533, 121.748329], [24.741387, 121.750880])
        refuse.start(takeCorNormal, stationName="兩點範圍收垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10")

        # Take Dot version
        # takeCorDOT = coordinate.coordinate([24.741969, 121.747007], [0.0, 0.0])
        refuse.start(takeCorDOT, stationName="一點範圍收垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10", deviation=50)

        # Go Normal version
        dropCorNormal = coordinate.coordinate([24.748711, 121.731357], [24.747038, 121.733112])
        refuse.start(dropCorNormal, stationName="兩點範圍丟垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10")

        # Go Dot version
        dropCorDOT = coordinate.coordinate([24.748202, 121.731988], [0.0, 0.0])
        refuse.start(dropCorDOT, stationName="一點範圍丟垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10", deviation=50)


if __name__ == '__main__':
    obj = Main()

