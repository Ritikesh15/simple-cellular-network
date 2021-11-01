import math

class Coordinate :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "( "+str(self.x)+" , "+str(self.y)+" )"

    def distance_between_points(self, coord):
        distance = math.sqrt((self.x-coord.x)*(self.x-coord.x)+(self.y-coord.y)*(self.y-coord.y))
        return distance
