


class Mobile:
    discount = 50
    def __init__(self, price, brand):
        self.__price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)

    @staticmethod
    def get_discount(self):
        return self.discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

m = Mobile(400, "asdf")
print(Mobile.get_discount(m))
