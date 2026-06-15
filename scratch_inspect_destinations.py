from myapp.destinations_data import DESTINATIONS

print(f"Total destinations: {len(DESTINATIONS)}")
for key in sorted(DESTINATIONS.keys()):
    data = DESTINATIONS[key]
    attractions = data.get('attractions', [])
    print(f"- {key} ({data.get('name')}):")
    for att in attractions:
        print(f"  * {att.get('name')}: {att.get('image')} | {att.get('description')}")
