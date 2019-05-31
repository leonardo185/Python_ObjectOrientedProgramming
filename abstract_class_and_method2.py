from abc import ABCMeta, abstractmethod
class Product(metaclass = ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class Furniture(Product):
    def return_policy(self):
        print("Furnitures cannot be returned.")

Furniture().return_policy()
