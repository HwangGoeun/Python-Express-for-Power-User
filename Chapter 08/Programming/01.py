class Cat:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return "{} {}".format(self.__name, self.__age)
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name
    
    def setAge(self, age):
        self.__age = age

missy = Cat('Missy', 3)
lucky = Cat('lucky', 5)
print(missy)
print(lucky)