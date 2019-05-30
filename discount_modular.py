def purchase_mobile(price, brand):
    if(brand == "Apple"):
        discount = 10
    else:
        discount = 5
    total_price = price - price * (discount / 100)
    print(f"Total price of Mobile is {total_price}")

def purchase_shoe(price, material):
     if(material == "leather"):
         tax = 5
     else:
         tax = 2
     total_price = price - price * (tax / 100)
     print(f"Total price of Shoe is {total_price}")

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")
