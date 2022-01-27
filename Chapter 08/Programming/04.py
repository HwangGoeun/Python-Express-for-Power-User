import turtle

class Rectangle:
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
    
    def __str__(self):
        return f"좌표 = ({self.__x}, {self.__y}), 크기 = {self.getArea()}"

    
    def getX(self):
        return int(self.__x)
    def getY(self):
        return int(self.__y)
    def getW(self):
        return int(self.__w)
    def getH(self):
        return int(self.__h)
    def getX1(self):
        return int(self.__x + self.__w)
    def getY1(self):
        return int(self.__y + self.__h)

    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setW(self, w):
        self.__w = w
    def setH(self, h):
        self.__h = h
    

    def getArea(self):
        return self.__w * self.__h    
    
    # 모든 조건을 입력해놓지 않았음.
    def overlap(self, r):
        if(((self.getX() < r.getX1()) and (r.getX1() < self.getX1())) and ((self.getY() < r.getY()) and (r.getY() < self.getY1))):
            return "도형이 겹칩니다."
        else:
            return "도형이 겹치지 않습니다."

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(-10, -300, 100, 100)
#r1.overlap(r2)

t = turtle.Turtle()
t.shape("turtle")

t.goto(0, 0)
for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-10, -300)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.write(r1.overlap(r2))

turtle.done()
