class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.brand = brand
        self.price = price

    def purchase(self):
        total = self.price - self.price * Mobile.discount/100
        print (self.brand, "mobile with price", str(self.price), "is available after discount at", str(total))

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

mob1.purchase()
mob2.purchase()
mob3.purchase()
