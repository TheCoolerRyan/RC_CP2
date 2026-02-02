#RC 1st, Reading notes

import csv

"""while True:
    try:
        with open("Notes/reading.txt", "r") as file:
            for line in file:
                print(f"Hello {line.strip()}")
            
    except:
        print("That file can't be found")


    else:
        print("Code ends")
        break"""


try:
    with open("Notes\sample.csv", mode = "r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0]: line[0], headers[1]: line[1]})

except:
    print("We can't find the csv")
else:
    for line in rows:
        print(line)
    