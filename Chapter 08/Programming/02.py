class Rocket:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self, location):
        return self.location
    
    def moveUp(self):
        self.y += 1

myRocket = Rocket()
print("로켓의 높이:", myRocket.y)

myRocket.moveUp()
print("로켓의 높이:", myRocket.y)