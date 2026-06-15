import urllib.request
import json
import re

unsplash_ids = []
seen = set()

headers = {'User-Agent': 'Mozilla/5.0'}

print("Fetching Unsplash photo IDs from Picsum List API...")
for page in range(1, 6):
    url = f"https://picsum.photos/v2/list?page={page}&limit=100"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            for item in data:
                unsplash_url = item.get('url')
                if unsplash_url:
                    # e.g. "https://unsplash.com/photos/yC-Yzbqy7PY"
                    photo_id = unsplash_url.strip().split('/')[-1]
                    if photo_id and photo_id not in seen:
                        seen.add(photo_id)
                        unsplash_ids.append(photo_id)
            print(f"  Page {page}: Total collected: {len(unsplash_ids)}")
    except Exception as e:
        print(f"  Error on page {page}: {e}")

print(f"\nSuccessfully collected {len(unsplash_ids)} unique Unsplash photo IDs.")

# Write to file
with open('picsum_unsplash_ids.json', 'w', encoding='utf-8') as f:
    json.dump(unsplash_ids, f, indent=4)
print("Saved to picsum_unsplash_ids.json")
