try:
        with open("Individual_projects/books.csv",mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)
            collection = []
            for line in content:
                collection.append({line[0]: [line[1],line[2],line[3]]})