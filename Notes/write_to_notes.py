#RC 1st, Write to notes

"""with open("Notes/writing.txt", "r+") as file:
    content = file.read()
    content += "\nI wrote on my file"
    file.write(content)



#If the file dosen't exist, it creates one
with open("Notes/writing.txt", "a") as file:
    file.write("\nThis is more on my file!")

print("Code end")"""


import csv
"""
#Setup for reading/writing
with open("Notes/sample.csv", 'w', newline= '') as csvfile:
    fieldnames = ['username','color']
    writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
    #writer.writeheader()
    writer.writerow({'username':'name', 'color':'orange'})
    writer.writerow({'username':'joe', 'color':'red'})
    writer.writerow({'username':'manny', 'color':'pink'})

print("Code is done")"""

with open("Notes/sample.csv", 'r+', newline= '') as csvfile:
    fieldnames = ['username','color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}: {line[0]}, favorite color: {line[1]}.")
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    #writer.writeheader()
    writer.writerow({'username':'Ryan', 'color':'orange'})
    writer.writerow({'username':'Joe', 'color':'red'})
    writer.writerow({'username':'Manny', 'color':'pink'})

print("Code is done")