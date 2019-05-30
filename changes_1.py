def change(strng):
    print("Object ID before modification inside the function:" +str(strng) ,id(strng))
    strng=strng.upper()
    print("Object ID after modification inside the function: "+str(strng),id(strng))

s1="hello"
change(s1)
print(s1)
