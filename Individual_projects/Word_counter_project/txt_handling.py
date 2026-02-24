#RC 1st, This is were the txt will be cleaned up and ready to go

#import time_managment file
from time_managment import *

#create a function that will update the text file, takes in the sentance that they created
def save(file_path, sentance):
    #Create a for loop that will go through there sentence's and for every space, and +1 to the count
    counts = sentance.count(' ') + 1
    good_time = read_time()
    #Create the code that will write to the file, overwriting all earlier code
    #While its still open, also add the time
    with open(file_path, "w") as file:
        file.write(sentance)
        together = "(" + "Last updated: " + good_time + ")"
        file.write(together)

    return (f"Document is updated. Word count {counts}")





#Create a function to read the file 
def view(file_path):
    print("Document content:")
    #use with open to read the file and then add it to a string
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("We could not find the file...")

    #Return the full txt as a sentance
 





#Create a function to add stuff to the document
def add():
    #Explain to them what they need to do and the exit requirment
    print("Enter new content (press ENTER TWICE to finish):")
    #Set sentance to empty string
    sentance = ""
    #Put them into a while loop
    while True:
        #Ask them for the input they would like to add to a sentance
        content = input().strip()
        #Append that to the sentance variable
        sentance += (content + " ")
        #If the input = an empty string then break
        if content == "":
            break
        #Else keep the loop going
        else:
            pass
    return sentance

