from os import name


class Person:
    def __init__(self, name = None, mobile = None, office = None, email = None):
        self.__name = name
        self.__mobile = mobile
        self.__office = office
        self.__email = email
    
    def __str__(self):
        return f"{self.__name}, {self.__mobile}, {self.__office}, {self.__email}"
    
    def getName(self):
        return self.__name
    def getMobile(self):
        return self.__mobile
    def getOffice(self):
        return self.__office
    def getEmail(self):
        return self.__email
    
    def setName(self, name):
        self.__name = name
    def setMobile(self, mobile):
        self.__mobile = mobile
    def setOffice(self, office):
        self.__office = office
    def setEmail(self, email):
        self.__email = email

p1 = Person("Kim", office="1234567", email="kem@company.com")
p2 = Person("Park", office="2345678")
p2.setEmail("park@company.com")

print(p1)
print(p2)