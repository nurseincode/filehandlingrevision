import json

matches = [
    {
        'Team A': 'New Zealand',
        'Team B': 'Australia',
        'Score A': 1,
        'Score B': 1,
        'Date': '2026-11-20'
    },
    {
        'Team A': 'Uganda',
        'Team B': 'Kenya',
        'Score A': 1,
        'Score B': 1,
        'Date': '2026-11-21'
    }

]

with open('matches.json', 'w') as file:
    (json.dump(matches, file, indent=4))