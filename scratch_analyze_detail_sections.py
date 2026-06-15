with open('templates/destination_detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
section_headers = []
for i, line in enumerate(lines, 1):
    if '<section' in line or 'class=\"section' in line or 'class=\"hotels' in line or 'class=\"alerts' in line or 'class=\"about' in line:
        section_headers.append(f"Line {i}: {line.strip()}")

print("=== Sections in destination_detail.html ===")
for sh in section_headers:
    print(sh)
