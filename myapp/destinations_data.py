# Dynamic Destinations Compiler for Indian States and Cities
from .custom_destinations_data import CUSTOM_DESTINATIONS
from .real_attractions_data import REAL_ATTRACTIONS
from .real_destinations_metadata import STATE_DETAILS, CITY_DETAILS

# 1. CURATED REAL UNIQUE UNSPLASH IMAGES FOR ALL STATES AND CITIES
LOCATION_IMAGES = {
    # States
    'andhra pradesh': 'Image Not Available',
    'arunachal pradesh': 'Image Not Available',
    'assam': 'Image Not Available',
    'bihar': 'Image Not Available',
    'chhattisgarh': 'Image Not Available',
    'goa': 'Image Not Available',
    'gujarat': 'Image Not Available',
    'haryana': 'Image Not Available',
    'himachal pradesh': 'Image Not Available',
    'jammu & kashmir': 'Image Not Available',
    'jharkhand': 'Image Not Available',
    'karnataka': 'Image Not Available',
    'kerala': 'Image Not Available',
    'madhya pradesh': 'Image Not Available',
    'maharashtra': 'Image Not Available',
    'manipur': 'Image Not Available',
    'meghalaya': 'Image Not Available',
    'mizoram': 'Image Not Available',
    'nagaland': 'Image Not Available',
    'odisha': 'Image Not Available',
    'punjab': 'Image Not Available',
    'rajasthan': 'Image Not Available',
    'sikkim': 'Image Not Available',
    'tamil nadu': 'Image Not Available',
    'telangana': 'Image Not Available',
    'tripura': 'Image Not Available',
    'uttar pradesh': 'Image Not Available',
    'uttarakhand': 'Image Not Available',
    'west bengal': 'Image Not Available',
    'andaman & nicobar islands': 'Image Not Available',
    'chandigarh': 'Image Not Available',
    'dadra & nagar haveli and daman & diu': 'Image Not Available',
    'delhi': 'Image Not Available',
    'lakshadweep': 'Image Not Available',
    'puducherry': 'Image Not Available',

    # Cities
    'visakhapatnam': 'Image Not Available',
    'tirupati': 'Image Not Available',
    'itanagar': 'Image Not Available',
    'tawang': 'Image Not Available',
    'ziro': 'Image Not Available',
    'guwahati': 'Image Not Available',
    'patna': 'Image Not Available',
    'gaya': 'Image Not Available',
    'raipur': 'Image Not Available',
    'panaji': 'Image Not Available',
    'calangute': 'Image Not Available',
    'anjuna': 'Image Not Available',
    'vagator': 'Image Not Available',
    'colva': 'Image Not Available',
    'palolem': 'Image Not Available',
    'ahmedabad': 'Image Not Available',
    'gandhinagar': 'Image Not Available',
    'bhuj': 'Image Not Available',
    'patan': 'Image Not Available',
    'gurugram': 'Image Not Available',
    'shimla': 'Image Not Available',
    'manali': 'Image Not Available',
    'dharamshala': 'Image Not Available',
    'srinagar': 'Image Not Available',
    'jammu': 'Image Not Available',
    'gulmarg': 'Image Not Available',
    'pahalgam': 'Image Not Available',
    'sonamarg': 'Image Not Available',
    'ranchi': 'Image Not Available',
    'bengaluru': 'Image Not Available',
    'mysore': 'Image Not Available',
    'hampi': 'Image Not Available',
    'gokarna': 'Image Not Available',
    'kochi': 'Image Not Available',
    'munnar': 'Image Not Available',
    'alappuzha': 'Image Not Available',
    'thiruvananthapuram': 'Image Not Available',
    'kovalam': 'Image Not Available',
    'leh': 'Image Not Available',
    'bhopal': 'Image Not Available',
    'indore': 'Image Not Available',
    'gwalior': 'Image Not Available',
    'khajuraho': 'Image Not Available',
    'ujjain': 'Image Not Available',
    'mumbai': 'Image Not Available',
    'nagpur': 'Image Not Available',
    'aurangabad': 'Image Not Available',
    'lonavala': 'Image Not Available',
    'imphal': 'Image Not Available',
    'shillong': 'Image Not Available',
    'cherrapunji': 'Image Not Available',
    'aizawl': 'Image Not Available',
    'kohima': 'Image Not Available',
    'bhubaneswar': 'Image Not Available',
    'puri': 'Image Not Available',
    'konark': 'Image Not Available',
    'amritsar': 'Image Not Available',
    'ludhiana': 'Image Not Available',
    'jaipur': 'Image Not Available',
    'udaipur': 'Image Not Available',
    'jodhpur': 'Image Not Available',
    'jaisalmer': 'Image Not Available',
    'pushkar': 'Image Not Available',
    'gangtok': 'Image Not Available',
    'pelling': 'Image Not Available',
    'chennai': 'Image Not Available',
    'coimbatore': 'Image Not Available',
    'rameswaram': 'Image Not Available',
    'kanyakumari': 'Image Not Available',
    'madurai': 'Image Not Available',
    'hyderabad': 'Image Not Available',
    'warangal': 'Image Not Available',
    'agartala': 'Image Not Available',
    'lucknow': 'Image Not Available',
    'kanpur': 'Image Not Available',
    'agra': 'Image Not Available',
    'varanasi': 'Image Not Available',
    'prayagraj': 'Image Not Available',
    'ayodhya': 'Image Not Available',
    'dehradun': 'Image Not Available',
    'haridwar': 'Image Not Available',
    'rishikesh': 'Image Not Available',
    'nainital': 'Image Not Available',
    'mussoorie': 'Image Not Available',
    'kolkata': 'Image Not Available',
    'siliguri': 'Image Not Available',
    'digha': 'Image Not Available',
    'port blair': 'Image Not Available',
    'daman': 'Image Not Available',
    'diu': 'Image Not Available',
    'delhi': 'Image Not Available',
    'kavaratti': 'Image Not Available',
    'puducherry': 'Image Not Available'
}

# Dynamic image helper using curated list of photo URLs or safe fallback pools
def get_location_photo(location_key, category='travel', index=0):
    key_lower = location_key.lower().strip()
    if key_lower in LOCATION_IMAGES:
        return LOCATION_IMAGES[key_lower]
        
    nature_pool = [
        'Image Not Available',
        'Image Not Available',
        'Image Not Available',
        'Image Not Available'
    ]
    temple_pool = [
        'Image Not Available',
        'Image Not Available',
        'Image Not Available'
    ]
    city_pool = [
        'Image Not Available',
        'Image Not Available',
        'Image Not Available'
    ]
    hotel_pool = [
        'Image Not Available',
        'Image Not Available',
        'Image Not Available'
    ]
    
    if 'temple' in category or 'spiritual' in category:
        return temple_pool[index % len(temple_pool)]
    elif 'nature' in category or 'scenic' in category or 'beach' in category:
        return nature_pool[index % len(nature_pool)]
    elif 'hotel' in category or 'resort' in category or 'stay' in category:
        return hotel_pool[index % len(hotel_pool)]
    else:
        return city_pool[index % len(city_pool)]

# Deterministic generator for real searchable hotel brands combined with city name
def get_hotel_name(city_name, category, index):
    luxury_brands = [
        "Taj Resort & Spa", "The Leela Palace", "The Oberoi", 
        "ITC Grand", "JW Marriott", "Hyatt Regency", 
        "Radisson Blu Plaza", "Trident Hotel"
    ]
    comfort_brands = [
        "Lemon Tree Premier", "Fortune Park", "Ginger Hotel", 
        "Sarovar Portico", "Holiday Inn", "Fairfield by Marriott", 
        "Keys Select", "Red Fox Hotel"
    ]
    budget_brands = [
        "Zostel", "OYO Rooms", "Youth Hostel", 
        "Homestay Inn", "Backpackers Lodge", "Tourist Guest House",
        "Residency Lodge", "Standard Hotel"
    ]
    
    if category == 'luxury':
        brand = luxury_brands[index % len(luxury_brands)]
        return f"{brand} {city_name}"
    elif category == 'comfort':
        brand = comfort_brands[index % len(comfort_brands)]
        return f"{brand} {city_name}"
    else:
        brand = budget_brands[index % len(budget_brands)]
        return f"{brand} {city_name}"

# Themed description generation to prevent generic f-string templates
def get_location_description(city_name, state_name, theme):
    descriptions = {
        'beaches': f"{city_name} is a beautiful coastal destination in {state_name}, celebrated for its sandy beaches, sea breeze, and exciting water sports.",
        'mountains': f"{city_name} is a picturesque hill station in the mountains of {state_name}, famous for scenic views, pine valleys, and refreshing weather.",
        'temples': f"{city_name} is a historic spiritual town in {state_name}, featuring ancient temples, rich local devotion, and sacred heritage sites.",
        'palaces': f"{city_name} is a majestic heritage city in {state_name}, renowned for its royal architecture, ancient forts, and vibrant bazaars.",
        'nature': f"{city_name} is a serene green haven in {state_name}, offering pristine nature reserves, rich biodiversity, and scenic lake trails.",
        'cities': f"{city_name} is a bustling urban center in {state_name}, blending modern attractions with local culture and gourmet dining."
    }
    return descriptions.get(theme, f"{city_name} is a famous travel destination in {state_name}, offering beautiful sights and warm local hospitality.")

def get_about_more(city_name, theme):
    details = {
        'beaches': f"Ideal for beachgoers, {city_name} features sunset views, coastal walks, and beach shacks. Visitors can enjoy local seafood and water sports like parasailing.",
        'mountains': f"Perfect for hikers and nature lovers, {city_name} offers trekking trails, waterfalls, and scenic viewpoints over mist-covered hills.",
        'temples': f"Steeped in history, {city_name} invites travelers to explore sacred stone architecture, attend local festivals, and experience peaceful traditions.",
        'palaces': f"Filled with royal history, {city_name} features heritage museums, ancient architecture, and markets selling traditional handicrafts.",
        'nature': f"Surrounded by lush forests and scenic lakes, {city_name} is a peaceful sanctuary perfect for boating, bird-watching, and photography.",
        'cities': f"Blending heritage landmarks with modern shopping, {city_name} offers a lively street food scene and easy local transportation."
    }
    return details.get(theme, f"Visitors to {city_name} can take local heritage tours, sample regional delicacies, and explore traditional craft markets.")

def get_travel_tips(theme):
    tips = {
        'beaches': "Apply sun protection frequently. Follow local swimming safety guides. Dress in light cotton clothing.",
        'mountains': "Carry warm layers for cool nights. Book accommodations in advance during peak season.",
        'temples': "Dress conservatively when visiting sacred places. Remove footwear where requested. Respect local customs.",
        'palaces': "Wear comfortable shoes for walking tours. Hire certified local guides. Stay hydrated during day tours.",
        'nature': "Avoid littering in forest zones. Carry a reusable water bottle. Keep a safe distance from wildlife.",
        'cities': "Use local ride-hailing apps for easy travel. Keep small cash handy for local street markets."
    }
    return tips.get(theme, "Keep digital copies of IDs. Taste local street foods from clean places. Carry local currency.")


# States and Union Territories metadata (36 total) with pruned tourist-relevant cities lists
states_metadata = {
    'andhra pradesh': {
        'name': 'Andhra Pradesh', 'type': 'state', 'capital': 'Amaravati',
        'tag': 'LAND OF SPICES AND SHINES', 'language': 'Telugu',
        'best_time': 'October - March', 'food': 'Pesarattu, Hyderabadi Biryani',
        'theme': 'temples', 'cities_list': ['visakhapatnam', 'tirupati']
    },
    'arunachal pradesh': {
        'name': 'Arunachal Pradesh', 'type': 'state', 'capital': 'Itanagar',
        'tag': 'LAND OF THE RISING SUN', 'language': 'English & Hindi',
        'best_time': 'March - October', 'food': 'Thukpa, Momos & Zan',
        'theme': 'mountains', 'cities_list': ['itanagar', 'tawang', 'ziro']
    },
    'assam': {
        'name': 'Assam', 'type': 'state', 'capital': 'Dispur',
        'tag': 'THE TEA GARDEN OF INDIA', 'language': 'Assamese & Bengali',
        'best_time': 'November - April', 'food': 'Masor Tenga, Khar',
        'theme': 'nature', 'cities_list': ['guwahati']
    },
    'bihar': {
        'name': 'Bihar', 'type': 'state', 'capital': 'Patna',
        'tag': 'LAND OF MONASTERIES AND KNOWLEDGE', 'language': 'Hindi, Maithili',
        'best_time': 'October - March', 'food': 'Litti Chokha, Sattu Paratha',
        'theme': 'temples', 'cities_list': ['patna', 'gaya']
    },
    'chhattisgarh': {
        'name': 'Chhattisgarh', 'type': 'state', 'capital': 'Raipur',
        'tag': 'LAND OF SCENIC WATERFALLS', 'language': 'Chhattisgarhi & Hindi',
        'best_time': 'October - March', 'food': 'Chila, Muthia',
        'theme': 'nature', 'cities_list': ['raipur']
    },
    'goa': {
        'name': 'Goa', 'type': 'state', 'capital': 'Panaji',
        'tag': 'BEACH PARADISE', 'language': 'Konkani & English',
        'best_time': 'November - February', 'food': 'Goan Fish Curry',
        'theme': 'beaches', 'cities_list': ['panaji', 'calangute', 'anjuna', 'vagator', 'colva', 'palolem']
    },
    'gujarat': {
        'name': 'Gujarat', 'type': 'state', 'capital': 'Gandhinagar',
        'tag': 'LAND OF LEGENDS & FESTIVALS', 'language': 'Gujarati & Hindi',
        'best_time': 'November - February', 'food': 'Dhokla, Thepla, Khandvi',
        'theme': 'palaces', 'cities_list': ['ahmedabad', 'gandhinagar', 'bhuj', 'patan']
    },
    'haryana': {
        'name': 'Haryana', 'type': 'state', 'capital': 'Chandigarh',
        'tag': 'LAND OF GREEN FIELDS', 'language': 'Haryanvi & Hindi',
        'best_time': 'October - March', 'food': 'Singri ki Sabzi, Bajra Khichdi',
        'theme': 'cities', 'cities_list': ['gurugram']
    },
    'himachal pradesh': {
        'name': 'Himachal Pradesh', 'type': 'state', 'capital': 'Shimla',
        'tag': 'LAND OF GODS & SNOWY PEAKS', 'language': 'Hindi & Pahari',
        'best_time': 'March - June (Pleasant) & December - February (Snow)', 'food': 'Siddu, Madra',
        'theme': 'mountains', 'cities_list': ['shimla', 'manali', 'dharamshala']
    },
    'jammu & kashmir': {
        'name': 'Jammu & Kashmir', 'type': 'ut', 'capital': 'Srinagar (Summer), Jammu (Winter)',
        'tag': 'PARADISE ON EARTH', 'language': 'Kashmiri, Urdu & Dogri',
        'best_time': 'March - October (Srinagar) & October - March (Jammu)', 'food': 'Rogan Josh, Kahwa Tea',
        'theme': 'mountains', 'cities_list': ['srinagar', 'jammu', 'gulmarg', 'pahalgam', 'sonamarg']
    },
    'jharkhand': {
        'name': 'Jharkhand', 'type': 'state', 'capital': 'Ranchi',
        'tag': 'LAND OF FORESTS AND WATERFALLS', 'language': 'Hindi',
        'best_time': 'October - March', 'food': 'Duska, Litti Chokha',
        'theme': 'nature', 'cities_list': ['ranchi']
    },
    'karnataka': {
        'name': 'Karnataka', 'type': 'state', 'capital': 'Bengaluru',
        'tag': 'ONE STATE MANY WORLDS', 'language': 'Kannada',
        'best_time': 'October - March', 'food': 'Bisi Bele Bath, Mysore Pak',
        'theme': 'temples', 'cities_list': ['bengaluru', 'mysore', 'hampi', 'gokarna']
    },
    'kerala': {
        'name': 'Kerala', 'type': 'state', 'capital': 'Thiruvananthapuram',
        'tag': "GOD'S OWN COUNTRY", 'language': 'Malayalam',
        'best_time': 'September - March', 'food': 'Sadya, Puttu and Kadala Curry',
        'theme': 'beaches', 'cities_list': ['kochi', 'munnar', 'alappuzha', 'thiruvananthapuram', 'kovalam']
    },
    'madhya pradesh': {
        'name': 'Madhya Pradesh', 'type': 'state', 'capital': 'Bhopal',
        'tag': 'THE HEART OF INCREDIBLE INDIA', 'language': 'Hindi',
        'best_time': 'October - March', 'food': 'Poha Jalebi, Bhutte Ka Kees',
        'theme': 'temples', 'cities_list': ['bhopal', 'indore', 'gwalior', 'khajuraho', 'ujjain']
    },
    'maharashtra': {
        'name': 'Maharashtra', 'type': 'state', 'capital': 'Mumbai',
        'tag': 'LAND OF MARATHA WARRIORS', 'language': 'Marathi',
        'best_time': 'October - March', 'food': 'Vada Pav, Misal Pav',
        'theme': 'cities', 'cities_list': ['mumbai', 'pune', 'nagpur', 'aurangabad', 'lonavala']
    },
    'manipur': {
        'name': 'Manipur', 'type': 'state', 'capital': 'Imphal',
        'tag': 'JEWEL OF INDIA', 'language': 'Manipuri',
        'best_time': 'October - April', 'food': 'Eromba, Singju',
        'theme': 'nature', 'cities_list': ['imphal']
    },
    'meghalaya': {
        'name': 'Meghalaya', 'type': 'state', 'capital': 'Shillong',
        'tag': 'THE ABODE OF CLOUDS', 'language': 'Khasi, Garo & English',
        'best_time': 'October - June', 'food': 'Jadoh, Doh-Khlieh',
        'theme': 'nature', 'cities_list': ['shillong', 'cherrapunji']
    },
    'mizoram': {
        'name': 'Mizoram', 'type': 'state', 'capital': 'Aizawl',
        'tag': 'LAND OF BLUE MOUNTAINS', 'language': 'Mizo & English',
        'best_time': 'October - March', 'food': 'Bai, Sawhchiar',
        'theme': 'mountains', 'cities_list': ['aizawl']
    },
    'nagaland': {
        'name': 'Nagaland', 'type': 'state', 'capital': 'Kohima',
        'tag': 'LAND OF FESTIVALS', 'language': 'English',
        'best_time': 'October - May', 'food': 'Smoked Pork, Axone',
        'theme': 'mountains', 'cities_list': ['kohima']
    },
    'odisha': {
        'name': 'Odisha', 'type': 'state', 'capital': 'Bhubaneswar',
        'tag': 'THE SOUL OF INCREDIBLE INDIA', 'language': 'Odia',
        'best_time': 'October - March', 'food': 'Rasagola, Dalma',
        'theme': 'temples', 'cities_list': ['bhubaneswar', 'puri', 'konark']
    },
    'punjab': {
        'name': 'Punjab', 'type': 'state', 'capital': 'Chandigarh',
        'tag': 'LAND OF FIVE RIVERS', 'language': 'Punjabi',
        'best_time': 'October - March', 'food': 'Makki di Roti & Sarson ka Saag',
        'theme': 'cities', 'cities_list': ['amritsar', 'ludhiana', 'chandigarh']
    },
    'rajasthan': {
        'name': 'Rajasthan', 'type': 'state', 'capital': 'Jaipur',
        'tag': 'THE INCREDIBLE STATE OF INDIA', 'language': 'Hindi & Rajasthani',
        'best_time': 'October - March', 'food': 'Dal Baati Churma, Laal Maas',
        'theme': 'palaces', 'cities_list': ['jaipur', 'udaipur', 'jodhpur', 'jaisalmer', 'pushkar']
    },
    'sikkim': {
        'name': 'Sikkim', 'type': 'state', 'capital': 'Gangtok',
        'tag': 'VALLEY OF PEACE AND CLEANLINESS', 'language': 'Nepali & English',
        'best_time': 'March - June & October - December', 'food': 'Momos, Thukpa, Gundruk',
        'theme': 'mountains', 'cities_list': ['gangtok', 'pelling']
    },
    'tamil nadu': {
        'name': 'Tamil Nadu', 'type': 'state', 'capital': 'Chennai',
        'tag': 'LAND OF TEMPLES & HERITAGE', 'language': 'Tamil',
        'best_time': 'November - March', 'food': 'Sambar, Dosa, Pongal',
        'theme': 'temples', 'cities_list': ['chennai', 'coimbatore', 'ooty', 'kodaikanal', 'rameswaram', 'kanyakumari', 'madurai']
    },
    'telangana': {
        'name': 'Telangana', 'type': 'state', 'capital': 'Hyderabad',
        'tag': 'SEEDBED OF HISTORY', 'language': 'Telugu & Urdu',
        'best_time': 'October - March', 'food': 'Hyderabadi Dum Biryani, Haleem',
        'theme': 'palaces', 'cities_list': ['hyderabad', 'warangal']
    },
    'tripura': {
        'name': 'Tripura', 'type': 'state', 'capital': 'Agartala',
        'tag': 'LAND OF EXQUISITE HANDICRAFTS', 'language': 'Bengali & Kokborok',
        'best_time': 'October - March', 'food': 'Mui Borok, Kosha Mangsho',
        'theme': 'temples', 'cities_list': ['agartala']
    },
    'uttar pradesh': {
        'name': 'Uttar Pradesh', 'type': 'state', 'capital': 'Lucknow',
        'tag': 'LAND OF DIVERSITY AND DEVOTION', 'language': 'Hindi & Urdu',
        'best_time': 'October - March', 'food': 'Tunday Kebab, Petha, Bedmi Poori',
        'theme': 'temples', 'cities_list': ['lucknow', 'kanpur', 'agra', 'varanasi', 'prayagraj', 'ayodhya']
    },
    'uttarakhand': {
        'name': 'Uttarakhand', 'type': 'state', 'capital': 'Dehradun',
        'tag': 'LAND OF GODS & YOGA', 'language': 'Hindi & Garhwali',
        'best_time': 'March - June & September - November', 'food': 'Aloo Ke Gutke, Kafuli',
        'theme': 'mountains', 'cities_list': ['dehradun', 'haridwar', 'rishikesh', 'nainital', 'mussoorie']
    },
    'west bengal': {
        'name': 'West Bengal', 'type': 'state', 'capital': 'Kolkata',
        'tag': 'BEAUTY OF BENGAL & HIMALAYAS', 'language': 'Bengali & English',
        'best_time': 'October - March', 'food': 'Macher Jhol, Roshogolla',
        'theme': 'nature', 'cities_list': ['kolkata', 'darjeeling', 'siliguri', 'digha']
    },
    'andaman & nicobar islands': {
        'name': 'Andaman & Nicobar Islands', 'type': 'ut', 'capital': 'Port Blair',
        'tag': 'PRISTINE TROPICAL ARCHIPELAGO', 'language': 'Hindi, Bengali',
        'best_time': 'October - May', 'food': 'Tandoori Fish, Coconut Prawn Curry',
        'theme': 'beaches', 'cities_list': ['port blair', 'havelock island', 'neil island']
    },
    'chandigarh': {
        'name': 'Chandigarh', 'type': 'ut', 'capital': 'Chandigarh',
        'tag': 'THE CITY BEAUTIFUL', 'language': 'Hindi, Punjabi',
        'best_time': 'October - March', 'food': 'Chole Bhature, Butter Chicken',
        'theme': 'cities', 'cities_list': ['chandigarh']
    },
    'dadra & nagar haveli and daman & diu': {
        'name': 'Dadra & Nagar Haveli and Daman & Diu', 'type': 'ut', 'capital': 'Daman',
        'tag': 'PORTUGUESE HERITAGE AND BEACHES', 'language': 'Gujarati, Hindi',
        'best_time': 'October - March', 'food': 'Seafood, Dhal, Curry & Ubadiyu',
        'theme': 'beaches', 'cities_list': ['daman', 'diu']
    },
    'delhi': {
        'name': 'Delhi', 'type': 'ut', 'capital': 'New Delhi',
        'tag': 'HEART OF INDIA', 'language': 'Hindi, Punjabi',
        'best_time': 'October - March', 'food': 'Chole Bhature, Street Chaat',
        'theme': 'cities', 'cities_list': ['delhi', 'new delhi']
    },
    'lakshadweep': {
        'name': 'Lakshadweep', 'type': 'ut', 'capital': 'Kavaratti',
        'tag': 'CORAL REEF PARADISE', 'language': 'Jeseri (Malayalam dialect)',
        'best_time': 'October - May', 'food': 'Tuna Fish Fry, Coconut Fish Curry',
        'theme': 'beaches', 'cities_list': ['kavaratti', 'agatti', 'bangaram']
    },
    'puducherry': {
        'name': 'Puducherry', 'type': 'ut', 'capital': 'Puducherry',
        'tag': 'THE FRENCH RIVIERA OF THE EAST', 'language': 'Tamil, French',
        'best_time': 'October - March', 'food': 'French Pastries, Seafood Bouillabaisse',
        'theme': 'beaches', 'cities_list': ['puducherry']
    }
}

# Group attractions from comprehensive_indian_tourism.json by city key
EXTRA_ATTRACTIONS = {}
try:
    import os
    import json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'comprehensive_indian_tourism.json')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            extra_places = json.load(f)
            for item in extra_places:
                c_key = item['city'].lower().strip()
                s_key = item['state'].lower().strip()
                if c_key not in EXTRA_ATTRACTIONS:
                    EXTRA_ATTRACTIONS[c_key] = []
                EXTRA_ATTRACTIONS[c_key].append({
                    'name': item['tourist_place'],
                    'image': get_location_photo(c_key, item.get('category', 'landmark'), len(EXTRA_ATTRACTIONS[c_key])),
                    'desc': item.get('description') or item.get('desc', ''),
                    'description': item.get('description') or item.get('desc', '')
                })
                
                # Dynamically register this city to its state's cities_list if not present
                # so it gets compiled into DESTINATIONS!
                if s_key in states_metadata:
                    if c_key not in states_metadata[s_key]['cities_list']:
                        states_metadata[s_key]['cities_list'].append(c_key)
except Exception as e:
    pass

# Master dictionary to be filled dynamically on import
DESTINATIONS = {}

# 1. Load original custom 6 ones first
for k, v in CUSTOM_DESTINATIONS.items():
    DESTINATIONS[k] = v

# 2. Add States and UTs themselves
for key, data in states_metadata.items():
    if key in DESTINATIONS:
        # Preserve original hand-crafted states if they exist
        continue
    
    if key in STATE_DETAILS:
        state_info = STATE_DETAILS[key]
        image = state_info.get('image')
        about_image = state_info.get('about_image')
        tag = state_info.get('tag', data['tag'])
        description = state_info.get('description')
        about_more = state_info.get('about_more')
    else:
        image = get_location_photo(key, 'travel', 0)
        about_image = get_location_photo(key, 'nature', 1)
        tag = data['tag']
        description = f"{data['name']} is a famous {data['type'].upper()} in India, celebrated for its unique heritage, culinary flavors, and beautiful tourist destinations."
        about_more = f"Known for its local language '{data['language']}' and traditional foods like {data['food']}, {data['name']} offers a fantastic travel experience. The best time to visit is {data['best_time']}."
    
    # Pull dynamic attractions from child cities in REAL_ATTRACTIONS or EXTRA_ATTRACTIONS
    state_cities = data.get('cities_list', [])
    attractions = []
    for c_key in state_cities:
        city_attractions = []
        if c_key in REAL_ATTRACTIONS:
            city_attractions = REAL_ATTRACTIONS[c_key]
        elif c_key in EXTRA_ATTRACTIONS:
            city_attractions = EXTRA_ATTRACTIONS[c_key]
            
        if city_attractions:
            # Add the first attraction of this child city to represent the state
            attractions.append({
                'name': f"{city_attractions[0]['name']} ({c_key.title()})",
                'image': city_attractions[0]['image'],
                'desc': city_attractions[0]['desc'],
                'description': city_attractions[0]['description']
            })
                
    # Fallback if no child city has real attractions in this database
    if not attractions:
        attractions = [
            {
                'name': f"Famous Landmark of {data['name']}",
                'image': get_location_photo(key, 'landmark', 2),
                'desc': f"Experience the majestic views and heritage of {data['name']} at this iconic site.",
                'description': f"Experience the majestic views and heritage of {data['name']} at this iconic site."
            },
            {
                'name': f"Scenic Nature Trail in {data['name']}",
                'image': get_location_photo(key, 'nature', 3),
                'desc': f"Take a relaxing walk through the beautiful forests and nature parks of {data['name']}.",
                'description': f"Take a relaxing walk through the beautiful forests and nature parks of {data['name']}."
            },
            {
                'name': f"Ancient Spiritual Center in {data['name']}",
                'image': get_location_photo(key, 'temple', 4),
                'desc': f"Immerse yourself in local traditions at this historic spiritual destination.",
                'description': f"Immerse yourself in local traditions at this historic spiritual destination."
            }
        ]
        
    hotels = {
        'luxury': [
            {
                'name': get_hotel_name(data['name'], 'luxury', 0),
                'stars': '5 Star',
                'location': 'Capital Region',
                'image': get_location_photo(key, 'hotel', 5),
                'desc': f"A magnificent heritage palace hotel offering royal hospitality and spa wellness in {data['name']}.",
                'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(data['name'], 'luxury', 0).replace(' ', '+')}",
                'price': '₹20,000 / night',
                'amenities': ["Free Wi-Fi", "Swimming Pool", "Spa & Wellness", "Bar & Lounge", "Room Service"]
            },
            {
                'name': get_hotel_name(data['name'], 'luxury', 1),
                'stars': '5 Star',
                'location': 'Tourist Hub',
                'image': get_location_photo(key, 'hotel', 6),
                'desc': f"Premium luxury stay with beautiful views, fine dining, and excellent service in {data['name']}.",
                'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(data['name'], 'luxury', 1).replace(' ', '+')}",
                'price': '₹15,000 / night',
                'amenities': ["Free Wi-Fi", "Swimming Pool", "Spa & Wellness", "Free Parking", "Bar & Lounge"]
            }
        ],
        'comfort': [
            {
                'name': get_hotel_name(data['name'], 'comfort', 0),
                'stars': '4 Star',
                'location': 'City Centre',
                'image': get_location_photo(key, 'hotel', 7),
                'desc': f"Modern rooms, excellent business services, and outstanding local dining in {data['name']}.",
                'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(data['name'], 'comfort', 0).replace(' ', '+')}",
                'price': '₹6,500 / night',
                'amenities': ["Free Wi-Fi", "Air Conditioning", "Restaurant", "Free Parking"]
            },
            {
                'name': get_hotel_name(data['name'], 'comfort', 1),
                'stars': '4 Star',
                'location': 'Scenic Hills',
                'image': get_location_photo(key, 'hotel', 8),
                'desc': f"Comfortable rooms with scenic valley views, garden lounges, and tour packages in {data['name']}.",
                'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(data['name'], 'comfort', 1).replace(' ', '+')}",
                'price': '₹5,800 / night',
                'amenities': ["Free Wi-Fi", "Air Conditioning", "Restaurant", "Room Service"]
            }
        ],
        'budget': [
            {
                'name': get_hotel_name(data['name'], 'budget', 0),
                'stars': 'Budget',
                'location': 'Backpacker Hub',
                'image': get_location_photo(key, 'hotel', 9),
                'desc': f"Vibrant budget hostel offering social common areas and tourist guides in {data['name']}.",
                'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(data['name'], 'budget', 0).replace(' ', '+')}",
                'price': '₹900 / night',
                'amenities': ["Free Wi-Fi", "Common Lounge", "Kitchen Access", "Bike Rental"]
            },
            {
                'name': get_hotel_name(data['name'], 'budget', 1),
                'stars': 'Budget',
                'location': 'Transit Centre',
                'image': get_location_photo(key, 'hotel', 10),
                'desc': f"Affordable, clean, and comfortable lodging close to transit links in {data['name']}.",
                'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(data['name'], 'budget', 1).replace(' ', '+')}",
                'price': '₹1,500 / night',
                'amenities': ["Free Wi-Fi", "Air Conditioning", "Room Service", "Breakfast Included"]
            }
        ]
    }
    
    DESTINATIONS[key] = {
        'name': data['name'],
        'type': data['type'],
        'tag': tag,
        'description': description,
        'about_more': about_more,
        'image': image,
        'about_image': about_image,
        'language': data['language'],
        'best_time': data['best_time'],
        'food': data['food'].split(',')[0],
        'attractions': attractions,
        'hotels': hotels,
        'travel_tips': get_travel_tips(data['theme']),
        'nearby_attractions': "Local villages, scenic viewpoints, traditional craft bazaars."
    }


# 3. Add Cities dynamically
for state_key, state_data in states_metadata.items():
    for city_key in state_data['cities_list']:
        if city_key in DESTINATIONS:
            # Preserve original custom destinations (e.g. agra, jaipur, varanasi)
            # but ensure they link to their state name
            DESTINATIONS[city_key]['state'] = state_data['name']
            continue
            
        city_name = city_key.title()
        if city_key in CITY_DETAILS:
            city_info = CITY_DETAILS[city_key]
            image = city_info.get('image')
            about_image = city_info.get('about_image')
            tag = city_info.get('tag')
            description = city_info.get('description')
            about_more = city_info.get('about_more')
        else:
            image = get_location_photo(city_key, 'travel', 1)
            about_image = get_location_photo(city_key, 'nature', 2)
            tag = f"EXPLORE THE CHARMS OF {city_name.upper()}"
            description = get_location_description(city_name, state_data['name'], state_data['theme'])
            about_more = get_about_more(city_name, state_data['theme'])
        
        if city_key in REAL_ATTRACTIONS:
            attractions = REAL_ATTRACTIONS[city_key]
        elif city_key in EXTRA_ATTRACTIONS:
            attractions = EXTRA_ATTRACTIONS[city_key]
        else:
            attractions = [
                {
                    'name': f"{city_name} Heritage Site",
                    'image': get_location_photo(city_key, 'landmark', 3),
                    'desc': f"A beautiful heritage landmark in {city_name} showing rich local design and history.",
                    'description': f"A beautiful heritage landmark in {city_name} showing rich local design and history."
                },
                {
                    'name': f"{city_name} Scenic Point",
                    'image': get_location_photo(city_key, 'nature', 4),
                    'desc': f"A serene scenic park and lake, perfect for boat rides and peaceful walks in {city_name}.",
                    'description': f"A serene scenic park and lake, perfect for boat rides and peaceful walks in {city_name}."
                },
                {
                    'name': f"{city_name} Spiritual Center",
                    'image': get_location_photo(city_key, 'temple', 5),
                    'desc': f"An ancient spiritual sanctuary in {city_name} filled with peace and local devotion.",
                    'description': f"An ancient spiritual sanctuary in {city_name} filled with peace and local devotion."
                }
            ]
        
        hotels = {
            'luxury': [
                {
                    'name': get_hotel_name(city_name, 'luxury', 0),
                    'stars': '5 Star',
                    'location': 'Premium Lakefront / City Center',
                    'image': get_location_photo(city_key, 'hotel', 6),
                    'desc': f"World-class 5-star premium stay in {city_name} offering heritage interiors, spa, and fine dining.",
                    'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(city_name, 'luxury', 0).replace(' ', '+')}",
                    'price': '₹24,000 / night',
                    'amenities': ["Free Wi-Fi", "Swimming Pool", "Spa & Wellness", "Bar & Lounge", "Room Service"]
                },
                {
                    'name': get_hotel_name(city_name, 'luxury', 1),
                    'stars': '5 Star',
                    'location': 'Royal District',
                    'image': get_location_photo(city_key, 'hotel', 7),
                    'desc': f"Elegant suites, private pools, royal gardens, and personalized service in {city_name}.",
                    'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(city_name, 'luxury', 1).replace(' ', '+')}",
                    'price': '₹26,000 / night',
                    'amenities': ["Free Wi-Fi", "Swimming Pool", "Spa & Gym", "Fine Dining Restaurants"]
                }
            ],
            'comfort': [
                {
                    'name': get_hotel_name(city_name, 'comfort', 0),
                    'stars': '4 Star',
                    'location': 'Transit Hub / Main Road',
                    'image': get_location_photo(city_key, 'hotel', 8),
                    'desc': f"Comfortable rooms with modern amenities, swimming pool, and business lounge in {city_name}.",
                    'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(city_name, 'comfort', 0).replace(' ', '+')}",
                    'price': '₹6,800 / night',
                    'amenities': ["Free Wi-Fi", "Rooftop Pool", "Bar & Lounge", "Fitness Centre"]
                },
                {
                    'name': get_hotel_name(city_name, 'comfort', 1),
                    'stars': '4 Star',
                    'location': 'Business District',
                    'image': get_location_photo(city_key, 'hotel', 9),
                    'desc': f"Bright, contemporary rooms with outstanding hospitality and rooftop dining in {city_name}.",
                    'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(city_name, 'comfort', 1).replace(' ', '+')}",
                    'price': '₹5,000 / night',
                    'amenities': ["Free Wi-Fi", "Swimming Pool", "Rooftop Cafe", "Business Center"]
                }
            ],
            'budget': [
                {
                    'name': get_hotel_name(city_name, 'budget', 0),
                    'stars': 'Budget',
                    'location': 'Tourist Hub',
                    'image': get_location_photo(city_key, 'hotel', 10),
                    'desc': f"Vibrant and affordable backpacker lodging with social spaces and clean rooms in {city_name}.",
                    'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(city_name, 'budget', 0).replace(' ', '+')}",
                    'price': '₹850 / night',
                    'amenities': ["Free Wi-Fi", "Common Lounge", "Patio", "Bike Rental"]
                },
                {
                    'name': get_hotel_name(city_name, 'budget', 1),
                    'stars': 'Budget',
                    'location': 'Railway Station Road',
                    'image': get_location_photo(city_key, 'hotel', 11),
                    'desc': f"Clean and affordable rooms with friendly service and direct transit links in {city_name}.",
                    'link': f"https://www.booking.com/searchresults.html?ss={get_hotel_name(city_name, 'budget', 1).replace(' ', '+')}",
                    'price': '₹1,600 / night',
                    'amenities': ["Free Wi-Fi", "Air Conditioning", "Restaurant", "Travel Desk"]
                }
            ]
        }
        
        DESTINATIONS[city_key] = {
            'name': city_name,
            'type': 'city',
            'state': state_data['name'],
            'tag': tag,
            'description': description,
            'about_more': about_more,
            'image': image,
            'about_image': about_image,
            'language': state_data['language'],
            'best_time': state_data['best_time'],
            'food': state_data['food'].split(',')[0],
            'attractions': attractions,
            'hotels': hotels,
            'travel_tips': get_travel_tips(state_data['theme']),
            'nearby_attractions': f"Scenic viewpoints, local handicraft hubs, and historical sites of {state_data['name']} within 15km."
        }

# Helpers
def get_autocomplete_list():
    places = set()
    for key, data in DESTINATIONS.items():
        places.add(data['name'])
        if 'state' in data:
            places.add(data['state'])
    return sorted(list(places))

def get_states_list():
    states = []
    for key, data in DESTINATIONS.items():
        if data.get('type') in ['state', 'ut']:
            states.append({
                'key': key,
                'name': data['name'],
                'type': data['type']
            })
    return sorted(states, key=lambda x: x['name'])

def get_uts_list():
    uts = []
    for key, data in DESTINATIONS.items():
        if data.get('type') == 'ut':
            uts.append(data['name'])
    return sorted(uts)

def get_state_to_cities_mapping():
    mapping = {}
    for key, data in DESTINATIONS.items():
        if data.get('type') in ['state', 'ut']:
            mapping[key] = []
            
    for key, data in DESTINATIONS.items():
        if data.get('type') == 'city':
            state_name = data.get('state')
            state_key = None
            for sk, sd in DESTINATIONS.items():
                if sd.get('type') in ['state', 'ut'] and sd['name'].lower() == state_name.lower():
                    state_key = sk
                    break
            if state_key:
                if state_key not in mapping:
                    mapping[state_key] = []
                mapping[state_key].append({
                    'key': key,
                    'name': data['name']
                })
                
    for sk in mapping:
        mapping[sk] = sorted(mapping[sk], key=lambda x: x['name'])
        
    return mapping
