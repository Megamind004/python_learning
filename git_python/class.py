import math
class orrientation:
    def __init__(self, x_pos, y_pos , degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = orrientation.getUnitVectorFromDegrees(degrees)

    def getUitVectorFromDegrees(degrees): 
        radians = (degrees / 180 ) * math.pi
        return math.sin(radians), -math.cos(radians)
    
    def getNextPos(self) : 
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir

myOrientation = orrientation( 5 , 5 , 75)
myOrientation.getNextPos()


