with open('euro_cup_matches.csv') as file:
    #Read the headings
    headings = file.readline().strip()
    columns = headings.split()
    print(columns)