class Mobile:
    def __init__(self, price, brand):
        print ("Inside constructor")
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")
mob2=mob1
mob2.price = 4000
print ("Id of object referred by mob1 reference variable is :" +str(mob1.price))
print ("Id of object referred by mob2 reference variable is :" +str(mob2.price))
#mob1 and mob2 are reference variables to the same object
