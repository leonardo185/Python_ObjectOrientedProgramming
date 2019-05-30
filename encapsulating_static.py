class Mobile:
    __discount = 50

    def get_discount(self):
        return Mobile.__discount

    def set_discount(self, discount):
        Mobile.__discount = discount

m1 = Mobile()
print(m1.get_discount())
m1.set_discount(20)
print(m1.get_discount())
