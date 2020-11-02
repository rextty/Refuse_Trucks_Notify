from Controller import Refuse_Trucks
from Entity import coordinate


class Main:
    def __init__(self):
        refuse = Refuse_Trucks.Refuse_Trucks()

        dropCor = coordinate.coordinate([24.749430, 121.731623], [24.747384, 121.733770])
        takeCor = coordinate.coordinate([24.745320, 121.748515], [24.744045, 121.750691])

        refuse.start(coor=takeCor, stationName="收垃圾", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10")
        refuse.start(coor=dropCor, stationName="出門", dayList=[1, 2, 4, 5], startTime="16 30", endTime="17 10")


if __name__ == '__main__':
    obj = Main()

