#for option 1 Buy:
#asking for the manufacturer's name
def inputName_buy():
    name = str(input("Enter the Manufacturer's name: "))
    return name

#asking for the manufacturer's phone number
def inputPhNumber_buy():
    Loop = True
    while Loop == True:
        try:
            phoneNum = int(input("Enter the Manufacturer's Phone Number: "))
            Loop = False
            return phoneNum
        except:
            print("\t\t***Please enter a vaild Phone Number!***")

#checks for the validity of ID entered by the user
def validId_buy(length):
    #loop for the question if the id is not valid
    loop = True
    while loop == True:
        #using try and except for a input error
        try:
            valid_id = int(input("Please Provide the ID of the laptop you want to Buy: "))
            loop = False
        except:
            print("\t\t***Please enter Numbers only!***")
    #using while loop for the correct Id
    while valid_id <= 0 or valid_id > length:
        print("\t\t***Please provide a valid LAPTOP ID!***")
        valid_id = int(input("Please Provide the ID of the laptop you want to Buy: "))
    return valid_id

#asks for quantity from the user and also the check if it's available in the stock
def verify_qty_buy(LaptopID):
    loop = True
    while loop:
        try:
            get_qty = int(input(f"Please Provide the quantity of laptop with ID {LaptopID} you want to buy: "))
            while get_qty <= 0:
                print("\t\t***Please order one or more than one Laptops!***")
                print("\n")
                get_qty = int(input(f"Please Provide the quantity of laptop with ID {LaptopID} you want to buy: "))
            loop = False
            return get_qty
        except ValueError:  
            print("\t\t***Please provide a valid Quantity number.***")
    

def Cal_cost(LaptopID, Quantity, laptops):
    unit_price = int(laptops[LaptopID][2])
    tcost = unit_price * Quantity
    return tcost
    

#updating the stock
def update_list(laptops):
    with open ('laptopfile.txt','w')as file:
        for values in laptops.values():
            file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))
            file.write("\n")

        
#adding the order to the stock
def add_order(LaptopID, Quantity, laptops):
    laptops[LaptopID][3] = str(int(laptops[LaptopID][3]) + Quantity)
    update_list(laptops)
    return("")
    
    

    
#for option 2 Sell:
def inputName_sell():
    name = str(input("Enter the Customer's name: "))
    return name

def inputPhNumber_sell():
    Loop = True
    while Loop == True:
        try:
            phoneNum = int(input("Enter the Customer's Phone Number: "))
            Loop = False
            return phoneNum
        except:
            print("\t\t***Please enter a vaild Phone Number!***")

def validId_sell(length):
    #loop for the question if the id is not valid
    loop = True
    while loop == True:
        #using try and except for a input error
        try:
            valid_id = int(input("Please Provide the ID of the laptop you want to Sell: "))
            loop = False
        except:
            print("\t\t***Please enter Numbers only!***")
    #using while loop for the correct Id
    while valid_id <= 0 or valid_id > length:
        print("\t\t***Please provide a valid LAPTOP ID!***")
        print("\n")
        valid_id = int(input("Please Provide the ID of the laptop you want to Sell: "))
    return valid_id

def verify_qty_sell(laptops, LaptopID):
    for available_qty in laptops:
        available_qty = int(laptops[LaptopID][3])
        not_available = True
        while not_available == True:
            try:
                get_sell_qty = int(input(f"Please Provide the quantity of laptop with ID {LaptopID} you want to Sell: "))
                while get_sell_qty <= 0 or get_sell_qty > available_qty:
                    print(f"\t\t***We don't have enough quantity of Laptop with ID {LaptopID}!***")
                    print("\t\t***Please write a quantity that is available in the stock***")
                    get_sell_qty = int(input(f"Please Provide the quantity of laptop with ID {LaptopID} you want to Sell: "))
                not_available = False
                return get_sell_qty
            except:
                print("\t\t***Please input numbers only for required quantity.***")
    
def Cal_amt(LaptopID, Quantity, laptops):
    unit_price = int(laptops[LaptopID][2])
    sold_cost = unit_price * Quantity
    return sold_cost


def sub_sold(LaptopID, Quantity, laptops):
    laptops[LaptopID][3] = str(int(laptops[LaptopID][3]) - Quantity)
    update_list(laptops)
    return("")
      

