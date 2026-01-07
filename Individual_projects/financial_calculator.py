#RC 1st, Finacial Calculator

#Creat sales function
def sales():
    #Put in a while loop ->
    while True:
        #Ask Them the amount it costs, <-
        cost = input("Tell me the original cost of the item (Before the sale).").strip()
        number = cost.isdigit()
        if number == True and int(cost) >= 0:
            break
        else:
            print("That is not a valid number for the cost.")
    while True:
        sale = input("Tell me the discount (Just the number! No signs,just the number, for example if its 15% of, put 15).").strip()
        number = cost.isdigit()
        if number == True and int(sale) >= 0:
            break
        else:
            print("That is not a valid number for the sale.")
    #Then do the same for the percent that is taken of
    #Create a calculation inner function
        #Times the cost by the after a decimal point (15% iis 0.15)
        #Subtract that to the cost and put it into a variable
        #Return Finial variable
    #Print of variable.
sales()