# importing what we need
from Read import*
from Operation import *
from Write import *

#starting the loop 
continueLoop = True
#calling the welcome function
wel_message()
while continueLoop == True:
    #calling this function to show all the options
    options()
    try:
        #asking the user to input desired option 
        userInput = int(input('Press 1, 2, 3, or 4 : ' ))

        if userInput == 1:
            laptop_ordered = []
            laptops = Read_txt_file()
            #calling the function that shows all the laptops in text file
            laptop_details()
            #calling function for inputs
            order_name = inputName_buy()
            order_num = inputPhNumber_buy()
            length = len(laptops)
            #calling function for Id
            LaptopID = validId_buy(length)
            #calling function that asks for quantity of laptops and checks the stock
            Quantity = verify_qty_buy(LaptopID)
            
            total_cost = Cal_cost(LaptopID, Quantity, laptops)
            add_order(LaptopID, Quantity, laptops)
            print(f"Your total cost for this purchase with laptop Id {LaptopID} is ${total_cost}")
            #gettin all the inputs/varibles
            laptop_name = laptops[LaptopID][0]
            laptop_brand = laptops[LaptopID][1]
            laptop_price = laptops[LaptopID][2]
    
            laptop_ordered.append([laptop_name, laptop_brand, Quantity, laptop_price, total_cost])

            buy_more = True
            while buy_more == True:
                more_laptop = input("Do you want to buy more laptops Yes/No: ")
                if more_laptop.upper() == "YES":
                    laptops = Read_txt_file()
                    laptop_details()   
                    LaptopID = validId_buy(length)
                    Quantity = verify_qty_buy(LaptopID)
                    total_cost = Cal_cost(LaptopID, Quantity, laptops)
                    add_order(LaptopID, Quantity, laptops)
                    print(f"Your total cost for this purchase with laptop Id {LaptopID} is ${total_cost}")
                    
                    #gettin all the inputs/varibles                   
                    laptop_name = laptops[LaptopID][0]
                    laptop_brand = laptops[LaptopID][1]
                    laptop_price = laptops[LaptopID][2]
            
                    laptop_ordered.append([laptop_name, laptop_brand, Quantity, laptop_price, total_cost])
                elif more_laptop.upper() == "NO":
                    buy_more = False
                    order_invoice(order_name, order_num, laptop_ordered)
                    order_invoice_txtFile(order_name, order_num, laptop_ordered)
                else:
                    print("\n")
                    print("\t\t***Please write from the above given options!***")
                    print("\n")
                            
        elif userInput == 2:
            laptop_sold = []
            laptops = Read_txt_file()
            #calling the function that shows all the laptops in text file
            laptop_details()
            #calling function for inputs
            sell_name = inputName_sell()
            sell_num = inputPhNumber_sell()
            length = len(laptops)
            #calling function for Id
            LaptopID = validId_sell(length)
            #calling function that asks for quantity of laptops and checks the stock
            Quantity = verify_qty_sell(laptops, LaptopID)
            total_amt_sold = Cal_amt(LaptopID, Quantity, laptops)
            sub_sold(LaptopID, Quantity, laptops)
            print(f"Your total amount for this purchase with laptop Id {LaptopID} is ${total_amt_sold}")
            #gettin all the inputs/varibles
            laptop_name = laptops[LaptopID][0]
            laptop_brand = laptops[LaptopID][1]
            laptop_price = laptops[LaptopID][2]
            laptop_sold.append([laptop_name, laptop_brand, Quantity, laptop_price, total_amt_sold])
            sell_more = True
            while sell_more == True:
                sell_laptop = input("Do you want to sell more laptops Yes/No: ")
                if sell_laptop.upper() == "YES":
                    laptops = Read_txt_file()
                    laptop_details()   
                    LaptopID = validId_sell(length)
                    Quantity = verify_qty_sell(laptops, LaptopID)
                    total_amt_sold = Cal_amt(LaptopID, Quantity, laptops)
                    sub_sold(LaptopID, Quantity, laptops)
                    print(f"Your total amount for this purchase with laptop Id {LaptopID} is ${total_amt_sold}")
                    
                    #gettin all the inputs/varibles
                    laptop_name = laptops[LaptopID][0]
                    laptop_brand = laptops[LaptopID][1]
                    laptop_price = laptops[LaptopID][2]
                    
                    laptop_sold.append([laptop_name, laptop_brand, Quantity, laptop_price, total_amt_sold])
                elif sell_laptop.upper() == "NO":
                    sell_more = False
                    shippingcost = input("Dear user do you want the product to be shipped or not Yes/No:")
                    if shippingcost.upper() == "YES":
                        sell_recepit_SP(sell_name, sell_num, laptop_sold)
                        sell_recepit_SP_txtFile(sell_name, sell_num, laptop_sold)
                    elif shippingcost.upper() == "NO":
                        sell_recepit(sell_name, sell_num, laptop_sold)
                        sell_recepit_txtFile(sell_name, sell_num, laptop_sold)
                    else:
                        print("\t\t***Please enter Yes or No!***")
                else:
                    print("\n")
                    print("\t\t***Please write from the above given options!***")
                    print("\n")

        elif userInput == 3:
            laptop_details()     
        elif userInput == 4:
            continueLoop = False
        else:
            print("\n")
            print('*****Please enter only from the Options given!*****')
            print("\n")
    except:
        print("\n")
        print("*****Please input NUMBERS only!*****")
        print("\n")
    
        
