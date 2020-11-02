from typing import List


class coordinate:
    def __init__(self, startCoor: List[float], endCoor: List[float]):
        """
        Normal coordinate range's entity.
        :param startCoor: range start.
        :param endCoor: range end.
        Coordinate format e.g. ([24.748443, 121.732561], [24.748210, 121.732792])
        """
        self.startCoorLa, self.startCoorLo = startCoor
        self.endCoorLa, self.endCoorLo = endCoor

    def getStartCoorLa(self):
        return self.startCoorLa

    def getStartCoorLo(self):
        return self.startCoorLo

    def getEndCoorLa(self):
        return self.endCoorLa

    def getEndCoorLo(self):
        return self.endCoorLo

    def setStartCoorLa(self, coor):
        self.startCoorLa = coor

    def setStartCoorLo(self, coor):
        self.startCoorLo = coor

    def setEndCoorLa(self, coor):
        self.endCoorLa = coor

    def setEndCoorLo(self, coor):
        self.endCoorLo = coor
