class Rectangle:
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
    
    def __str__(self):
        return f"좌표 = ({self.__x}, {self.__y})"
    
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getW(self):
        return self.__w
    def getH(self):
        return self.__h
    
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setW(self, w):
        self.__w = w
    def setH(self, h):
        self.__h = h
    
    def getArea(self):
        return self.__x * self.__y
    
    def overlap(self, r):
        if (self.__x < r.__x + r.__w or self.__x + self.__w > r.__x) and (self.__y < r.__y + r.h or self.__y + self.__h > r.__y)
            print(f"{self}와 {r}은 서로 겹칩니다.")
        else:
            print(f"{self}와 {r}은 서로 겹치지 않습니다.")

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)
r1.overlap(r2)