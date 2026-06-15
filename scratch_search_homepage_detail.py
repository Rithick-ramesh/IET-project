with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for "bengaluru" (case-insensitive) in homepage.html
import re
bengaluru_matches = [m.start() for m in re.finditer(r'bengaluru', content, re.IGNORECASE)]
print(f"Found 'bengaluru' {len(bengaluru_matches)} times.")
for pos in bengaluru_matches:
    start = max(0, pos - 150)
    end = min(len(content), pos + 150)
    print(f"--- MATCH AT {pos} ---")
    print(content[start:end])
    print("-----------------------")

# Let's also print any onclick handlers or script navigations
navs = re.findall(r'window\.location\.[^;]*|location\.href\s*=[^;]*', content)
print("\nJS Navigations:")
for n in navs:
    print(n)
