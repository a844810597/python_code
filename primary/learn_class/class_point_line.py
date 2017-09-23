import math

class Point:
    def __init__(self, x=0, y=0):
        self.pos_x = x
        self.pos_y = y

    def getPostion(self):
        return (self.pos_x, self.pos_y)

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def getLen(self):
        delta_x = self.point_1.pos_x - self.point_2.pos_x
        delta_y = self.point_1.pos_y - self.point_2.pos_y
        length = math.sqrt(delta_x*delta_x + delta_y*delta_y)
        return length
    
