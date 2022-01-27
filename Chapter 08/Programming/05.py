class Triangle:
    def __init__(self, a1 = 0, a2 = 0, a3 = 0, s = 3):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__numberOfSides = s
    
    def __str__(self):
        return f"({self.__a1}, {self.__a2}, {self.__a3})"
    
    def getAngle1(self):
        return self.__a1
    def getAngle2(self):
        return self.__a2
    def getAngle3(self):
        return self.__a3

    def setAngle1(self, a1):
        self.__a1 = a1
    def setAngle2(self, a2):
        self.__a2 = a2
    def setAngle3(self, a3):
        self.__a3 = a3
    
    def checkAngles(self):
        if self.__a1 + self.__a2 + self.__a3 == 180:
            return "삼각형의 내각의 합은 180도 입니다."
        else:
            return "삼각형의 내각의 합은 180도가 아닙니다."

triangle = Triangle(90, 30, 60)
print(triangle.checkAngles())