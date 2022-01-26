class Box:
    def __init__(self, l = 0, h = 0, d = 0):
        self.__length = l
        self.__height = h
        self.__depth = d
    
    def __str__(self):
        return f"({self.__length}, {self.__height}, {self.__depth})"
    
    def getLength(self):
        return self.__length
    
    def getheight(self):
        return self.__height

    def getdepth(self):
        return self.__depth

    def setLength(self, l):
        self.__length = l
    
    def setHeight(self, h):
        self.__length = h
    
    def setDepth(self, d):
        self.__length = d
    
b1 = Box(100, 100, 100)
print(b1)    
print("상자의 부피는", b1.getheight() * b1.getLength() * b1.getdepth())