import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from myapp.destinations_data import states_metadata
from myapp.real_destinations_metadata import STATE_DETAILS, CITY_DETAILS

theme_to_ids = {}

# We know the theme of each state/city from states_metadata
for key, data in states_metadata.items():
    theme = data['theme']
    if theme not in theme_to_ids:
        theme_to_ids[theme] = set()
        
    # Check state details
    if key in STATE_DETAILS:
        sd = STATE_DETAILS[key]
        if 'image' in sd:
            theme_to_ids[theme].add(sd['image'].split('?')[0].split('/')[-1])
        if 'about_image' in sd:
            theme_to_ids[theme].add(sd['about_image'].split('?')[0].split('/')[-1])
            
    # Check city details
    for city_key in data.get('cities_list', []):
        if city_key in CITY_DETAILS:
            cd = CITY_DETAILS[city_key]
            if 'image' in cd:
                theme_to_ids[theme].add(cd['image'].split('?')[0].split('/')[-1])
            if 'about_image' in cd:
                theme_to_ids[theme].add(cd['about_image'].split('?')[0].split('/')[-1])

print("Existing themed photo IDs:")
for theme, ids in theme_to_ids.items():
    print(f"  {theme}: {len(ids)} unique IDs")
    print(f"    {sorted(list(ids))[:5]}")
