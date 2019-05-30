class Mobile:
    discount=50
    def display(self):
        print(self.discount)
         #The above line is valid way of accessing static
        print(Mobile.discount)

    def change(self):
        self.discount=40
        #The above line creates a new attribute
        #instead of modifying the static value
        #Now there are two discount variables,
        #one at class level and the other at object level
        #Hence best is to access Static through class name

m1=Mobile()
m1.display()#Will display 50 and 50

m1.change()
m1.display()#Will display 50 and 40
