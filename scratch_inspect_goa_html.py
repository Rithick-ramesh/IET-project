with open('templates/Goa.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Find place-card blocks
matches = re.findall(r'<div class="place-card">.*?</div>\s*</div>', content, re.DOTALL)
print(f"Found {len(matches)} place-cards in Goa.html:")
for i, m in enumerate(matches, 1):
    print(f"--- Card {i} ---")
    print(m.strip())
