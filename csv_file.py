import csv

total_goals = 0
with open('euro_cup_matches.csv') as file:
    content = csv.DictReader(file)
    for row in content:
        total_goals += int(row['Score A']) + int(row['Score B'])
print(f'Total goals in the tournament so far: {total_goals}')

    #Read the headings
    # headings = file.readline().strip()
    # columns = headings.split(',')
    # print(columns)

with open('new_matches.csv', 'w') as file:
    writer = csv.DictWriter(file, ['Team A', 'Team B', 'Score A', 'Score B', 'Date'])
    writer.writeheader()