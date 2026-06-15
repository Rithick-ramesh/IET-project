import urllib.request
import re
import urllib.parse
import time

categories = {
    'temple': ["indian temple", "ancient temple india", "spiritual india", "mandir", "hindu temple", "south indian temple"],
    'mountain': ["himalayas", "snow mountain", "scenic mountains", "hill station india", "mountain valley", "kashmir valley"],
    'beach': ["goa beach", "kerala beach", "andaman beach", "tropical beach", "ocean coast", "beach sunset"],
    'palace': ["indian palace", "rajasthan fort", "heritage building india", "royal palace", "ancient fort", "historical monument india"],
    'nature': ["national park india", "wildlife india", "waterfall", "scenic lake", "kerala backwaters", "green forest"],
    'city': ["indian city street", "mumbai traffic", "delhi street", "city skyline", "modern architecture india", "bangalore city"]
}

def scrape_bing_unsplash(query, count=30):
    escaped_query = urllib.parse.quote(f"{query} unsplash")
    url = f"https://www.bing.com/images/search?q={escaped_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read().decode('utf-8')
            # Look for photo-xxxxxxxxxxxxx
            matches = re.findall(r'photo-[a-zA-Z0-9\-]+', html)
            seen = set()
            unique_ids = []
            for m in matches:
                # Unsplash photo IDs have length > 12 and contain only alphanumeric and dash
                if len(m) > 12 and m not in seen:
                    seen.add(m)
                    unique_ids.append(m)
            print(f"Bing '{query}': Found {len(unique_ids)} IDs.")
            return unique_ids[:count]
    except Exception as e:
        print(f"Error scraping Bing for '{query}': {e}")
        return []

library = {}
all_scraped_ids = set()

for cat, queries in categories.items():
    print(f"Scraping for category: {cat}")
    library[cat] = []
    cat_seen = set()
    for q in queries[:3]: # Limit to 3 queries per category to be fast
        ids = scrape_bing_unsplash(q, 20)
        for val in ids:
            if val not in all_scraped_ids and val not in cat_seen:
                all_scraped_ids.add(val)
                cat_seen.add(val)
                library[cat].append(val)
        time.sleep(0.5)

import json
with open('bing_unsplash_library.json', 'w', encoding='utf-8') as f:
    json.dump(library, f, indent=4)

print(f"\nDone! Scraped {len(all_scraped_ids)} unique photo IDs from Bing.")
