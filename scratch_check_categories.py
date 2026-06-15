import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from myapp.destinations_data import states_metadata

theme_counts = {}
for key, data in states_metadata.items():
    theme = data['theme']
    if theme not in theme_counts:
        theme_counts[theme] = {'states': 0, 'cities': 0}
    theme_counts[theme]['states'] += 1
    theme_counts[theme]['cities'] += len(data.get('cities_list', []))

print("Theme distribution:")
total_cities = 0
total_states = 0
for theme, counts in theme_counts.items():
    print(f"  {theme}: {counts['states']} states, {counts['cities']} cities")
    total_states += counts['states']
    total_cities += counts['cities']
print(f"Total: {total_states} states/UTs, {total_cities} cities")
