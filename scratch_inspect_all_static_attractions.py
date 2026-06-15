import os
import re

files = ['templates/agra.html', 'templates/jaipur.html', 'templates/kashmir.html', 'templates/kerala.html', 'templates/varanasi.html']
for filepath in files:
    if os.path.exists(filepath):
        print(f"=== {filepath} ===")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = re.findall(r'<div class="place-card">.*?</div>\s*</div>', content, re.DOTALL)
        print(f"Found {len(matches)} place-cards:")
        for i, m in enumerate(matches, 1):
            # print h3 and first 100 chars of paragraph
            h3_match = re.search(r'<h3>(.*?)</h3>', m)
            p_match = re.search(r'<p>(.*?)</p>', m, re.DOTALL)
            h3 = h3_match.group(1).strip() if h3_match else "No H3"
            p = p_match.group(1).strip().replace('\n', ' ') if p_match else "No P"
            print(f"  * Attraction {i}: {h3} | {p[:120]}...")
        print("-" * 55)
