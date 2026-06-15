import sys
import json

sys.path.append(r"c:\Users\Rithick prabhu\OneDrive\Desktop\tourism backgroung\myproject")

from myapp.destinations_data import DESTINATIONS

original_keys = ['agra', 'jaipur', 'kerala', 'goa', 'kashmir', 'varanasi']
extracted = {}
for k in original_keys:
    if k in DESTINATIONS:
        extracted[k] = DESTINATIONS[k]

with open('custom_destinations.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, indent=4)

print("Extracted successfully!")
