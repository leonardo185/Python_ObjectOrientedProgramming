def change_function(data):
    print ("Id of list received in method", id(data))
    data = [200, 300, 400]
    print ("Id of list after list assignment in method and inside the method"+str(data) , id(data))

value = [100, 200, 300]
print ("List and its id before method call", value, id(value))
change_function(value)
print ("List and its id after method call ", value, id(value))
