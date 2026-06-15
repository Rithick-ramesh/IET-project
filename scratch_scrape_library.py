import urllib.request
import re
import json
import time

categories = {
    'temple': ["indian temple", "ancient temple india", "spiritual india", "mandir", "hindu temple", "south indian temple"],
    'mountain': ["himalayas", "snow mountain", "scenic mountains", "hill station india", "mountain valley", "kashmir valley"],
    'beach': ["goa beach", "kerala beach", "andaman beach", "tropical beach", "ocean coast", "beach sunset"],
    'palace': ["indian palace", "rajasthan fort", "heritage building india", "royal palace", "ancient fort", "historical monument india"],
    'nature': ["national park india", "wildlife india", "waterfall", "scenic lake", "kerala backwaters", "green forest"],
    'city': ["indian city street", "mumbai traffic", "delhi street", "city skyline", "modern architecture india", "bangalore city"],
    'hotel': ["luxury hotel room", "hotel pool", "resort stay", "cozy bed", "hotel bedroom", "luxury resort"]
}

def scrape_unsplash_ids(query):
    url = f"https://unsplash.com/s/photos/{query.replace(' ', '-')}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            matches = re.findall(r'photo-[a-zA-Z0-9\-]+', html)
            seen = set()
            unique_ids = []
            for m in matches:
                if len(m) > 12 and m not in seen:
                    seen.add(m)
                    unique_ids.append(m)
            return unique_ids
    except Exception as e:
        print(f"Error scraping '{query}': {e}")
        return []

library = {}
all_scraped_ids = set()

for cat, queries in categories.items():
    print(f"Scraping for category: {cat}")
    library[cat] = []
    cat_seen = set()
    for q in queries:
        print(f"  Query: {q}")
        ids = scrape_unsplash_ids(q)
        for val in ids:
            if val not in all_scraped_ids and val not in cat_seen:
                all_scraped_ids.add(val)
                cat_seen.add(val)
                library[cat].append(val)
        time.sleep(0.5)  # Respectful pause
    print(f"Category '{cat}' collected {len(library[cat])} unique photo IDs.")

# Write library to JSON
with open('unsplash_library.json', 'w', encoding='utf-8') as f:
    json.dump(library, f, indent=4)

print(f"\nDone! Scraped a total of {len(all_scraped_ids)} unique photo IDs across all categories.")
