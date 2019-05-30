class Mobile:
    def __init__(self, brand, price):
        print("Inside the constructor.")
        self.brand = brand
        self.price = price

    def purchase(self):
        print("Purchasing a Mobile")
        print(f"This Mobile has a brand of {self.brand} and price {self.price}")

mob1 = Mobile("Apple", 70000)
mob1.purchase()

mob2 = Mobile("Samsung", 30000)
mob2.purchase()
