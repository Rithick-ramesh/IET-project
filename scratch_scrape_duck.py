import urllib.request
import json
import re
import urllib.parse
import time

def get_ddg_unsplash_ids(query, count=40):
    # DuckDuckGo image search JSON endpoint
    escaped_query = urllib.parse.quote(f"{query} site:unsplash.com/photos/")
    # DDG HTML search works well for scraping
    url = f"https://html.duckduckgo.com/html/?q={escaped_query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            html = response.read().decode('utf-8')
            # Look for links containing unsplash.com/photos/xxxxx
            matches = re.findall(r'unsplash\.com/photos/([a-zA-Z0-9\-]+)', html)
            seen = set()
            unique_ids = []
            for m in matches:
                # Unsplash photo IDs are usually 11 characters
                if 5 <= len(m) <= 15 and m not in seen and m not in ['download', 'license', 'privacy', 'terms']:
                    seen.add(m)
                    unique_ids.append(m)
            print(f"DDG '{query}': Found {len(unique_ids)} photo IDs.")
            return unique_ids[:count]
    except Exception as e:
        print(f"Error for '{query}': {e}")
        return []

ids = get_ddg_unsplash_ids("temple", 10)
print(ids)
