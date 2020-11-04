from Controller import Refuse_Trucks
from Entity import coordinate


class Main:
    def __init__(self):
        refuse = Refuse_Trucks.Refuse_Trucks()

        takeCorDOT = coordinate.coordinate([24.741969, 121.747007], [0.0, 0.0])
        refuse.start(takeCorDOT, stationName="去收垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10", deviation=50)

        dropCorDOT = coordinate.coordinate([24.748202, 121.731988], [0.0, 0.0])
        refuse.start(dropCorDOT, stationName="去丟垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10", deviation=50)


if __name__ == '__main__':
    obj = Main()

