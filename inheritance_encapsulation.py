class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the phone class.")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def check(self):
        print(self.price)

s1 = SmartPhone(10000, "Apple", "12Mp")
s1.check()
