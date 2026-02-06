def paser():
    #Use try and except
    try:
        with open("Individual_projects/movies_list.csv", mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            rows = {}
            for line in content:
                rows[line[0]] =  [line[1],line[2],line[3],int(line[4]),list[line[5]]]

    except:
        print("We can't find the csv file")

    else:
        for key,value in rows.items():
            print(f"{key}: {value}")
