import urllib.request
import re
import urllib.parse

def scrape_yahoo_unsplash(query, count=20):
    escaped_query = urllib.parse.quote(f"{query} unsplash")
    url = f"https://images.search.yahoo.com/search/images?p={escaped_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read().decode('utf-8')
            # Yahoo search results contain URLs inside the source code
            # e.g., "https://images.unsplash.com/photo-1596422846543-75c6fc1f4751..."
            matches = re.findall(r'photo-[a-zA-Z0-9\-]+', html)
            seen = set()
            unique_ids = []
            for m in matches:
                if len(m) > 12 and m not in seen:
                    seen.add(m)
                    unique_ids.append(m)
            print(f"Yahoo '{query}': Found {len(unique_ids)} IDs. First few: {unique_ids[:5]}")
            return unique_ids[:count]
    except Exception as e:
        print(f"Error scraping Yahoo for '{query}': {e}")
        return []

scrape_yahoo_unsplash("indian temple", 5)
scrape_yahoo_unsplash("goa beach", 5)
