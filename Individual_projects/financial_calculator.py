#RC 1st, Finacial Calculator

#Creat sales function
def sales():
    #Put in a while loop ->
    while True:
        #Ask Them the amount it costs, <-
        cost = input("Tell me the original cost of the item (Before the sale):").strip()
        #Stupid proff
        number = cost.isdigit()
        if number == True and int(cost) >= 0:
            cost = int(cost)
            break
        else:
            print("That is not a valid number for the cost.")
    #Then do the same for the percent that is taken of
    while True:
        sale = input("Tell me the discount (Just the number! No signs,just the number, for example if its 15% of, put 15):").strip()
        #stupid proff
        number = sale.isdigit()
        if number == True and int(sale) >= 0:
            sale = int(sale)
            break
        else:
            print("That is not a valid number for the sale.")
    #Create a calculation inner function
    def calculation():
        percent = sale/100
        #Times the cost by the after a decimal point (15% iis 0.15)
        #Subtract that to the cost and put it into a variable
        price = cost - (cost*percent)
        #Return Finial variable
        return price
    print(f"The end cost is: {calculation():.2f}")
    #Print of variable.
#Creat goal function
def goal():
    #Ask how much they are trying to save up to
    while True:
        goal = input("How much money do you want to save up to:").strip()
        #Stupid proff it
        if goal.isdigit() == True and int(goal) > 0:
            goal = int(goal)
            break
        else:
            print("That is not a valid option")
    #Figure out how much there putting in weekly
    while True:
        deposit = input("How much money do you deposit weekly:").strip()
        #Stupid proff it
        if deposit.isdigit() == True and int(deposit) > 0:
            deposit = int(deposit)
            break
        else:
            print("That is not a valid option")
    #Calculate amount of weeks
    weeks = goal/deposit
    #Tell them how many weeks it will take
    print(f"It will take {weeks:.2f} weeks!")
#Create compound interest function
def compound():
    #Ask how much they are depositing
    while True:
        bank = input("How much money do you want to put into the bank:").strip()
        #Stupid proff it
        if bank.isdigit() == True and int(bank) > 0:
            bank = int(bank)
            break
        else:
            print("That is not a valid option")
    #Ask how long they are going to wait
    while True:
        time = input("How long are you going to wait:").strip()
        #Stupid proff it
        if time.isdigit() == True and int(time) > 0:
            time = int(time)
            break
        else:
            print("That is not a valid option")
    #Ask how much they are trying to save up to
    while True:
        rate = input("What is the interest rates?:").strip()
        #Stupid proff it
        if rate.isdigit() == True and int(rate) > 0:
            rate = int(rate)
            break
        else:
            print("That is not a valid option")
def proff(variable):
    #Ask how much they are trying to save up to
    while True:
        variable = input("How much money do you want to save up to:").strip()
        #Stupid proff it
        if variable.isdigit() == True and int(variable) > 0:
            variable = int(variable)
            break
        else:
            print("That is not a valid option")
#Use proof to simplfy code