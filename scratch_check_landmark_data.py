from myapp.destinations_data import DESTINATIONS

keys = ['gaya', 'goa', 'mumbai', 'diu']
for key in keys:
    if key in DESTINATIONS:
        data = DESTINATIONS[key]
        print(f"=== KEY: {key} ===")
        print(f"Name: {data.get('name')}")
        print(f"Type: {data.get('type')}")
        print(f"State: {data.get('state')}")
        print(f"Tag: {data.get('tag')}")
        print(f"Description: {data.get('description')}")
        print(f"About More: {data.get('about_more')}")
        print(f"Attractions:")
        for att in data.get('attractions', []):
            print(f"  * {att.get('name')}: {att.get('desc') or att.get('description')}")
        print(f"Hotels Keys: {list(data.get('hotels', {}).keys())}")
        print("-" * 40)
    else:
        print(f"KEY: {key} NOT FOUND IN DESTINATIONS")
