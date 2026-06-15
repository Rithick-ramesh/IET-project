import urllib.request
import re
import json

urls = [
    "https://raw.githubusercontent.com/RishiRanjan-01/Booking.com-Clone/main/db.json"
]

unsplash_pattern = re.compile(r'photo-[a-zA-Z0-9\-]+')
all_ids = set()

headers = {'User-Agent': 'Mozilla/5.0'}

for url in urls:
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            content = response.read().decode('utf-8')
            matches = unsplash_pattern.findall(content)
            print(f"  Found {len(matches)} matches.")
            for m in matches:
                if len(m) > 12:
                    all_ids.add(m)
    except Exception as e:
        print(f"  Error: {e}")

print(f"\nTotal unique Unsplash photo IDs found: {len(all_ids)}")
if all_ids:
    print("First 20 IDs:")
    for i in list(all_ids)[:20]:
        print(f"  '{i}',")
        
with open('booking_unsplash_ids.json', 'w', encoding='utf-8') as f:
    json.dump(list(all_ids), f, indent=4)
print("Saved to booking_unsplash_ids.json")
