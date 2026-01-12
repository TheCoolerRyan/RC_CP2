#RC 1st, List type notes

name = ["Alex", "Katie", "Andrew", "Tia"]

print(name[3])
name[-2] = "DOW"

print(name)

#Tupple
fruit = ("apple","orange","peach","kiwi","raspberry")
home = (0,0)
x,y = home
#fruit[3] = "pineapple"
print(x)

#set
colors = {"Orange", "Purple","Green","Blue","Yellow","Red"}
colors.add("Pink")
colors.remove("Purple")
for i in colors:
    if i == "Orange":
        i = "Burgendy"
    print(i)

