from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
import json
from .destinations_data import DESTINATIONS, get_autocomplete_list, get_states_list, get_state_to_cities_mapping
from .models import Review
from django.db.models import Avg

def get_live_alerts_for_place(place_key, place_name, state_name=None):
    name = place_name
    state = state_name or ""
    
    custom_alerts = {
        'agra': {
            'hospital': 'S.N. Medical College & Hospital, Agra',
            'police': 'Tajganj Police Station, Agra',
            'weather': 'Sunny and warm, 35°C. Carry water and sun wear.',
            'crowd': 'High crowd expected near the Taj Mahal this weekend.',
            'safety': 'High security checkpoints active. Tourist Police available.'
        },
        'jaipur': {
            'hospital': 'Sawai Man Singh (SMS) Hospital, Jaipur',
            'police': 'Manak Chowk Police Station, Jaipur',
            'weather': 'Sunny and dry, 38°C. Sun protection highly advised.',
            'crowd': 'Moderate tourist volume at Amber Palace and City Palace.',
            'safety': 'Safe zone verified. Night patrols active in central markets.'
        },
        'varanasi': {
            'hospital': 'Sir Sundarlal Hospital (BHU), Varanasi',
            'police': 'Dashashwamedh Police Station, Varanasi',
            'weather': 'Warm and humid, 34°C. Pleasant breeze near river banks.',
            'crowd': 'High crowd expected at Dashashwamedh Ghat for evening Aarti.',
            'safety': 'Guard your belongings in crowded ghat lanes. Active river patrols.'
        },
        'mumbai': {
            'hospital': 'King Edward Memorial (KEM) Hospital, Parel',
            'police': 'Colaba Police Station, Mumbai',
            'weather': 'Humid coastal weather, cloudy skies, 31°C.',
            'crowd': 'Moderate traffic and volume near Gateway of India.',
            'safety': 'CCTV surveillance active. Highly secure, 24/7 city patrols.'
        },
        'delhi': {
            'hospital': 'All India Institute of Medical Sciences (AIIMS), New Delhi',
            'police': 'Connaught Place Police Station, New Delhi',
            'weather': 'Clear skies, high UV index, 39°C. Carry sunglasses.',
            'crowd': 'Moderate crowd volumes at India Gate and Red Fort.',
            'safety': 'Active tourist police desks. Safe central transit corridors.'
        },
        'bengaluru': {
            'hospital': 'Bowring & Lady Curzon Hospital, Bengaluru',
            'police': 'Cubbon Park Police Station, Bengaluru',
            'weather': 'Pleasant breeze, partly cloudy, 28°C. Perfect outdoors.',
            'crowd': 'Low tourist crowds. Normal city traffic.',
            'safety': 'Very safe. Tourist assistance centers active.'
        },
        'goa': {
            'hospital': 'Goa Medical College & Hospital, Bambolim',
            'police': 'Calangute Police Station, Goa',
            'weather': 'Sunny beach weather, 32°C. Light sea breeze.',
            'crowd': 'High crowd expected at Baga and Calangute beaches.',
            'safety': 'Beach lifeguards active until sunset. Safe tourist swimming zones.'
        },
        'kerala': {
            'hospital': 'General Hospital, Ernakulam',
            'police': 'Fort Kochi Police Station, Kochi',
            'weather': 'Tropical warmth, 30°C. Slight chances of brief rain showers.',
            'crowd': 'Moderate traveler volume in backwater and houseboat sectors.',
            'safety': 'Safe beach fronts and hill stations. Local tourist police desks.'
        },
        'kashmir': {
            'hospital': 'Shri Maharaja Hari Singh (SMHS) Hospital, Srinagar',
            'police': 'Kothibagh Police Station, Srinagar',
            'weather': 'Cool mountain weather, 18°C. Clear roads.',
            'crowd': 'Moderate crowd volumes at Shalimar Bagh and Gulmarg cable cars.',
            'safety': 'Strict safety protocols verified by local administration.'
        }
    }
    
    key_lower = place_key.lower()
    if key_lower in custom_alerts:
        return custom_alerts[key_lower]
        
    hospital = f"Government Civil Hospital, {name.title()}"
    police = f"{name.title()} Central Police Station"
    
    is_mountain = any(m in name.lower() or (state and m in state.lower()) for m in ['himachal', 'uttarakhand', 'sikkim', 'ladakh', 'arunachal', 'kashmir', 'tawang', 'manali', 'shimla', 'leh'])
    is_beach = any(b in name.lower() or (state and b in state.lower()) for b in ['goa', 'kerala', 'andaman', 'daman', 'diu', 'lakshadweep', 'pondicherry', 'puducherry', 'visakhapatnam', 'digha', 'puri'])
    
    if is_mountain:
        weather = "Cool mountain breeze, temperature 16°C. Clear mountain roads."
        crowd = "Moderate crowd on popular trekking trails and viewpoint summits."
        safety = "Mountain rescue team on standby. Safe driving conditions."
    elif is_beach:
        weather = "Sunny beach weather, 31°C. Gentle coastal waves."
        crowd = "High crowd near beach shacks and sunset spots."
        safety = "Coastal guards on duty. Safe beach zone verified."
    else:
        weather = "Sunny and clear skies, 33°C. Perfect day for historic tours."
        crowd = "Low to moderate crowd at historical structures."
        safety = "Local police patrols active. Safe tourist sector."
        
    return {
        'hospital': hospital,
        'police': police,
        'weather': weather,
        'crowd': crowd,
        'safety': safety
    }

def home(request):
    states_list = get_states_list()
    state_to_cities = get_state_to_cities_mapping()
    state_to_cities_json = json.dumps(state_to_cities)
    
    # Pass comprehensive catalog list for home page search bar suggestions
    catalog_list = []
    # 1. Add States and Cities from DESTINATIONS
    for key, data in DESTINATIONS.items():
        catalog_list.append({
            'key': key,
            'name': data['name'],
            'type': data.get('type', 'city'),
            'state': data.get('state', '')
        })
        # 2. Add Attractions from each destination
        for att in data.get('attractions', []):
            catalog_list.append({
                'key': key,
                'name': att['name'],
                'type': 'attraction',
                'state': data['name'] if data.get('type') == 'state' else data.get('state', '')
            })
            
    # 3. Add items from ITEM_DETAILS
    from .item_details_data import ITEM_DETAILS
    for key, data in ITEM_DETAILS.items():
        catalog_list.append({
            'key': key,
            'name': data['name'],
            'type': data.get('type', 'attraction'),
            'state': data.get('location', ''),
            'is_item_detail': True
        })
        
    catalog_json = json.dumps(catalog_list)
    
    return render(request, 'homepage.html', {
        'states_list': states_list,
        'state_to_cities_json': state_to_cities_json,
        'catalog_json': catalog_json
    })


def about(request):
    return render(request, 'About.html')


def destination(request):
    query = request.GET.get('q', '').strip().lower()
    
    # 1. Exact match check
    if query:
        # Check if the query is an exact key in DESTINATIONS
        if query in DESTINATIONS:
            if query in ['agra', 'jaipur', 'kerala', 'goa', 'kashmir', 'varanasi']:
                return redirect(query)
            else:
                place_data = DESTINATIONS[query]
                # Query reviews and average rating
                reviews = Review.objects.filter(place_key=query).order_by('-created_at')
                avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
                avg_rating = round(avg_rating, 1)
                alerts = get_live_alerts_for_place(query, place_data['name'], place_data.get('state'))
                return render(request, 'destination_detail.html', {
                    'place': place_data,
                    'reviews': reviews,
                    'avg_rating': avg_rating,
                    'place_key': query,
                    'alerts': alerts
                })
        
        # Check if the query is an exact match for destination name
        found_key = None
        for key, data in DESTINATIONS.items():
            if data['name'].lower() == query:
                found_key = key
                break
        
        if found_key:
            if found_key in ['agra', 'jaipur', 'kerala', 'goa', 'kashmir', 'varanasi']:
                return redirect(found_key)
            else:
                place_data = DESTINATIONS[found_key]
                reviews = Review.objects.filter(place_key=found_key).order_by('-created_at')
                avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
                avg_rating = round(avg_rating, 1)
                alerts = get_live_alerts_for_place(found_key, place_data['name'], place_data.get('state'))
                return render(request, 'destination_detail.html', {
                    'place': place_data,
                    'reviews': reviews,
                    'avg_rating': avg_rating,
                    'place_key': found_key,
                    'alerts': alerts
                })

    # Prepare catalog data for dynamic search on the client
    catalog_list = []
    # 1. Add States and Cities from DESTINATIONS
    for key, data in DESTINATIONS.items():
        img = data['image']
        if img.startswith('images/'):
            img_url = f"/static/{img}"
        else:
            img_url = img
            
        catalog_list.append({
            'key': key,
            'name': data['name'],
            'type': data.get('type', 'city'),
            'state': data.get('state', ''),
            'tag': data.get('tag', ''),
            'description': data.get('description', ''),
            'image': img_url,
            'best_time': data.get('best_time', ''),
            'food': data.get('food', ''),
            'is_search_helper': False,
            'attraction_names': [att['name'].lower() for att in data.get('attractions', [])]
        })
        
        # 2. Add Attractions from each destination as helper items
        for att in data.get('attractions', []):
            catalog_list.append({
                'key': key,
                'name': att['name'],
                'type': 'attraction',
                'state': data['name'] if data.get('type') == 'state' else data.get('state', ''),
                'is_search_helper': True
            })
            
    # 3. Add items from ITEM_DETAILS as helper items
    from .item_details_data import ITEM_DETAILS
    for key, data in ITEM_DETAILS.items():
        catalog_list.append({
            'key': key,
            'name': data['name'],
            'type': data.get('type', 'attraction'),
            'state': data.get('location', ''),
            'is_item_detail': True,
            'is_search_helper': True
        })
        
    catalog_json = json.dumps(catalog_list)
    states_list = get_states_list()
    state_to_cities = get_state_to_cities_mapping()
    state_to_cities_json = json.dumps(state_to_cities)
    
    return render(request, 'destination.html', {
        'states_list': states_list,
        'state_to_cities_json': state_to_cities_json,
        'catalog_json': catalog_json,
        'initial_query': request.GET.get('q', '').strip()
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def contact(request):
    return render(request, 'contact us.html')    


def jaipur(request):
    place_key = 'jaipur'
    reviews = Review.objects.filter(place_key=place_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    alerts = get_live_alerts_for_place(place_key, 'Jaipur', 'Rajasthan')
    return render(request, 'jaipur.html', {
        'reviews': reviews,
        'avg_rating': avg_rating,
        'place_key': place_key,
        'alerts': alerts
    })


def agra(request):
    place_key = 'agra'
    reviews = Review.objects.filter(place_key=place_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    alerts = get_live_alerts_for_place(place_key, 'Agra', 'Uttar Pradesh')
    return render(request, 'agra.html', {
        'reviews': reviews,
        'avg_rating': avg_rating,
        'place_key': place_key,
        'alerts': alerts
    })


def kashmir(request):
    place_key = 'kashmir'
    reviews = Review.objects.filter(place_key=place_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    alerts = get_live_alerts_for_place(place_key, 'Kashmir', 'Jammu & Kashmir')
    return render(request, 'kashmir.html', {
        'reviews': reviews,
        'avg_rating': avg_rating,
        'place_key': place_key,
        'alerts': alerts
    })


def varanasi(request):
    place_key = 'varanasi'
    reviews = Review.objects.filter(place_key=place_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    alerts = get_live_alerts_for_place(place_key, 'Varanasi', 'Uttar Pradesh')
    return render(request, 'varanasi.html', {
        'reviews': reviews,
        'avg_rating': avg_rating,
        'place_key': place_key,
        'alerts': alerts
    })

def goa(request):
    place_key = 'goa'
    reviews = Review.objects.filter(place_key=place_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    alerts = get_live_alerts_for_place(place_key, 'Goa', 'Goa')
    return render(request, 'goa.html', {
        'reviews': reviews,
        'avg_rating': avg_rating,
        'place_key': place_key,
        'alerts': alerts
    })

def kerala(request):
    place_key = 'kerala'
    reviews = Review.objects.filter(place_key=place_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    alerts = get_live_alerts_for_place(place_key, 'Kerala', 'Kerala')
    return render(request, 'kerala.html', {
        'reviews': reviews,
        'avg_rating': avg_rating,
        'place_key': place_key,
        'alerts': alerts
    })

def item_detail(request, item_key):
    from .item_details_data import ITEM_DETAILS
    item_key = item_key.lower()
    
    if item_key not in ITEM_DETAILS:
        return redirect('home')
        
    item_data = ITEM_DETAILS[item_key]
    
    # Retrieve reviews specific to this item
    reviews = Review.objects.filter(place_key=item_key).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating, 1)
    
    # Try to load parent city/state metadata for hotels and weather alerts
    parent_key = item_data.get('parent_city_key')
    hotels = None
    alerts = None
    
    if parent_key and parent_key in DESTINATIONS:
        parent_data = DESTINATIONS[parent_key]
        hotels = parent_data.get('hotels')
        alerts = get_live_alerts_for_place(parent_key, parent_data['name'], parent_data.get('state'))
    else:
        # Fallback alerts if parent is not in DESTINATIONS
        alerts = get_live_alerts_for_place(item_key, item_data['name'], item_data['location'])
        
    return render(request, 'item_detail.html', {
        'item': item_data,
        'item_key': item_key,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'hotels': hotels,
        'alerts': alerts
    })

def submit_review(request, place_key):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to submit a review.")
            return redirect('login')

        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '').strip()

        if not rating or not comment:
            messages.error(request, "Please provide a rating and a comment.")
        else:
            try:
                rating = int(rating)
                if 1 <= rating <= 5:
                    Review.objects.create(
                        place_key=place_key.lower(),
                        user=request.user,
                        rating=rating,
                        comment=comment
                    )
                    messages.success(request, "Review submitted successfully!")
                else:
                    messages.error(request, "Rating must be between 1 and 5.")
            except ValueError:
                messages.error(request, "Invalid rating submitted.")

        from .item_details_data import ITEM_DETAILS
        if place_key.lower() in ITEM_DETAILS:
            return redirect('item_detail', item_key=place_key.lower())
        elif place_key.lower() in ['agra', 'jaipur', 'kerala', 'goa', 'kashmir', 'varanasi']:
            return redirect(place_key.lower())
        else:
            return redirect(f"/destination/?q={place_key}")
    return redirect('home')

def ai_planner(request):
    states_list = get_states_list()
    state_to_cities = get_state_to_cities_mapping()
    state_to_cities_json = json.dumps(state_to_cities)
    
    # Generate complete list of places for selection
    places = []
    for key, data in DESTINATIONS.items():
        places.append({
            'key': key,
            'name': data['name'],
            'type': data.get('type', 'city')
        })
    places = sorted(places, key=lambda x: x['name'])
    
    return render(request, 'ai_planner.html', {
        'states_list': states_list,
        'state_to_cities_json': state_to_cities_json,
        'destinations_list': places
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user to DB automatically
            return redirect('login')  # Go to login page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')


    return render(request, 'login.html')

