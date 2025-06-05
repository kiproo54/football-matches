import json
import os

# Convert team names to match logo file format
def slugify(name):
    return (
        name.strip().lower()
        .replace(' ', '-')      # Use hyphens for filenames
        .replace('&', 'and')
        .replace('.', '')
        .replace('/', '-')
    )

# Load the JSON data
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add logo paths to each match
for category, matches in data['categories'].items():
    for match in matches:
        teams = match.get('teams', '')
        split = teams.lower().split(' vs ')
        if len(split) != 2:
            continue
        home, away = [slugify(team) for team in split]
        match['home_logo'] = f'logos/{home}.png'
        match['away_logo'] = f'logos/{away}.png'

# Save the updated data
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("✅ Logos linked successfully.")
