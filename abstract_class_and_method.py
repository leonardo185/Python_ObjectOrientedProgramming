from abc import ABCMeta, abstractmethod

class Product(metaclass = ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

Product() 
