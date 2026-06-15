import os

files = ['Goa.html', 'agra.html', 'jaipur.html', 'kashmir.html', 'kerala.html', 'varanasi.html']
for f in files:
    path = os.path.join('templates', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        lines = content.split('\n')
        hotel_lines = [f"Line {i+1}: {line.strip()}" for i, line in enumerate(lines) if 'hotel' in line.lower()]
        print(f"=== {f} ===")
        for hl in hotel_lines[:5]:
            print(f"  {hl}")
        print(f"Total occurrences: {len(hotel_lines)}")
