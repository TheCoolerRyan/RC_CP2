#RC 1st, Finacial Calculator

#Creat sales function
def sales():
    #Put in a while loop ->
    while True:
        #Ask Them the amount it costs, <-
        cost = input("Tell me the original cost of the item (Before the sale):").strip()
        #Stupid proff
        test, cost = proff(cost)
        if test == True:
            break
    #Then do the same for the percent that is taken of
    while True:
        sale = input("Tell me the discount (Just the number! No signs,just the number, for example if its 15% of, put 15):").strip()
        #stupid proff
        test,sale = proff(sale)
        if test == True:
            break
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
        test,goal = proff(goal)
        if test == True:
            break
    #Figure out how much there putting in weekly
    while True:
        deposit = input("How much money do you deposit weekly:").strip()
        #Stupid proff it
        test,deposit = proff(deposit)
        if test == True:
            break
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
        test,bank = proff(bank)
        if test == True:
            break
    #Ask how long they are going to wait
    while True:
        time = input("How many months are you going to wait:").strip()
        #Stupid proff it
        test,time = proff(time)
        if test == True:
            num = time
            break
    #Ask how much they are trying to save up to
    while True:
        rate = input("What is the interest rates? (if its 1%, put 1):").strip()
        #Stupid proff it
        test,rate = proff(rate)
        if test == True:
            percent = rate/100
            break
    #create for loop that allows for the loop to calculate
    for i in range(num):
        bank += bank*percent
    print(f"After {time} months, you have ${bank:.2f}!")
#Create the Budget calculator
def budget():
    #Ask them how much money they will have
    while True:
        print("Please make sure all percents add up to 100")
        while True:
            #Ask for money
            money = input("How much money do you have?:").strip()
            #Stupid proof
            test,money = proff(money)
            if test == True:
                break
        #Ask them for how much they want to put into car
        while True:
            #Ask via an input
            car = input("What percent of your money do you want to put into your car savings? (If its 10%, just put 10):").strip()
            #stupdid proff
            test,car = proff(car)
            if test == True:
                cars = car/100
                break
        #Ask them for how much they want to put into grocieris
        while True:
            #Ask via an input
            grocieries = input("What percent of your money do you want to put into your grocieries savings? (If its 10%, just put 10):").strip()
            #stupdid proff
            test,grocieries = proff(grocieries)
            if test == True:
                grocieriess = grocieries/100
                break
        #Ask them for how much they want to put into housing
        while True:
            #Ask via an input
            house = input("What percent of your money do you want to put into your house savings? (If its 10%, just put 10):").strip()
            #stupdid proff
            test,house = proff(house)
            if test == True:
                houses = house/100
                break
        #Ask them for how much they want to put into emergencies
        while True:
            #Ask via an input
            emergincies = input("What percent of your money do you want to put into your emergincies savings? (If its 10%, just put 10):").strip()
            #stupdid proff
            test,emergincies = proff(emergincies)
            if test == True:
                emerginciess = emergincies/100
                break
        #Ask them for how much they want to put into fun
        while True:
            #Ask via an input
            fun = input("What percent of your money do you want to put into your free spending? (If its 10%, just put 10):").strip()
            #stupdid proff
            test,fun = proff(fun)
            if test == True:
                funs = fun/100
                break
        #Ask them for how much they want to put into savings
        while True:
            #Ask via an input
            savings = input("What percent of your money do you want to put into your savings? (If its 10%, just put 10):").strip()
            #stupdid proff
            test,savings = proff(savings)
            if test == True:
                savingss = savings/100
                break
        #Create calculations for everyone of the percents
    #Check to make sure that percents add up to 100
        if (savings) + (fun) + (emergincies) + (house) + (grocieries) + (car) == 100:
            break
        else:
            print("That doesn't add up to 100 percent!")
    save = money*savingss
    fu= money*funs
    emergin = money*emerginciess
    home = money*houses
    food = money*grocieriess
    van = money*cars
    print(f"Savings is ${save:.2f}\nFree time is ${fu:.2f}\nEmergincies is ${emergin:.2f}\nHouse is ${home:.2f}\nGrocieries is ${food:.2f}\nCar is ${van:.2f}")
#Create Tip function
def tip():
    print()
#create stupid proff function
def proff(variable):
    #Ask how much they are trying to save up to
        #Stupid proff it
        if variable.isdigit() == True and int(variable) > 0:
            variable = int(variable)
            return True, variable
        else:
            print("That is not a valid option")
            return False, variable




#might've fixed it, could still be messed up.
budget()
