class Customer:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = None

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer(100, "Gopal", 24)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
