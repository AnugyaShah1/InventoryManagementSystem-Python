from datetime import datetime

def wel_message():
    print('\n')
    print("=" * 88)
    print('\t \t \t Welcome to Euphoria Laptop Store')
    print('----------------------------------------------------------------------------------------')
    print('\t \t Address: Kathmandu     Contact: 9930546644')
    print('----------------------------------------------------------------------------------------')
    
def options():
    print("Type 1 to buy from manufacturer")
    print("Type 2 to sell to customer")
    print("Type 3 to Display All Laptops")
    print("Type 4 to exit")
    print("=" * 88)

def laptop_details():
    print('\n')
    print("=========================================================================================")
    print("---------------------------------------LAPTOP LIST---------------------------------------")
    print("=========================================================================================")
    print("S.N. \t Name \t \t Brand \t\t Price \t Quantity  Processor     Graphics ")
    print("-----------------------------------------------------------------------------------------")
    file = open('laptopfile.txt', 'r')
    Laptop_Id = 1
    for line in file:
        print(Laptop_Id, "\t" + line.replace(",", "\t"))
        Laptop_Id += 1
    print("=========================================================================================")
    print("\n")
    file.close()
    return("")

def order_invoice(order_name, order_num, laptop_ordered):
    totalp = 0 
    for i in laptop_ordered:
        totalp += int(i[4])
    vat = 13/100
    grand_total = (vat * totalp) + totalp
    current_time = datetime.now()
    print('\n')
    print("=" * 95)
    print("\t \t \t \t \t The Invoice:  ")
    print("-----------------------------------------------------------------------------------------------")
    print("\t \t \t   Address: Kathmandu   Contact: 9823581391")
    print("=" * 95)
    print("\t \t \t \t \t The Details are: ")
    print("-----------------------------------------------------------------------------------------------\n")
    print("\t\t\t\tInvoice to the Company: " + str(order_name))
    print("Contact Number: " + str(order_num))
    print("Date and Time of purchase: " + str(current_time))
    print("-----------------------------------------------------------------------------------------------")
    print("Laptop name \t Laptop Brand \t Total Quantity \t Unit Price \t Total Price")
    for i in laptop_ordered:
        print(i[0], "\t", i[1],"\t\t", i[2], "\t\t\t", "$", i[3], "\t\t", "$", i[4])

    print("-----------------------------------------------------------------------------------------------")
    print(f"Net Amount is: ${totalp}")
    print(f"Gross Amount is: ${grand_total}")
    print("\t\t\t*** 13% Vat is applied in this product ***")
    print("=" * 95)
    print("\n")

def order_invoice_txtFile(order_name, order_num, laptop_ordered):
    totalp = 0 
    for i in laptop_ordered:
        totalp += int(i[4])
    vat = 13/100
    grand_total = (vat * totalp) + totalp
    current_time = datetime.now()
    with open(str(order_name)+ "_Invoice" + ".txt","w")as file:
        file.write('\n')
        file.write("=" * 95 + "\n")
        file.write("\t \t \t \t \t The Invoice:  \n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\t \t \t   Address: Kathmandu   Contact: 9823581391")
        file.write("=" * 95 +"\n")
        file.write("\t \t \t \t \t The Details are: \n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\tInvoice to the Company: " + str(order_name)+"\n")
        file.write("Contact Number: " + str(order_num)+"\n")
        file.write("Date and Time of purchase: " + str(current_time)+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("Laptop name \t Laptop Brand \t Total Quantity \t Unit Price \t Total Price\n")
        for i in laptop_ordered:
            file.write(str(i[0]) +"\t"+ str(i[1])+"\t\t" + str(i[2])+"\t\t\t"+"$"+ str(i[3]) + "\t\t"+"$"+ str(i[4])+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("Net Amount is: $"+str(totalp)+"\n")
        file.write("Gross Amount is: $"+str(grand_total)+"\n")
        file.write("\t\t\t*** 13% Vat is applied in this product ***\n")
        file.write("=" * 95 +"\n")
    

def sell_recepit(sell_name, sell_num, laptop_sold):
    totalp = 0 
    for i in laptop_sold:
        totalp += int(i[4])
    current_time = datetime.now()
    print('\n')
    print("=" * 95)
    print("\t \t \t \t \t The Receipt:  ")
    print("-----------------------------------------------------------------------------------------------")
    print("\t \t \t   Address: Kathmandu   Contact: 9823581391")
    print("=" * 95)
    print("\t \t \t \t \t The Details are: ")
    print("-----------------------------------------------------------------------------------------------\n")
    print("\t\t\t\tRecepit to the Customer: " + str(sell_name))
    print("Contact Number: " + str(sell_num))
    print("Date and Time of purchase: " + str(current_time))
    print("-----------------------------------------------------------------------------------------------")
    print("Laptop name \t Laptop Brand \t Total Quantity \t Unit Price \t Total Price")
    for i in laptop_sold:
        print(i[0], "\t", i[1],"\t\t", i[2], "\t\t\t", "$", i[3], "\t\t", "$", i[4])

    print("-----------------------------------------------------------------------------------------------")
    print(f"Total Amount is: ${totalp}")
    print("=" * 95)
    print("\n")

def sell_recepit_txtFile(sell_name, sell_num, laptop_sold):
    totalp = 0 
    for i in laptop_sold:
        totalp += int(i[4])
    current_time = datetime.now()
    with open(str(sell_name)+ "_Recepit" + ".txt","w")as file:
        file.write('\n')
        file.write("=" * 95 + "\n")
        file.write("\t \t \t \t \t The Receipt:  \n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\t \t \t   Address: Kathmandu   Contact: 9823581391")
        file.write("=" * 95 +"\n")
        file.write("\t \t \t \t \t The Details are: \n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\tRecepit to the Customer: " + str(sell_name)+"\n")
        file.write("Contact Number: " + str(sell_num)+"\n")
        file.write("Date and Time of purchase: " + str(current_time)+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("Laptop name \t Laptop Brand \t Total Quantity \t Unit Price \t Total Price\n")
        for i in laptop_sold:
            file.write(str(i[0]) +"\t"+ str(i[1])+"\t\t" + str(i[2])+"\t\t\t"+"$"+ str(i[3]) + "\t\t"+"$"+ str(i[4])+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("Total Amount is: $"+str(totalp)+"\n")
        file.write("=" * 95 +"\n")



def sell_recepit_SP(sell_name, sell_num, laptop_sold):
    totalp = 0
    shipping_p = 200
    current_time = datetime.now()
    for i in laptop_sold:
        totalp += int(i[4])
    grand_total = (totalp + shipping_p)
    print('\n')
    print("=" * 95)
    print("\t \t \t \t \t The Receipt:  ")
    print("-----------------------------------------------------------------------------------------------")
    print("\t \t \t   Address: Kathmandu   Contact: 9823581391")
    print("=" * 95)
    print("\t \t \t \t \t The Details are: ")
    print("-----------------------------------------------------------------------------------------------\n")
    print("\t\t\t\tRecepit to the Customer: " + str(sell_name))
    print("Contact Number: " + str(sell_num))
    print("Date and Time of purchase: " + str(current_time))
    print("-----------------------------------------------------------------------------------------------")
    print("Laptop name \t Laptop Brand \t Total Quantity \t Unit Price \t Total Price")
    for i in laptop_sold:
        print(i[0], "\t", i[1],"\t\t", i[2], "\t\t\t", "$", i[3], "\t\t", "$", i[4])

    print("-----------------------------------------------------------------------------------------------")
    print(f"Total Amount is: ${totalp}")
    print("The Shipping Price is $200")
    print(f"Grand Total(with shipping)is: ${grand_total}")
    print("\t\t\t*** Shipping price is included ***")
    print("=" * 95)
    print("\n")

def sell_recepit_SP_txtFile(sell_name, sell_num, laptop_sold):
    totalp = 0 
    shipping_p = 200
    current_time = datetime.now()
    for i in laptop_sold:
        totalp += int(i[4])
    grand_total = (totalp + shipping_p)
    with open(str(sell_name)+ "_Recepit" + ".txt","w")as file:
        file.write('\n')
        file.write("=" * 95 + "\n")
        file.write("\t \t \t \t \t The Receipt:  \n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\t \t \t   Address: Kathmandu   Contact: 9823581391")
        file.write("=" * 95 +"\n")
        file.write("\t \t \t \t \t The Details are: \n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\tRecepit to the Customer: " + str(sell_name)+"\n")
        file.write("Contact Number: " + str(sell_num)+"\n")
        file.write("Date and Time of purchase: " + str(current_time)+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("Laptop name \t Laptop Brand \t Total Quantity \t Unit Price \t Total Price\n")
        for i in laptop_sold:
            file.write(str(i[0]) +"\t"+ str(i[1])+"\t\t" + str(i[2])+"\t\t\t"+"$"+ str(i[3]) + "\t\t"+"$"+ str(i[4])+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        file.write("Total Amount is: $"+str(totalp)+"\n")
        file.write("The Shipping Price is $200")
        file.write("Grand Total(with shipping)is: $"+str(grand_total)+"\n")
        file.write("\t\t\t*** Shipping price is included ***\n")
        file.write("=" * 95 +"\n")

        
