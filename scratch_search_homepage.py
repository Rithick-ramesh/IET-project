import re

with open('templates/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of href linking to /destination/ or destination details
links = re.findall(r'href="[^"]*destination[^"]*"|href=\'[^\']*destination[^\']*\'', content)
print("Links with destination:")
for l in links[:20]:
    print(l)

# Let's also search for how cards are structured
cards = re.findall(r'<div class="card[^"]*".*?</div>', content, re.DOTALL)
print(f"\nFound {len(cards)} cards on homepage.")
