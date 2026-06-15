import os
import re

files = ['templates/destination.html', 'templates/destination_detail.html']
for filepath in files:
    if os.path.exists(filepath):
        print(f"=== {filepath} ===")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Find occurrences of class names containing 'card'
        matches = re.findall(r'<div[^>]*class=["\'][^"\']*card[^"\']*["\'][^>]*>', content)
        for match in matches[:15]:  # print first 15 matches
            print(f"  {match.strip()}")
        # Check if there are onclick handlers or specific links
        print("  Checking for a href in cards:")
        # Look at lines near card declarations
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'class=' in line and 'card' in line:
                print(f"    Line {i+1}: {line.strip()}")
                # print next 3 lines
                for j in range(1, 4):
                    if i+j < len(lines):
                        print(f"      + {lines[i+j].strip()}")
                print("-" * 20)
