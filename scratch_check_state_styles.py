import os

files = ['Goa.html', 'agra.html', 'jaipur.html', 'kashmir.html', 'kerala.html', 'varanasi.html']
for f in files:
    path = os.path.join('templates', f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        has_hotel_card = '.hotel-card' in content
        has_hotels_section = '.hotels-section' in content
        print(f'{f}: has .hotel-card = {has_hotel_card}, has .hotels-section = {has_hotels_section}')
