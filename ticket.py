class Ticket:
    counter = -1
    def __init__(self, passenger, source, destination):
        self.__pasenger_name = str(passenger)
        self.__source = source
        self.__destination = destination
        Ticket.counter += 1

    def validate_source_destination(self):
        destination_list = ["Mumbai", "Chennai", "Pune", "Kolkata"]
        if (self.__source == "Delhi" and (self.__destination in destination_list)):
            return True
        else:
            return False

    def generate_ticket(self):
        if(Ticket.validate_source_destination(self)):
            if(Ticket.counter < 10):
                self.ticket_id = self.__source[0] + self.__destination[0] + "0" + str(Ticket.counter)
                return True
            else:
                self.ticket_id = self.__source[0] + self.__destination[0] + str(Ticket.counter)
                return True
        else:
            return False

    def get_ticket_id(self):
        if(Ticket.generate_ticket(self)):
            print(self.ticket_id)
        else:
            print("Ticket does not exist.")

    def get_passenger_name(self):
        if(Ticket.generate_ticket(self)):
            print(self.__pasenger_name)
        else:
            print("Ticket does not exist.")

    def get_source(self):
        if(Ticket.generate_ticket(self)):
            print(self.__source)
        else:
            print("Ticket does not exist.")

    def get_destination(self):
        if(Ticket.generate_ticket(self)):
            print(self.__destination)
        else:
            print("Ticket does not exist.")

t1 = Ticket("xyz", "Delhi", "Mumbai")
t1.validate_source_destination()
t1.generate_ticket()
t1.get_ticket_id()
t1.get_passenger_name()
t1.get_source()
t1.get_destination()
print("")
