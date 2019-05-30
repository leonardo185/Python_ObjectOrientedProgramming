#OOPR-Assgn-5
#Start writing your code here

class vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost, premium_amount):
        self.__veicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__vehicle_cost = vehicle_cost
        self.__premium_amount = premium_amount

    def calcualte_premium(self):
        if(self.__vehicle_type == "Two Wheeler" or self.__vehicle_type == "Four Wheeler"):
            if(self.__vehicle_type == "Two Wheeler"):
                self.__premium_amount = 2
                vehicle_premium = self.__vehicle_cost * self.__premium_amount/100
                self.__vehicle_cost = self.__vehicle_cost + vehicle_premium
            else:
                self.__premium_amount = 4
                vehicle_premium = self.__vehicle_cost * self.__premium_amount/100
                self.__vehicle_cost = self.__vehicle_cost + vehicle_premium
        else:
            print("Vehicle type is invalid.")

    def display_vehicle_details(self):
        print("Vehicle ID: " +str(self.__veicle_id))
        print("Vehicle Type:" +str(self.__vehicle_type))
        print("Vehicle Premium:"+str(self.__premium_amount))
        print("Vehicle Cost:"+str(self.__vehicle_cost))

vehicle1 = vehicle(1, "Two Wheeler", 40000, 2)
vehicle1.calcualte_premium()
vehicle1.display_vehicle_details()
