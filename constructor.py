class Mobile:
    def __init__(self, brand, price):
        print("Inside the constructor.")
        self.brand = brand
        self.price = price

mob1 = Mobile("Apple", 70000)
mob2 = Mobile("Samsung", 3000)

print(f"Mobile 1 has a brand name of {mob1.brand} and a price of {mob1.price}")
print(f"Mobile 2 has a brand name of {mob2.brand} and a price of {mob2.price}")
