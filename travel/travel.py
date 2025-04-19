# Import necessary modules
import os
import time
import random
import requests
import json
from datetime import datetime
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import urllib.parse
from utils.image_utils import get_destination_image, get_attraction_image, get_cuisine_imageimport hashlib
import folium
from streamlit_folium import folium_staticge

# Page configuration with improved themectory
st.set_page_config(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/images")
    page_title="AI Travel Planner",k=True)
    page_icon="✈️",
    layout="wide",# Dictionary mapping destinations to image URLs for faster development
DESTINATION_IMAGES = {ate="expanded"
    "Paris": [
        "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
        "https://images.unsplash.com/photo-1499856871958-5b9627545d1a",6871958-5b9627545d1a",
        "https://images.unsplash.com/photo-1541791135449-6ceac4ebea0d"
    ],>
    "Rome": [der {
        "https://images.unsplash.com/photo-1529260830199-42c24126f198",
        "https://images.unsplash.com/photo-1552832230-c0197dd311b5",om/photo-1552832230-c0197dd311b5",
        "https://images.unsplash.com/photo-1515542622106-78bda8ba0e5b"da8ba0e5b"
    ],  -webkit-text-fill-color: transparent;
    "Tokyo": [lign: center;Tokyo": [
        "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc",998e48cbcc",
        font-size: 1.8rem;plash.com/photo-1503899036084-c55cdd92da26",
        color: #5E35B1;o-1513407030348-c983a97b98d8"
        margin-bottom: 1.2rem;
        text-align: center;
    }   color: #5E35B1;   "https://images.unsplash.com/photo-1518391846015-55a9cc003b25",
    .card {gin-bottom: 1.2rem;tps://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9",
        background-color: #f8f9fa;o-1534430480872-3498386e7856"
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 24px;lash.com/photo-1513635269975-59663e0ac1ad",8f9fa;
        border-left: 6px solid #1E88E5;oto-1529180184525-78f99958a373",
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);929736458-ca588d08c8be"
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }Sydney": [   border-left: 6px solid #1E88E5;
    .card:hover {images.unsplash.com/photo-1506973035872-a4ec16b8e8d9",w: 0 6px 12px rgba(0,0,0,0.1);
        transform: translateY(-5px);/photo-1524293581917-878a6d017c71",ase, box-shadow 0.3s ease;
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);2164453-f4e8ef0d475a"
    },card:hover {
    .highlight { [m: translateY(-5px);
        color: #E53935;.unsplash.com/photo-1583422409516-2895a77efded",2px 24px rgba(0,0,0,0.15);
        font-weight: bold;splash.com/photo-1579282240050-352db0a14c21",
    }   "https://images.unsplash.com/photo-1562883676-8c7feb83f09b"highlight {
    .info-box {
        background-color: #E3F2FD;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 18px;ges.unsplash.com/photo-1488646953014-85cb44e25828"3F2FD;
        border: 1px solid #BBDEFB;
    }ache_data(ttl=3600)   border-radius: 8px;
    .rating {nation_image(destination, index=None):n-bottom: 18px;
        color: #FFB300;n image from predefined list or fetch from Unsplash"""id #BBDEFB;
    destination = destination.split(",")[0].strip()  # Handle multi-city listings
    rating {
    # Try to match with our predefined destinations
    for known_dest in DESTINATION_IMAGES:
        if known_dest.lower() in destination.lower():
            images = DESTINATION_IMAGES[known_dest]color: #4CAF50; font-weight: bold;}
            if index is not None and 0 <= index < len(images):800; font-weight: bold;}
                return images[index]or: #F44336; font-weight: bold;}
            return random.choice(images)
    ;
    # If no match, use a cached search approach
    try:
        # Create a cache filename based on destination   border-radius: 8px;
        cache_key = hashlib.md5(destination.encode()).hexdigest() 0 15px 0;
        cache_path = os.path.join(IMAGE_CACHE_DIR, f"{cache_key}.jpg")
        
        # If image is already cached, return path
        if os.path.exists(cache_path):lid #1E88E5;
            return cache_path
           margin: 10px 0;
        # Construct Unsplash source URLdius: 4px;
        img_url = f"https://source.unsplash.com/800x600/?{destination},travel,city"
        response = requests.get(img_url, stream=True, timeout=5)
        
        if response.status_code == 200:id #e0e0e0;
            img = Image.open(BytesIO(response.content));
            img = img.convert("RGB")
            img.save(cache_path, "JPEG", quality=85)   margin: 10px 0;
            return cache_pathte;
    .2s ease;
    except Exception as e:
        print(f"Error fetching image for {destination}: {e}")hotel-card:hover {
     scale(1.02);
    # Fallback to default image(0,0,0,0.1);
    return DEFAULT_IMAGE

@st.cache_data(ttl=3600)FF5722;
def get_attraction_image(attraction_name):
    """Get an image for a specific attraction"""
    try:x;
        # Create a cache key for this attractionone;
        cache_key = hashlib.md5(f"attraction-{attraction_name}".encode()).hexdigest()   display: inline-block;
        cache_path = os.path.join(IMAGE_CACHE_DIR, f"{cache_key}.jpg");
        
        # If cached, return the path
        if os.path.exists(cache_path)::hover {
            return cache_pathor: #E64A19;
            
        # Use Unsplash source for attraction imagesicon-text {
        img_url = f"https://source.unsplash.com/600x400/?{attraction_name},attraction,landmark"x;
        response = requests.get(img_url, stream=True, timeout=5);
        
        if response.status_code == 200:t img {
            img = Image.open(BytesIO(response.content))
            img = img.convert("RGB")
            img.save(cache_path, "JPEG", quality=85)
            return cache_path
       padding: 20px;
    except Exception as e:: 30px;
        print(f"Error fetching attraction image: {e}")solid #e0e0e0;
    
    # Fallback to default image-content {
    return "https://images.unsplash.com/photo-1543429776-2782fc8e1acd"
    }
@st.cache_data(ttl=3600)
def get_cuisine_image(cuisine):llow_html=True)
    """Get image for a specific cuisine type"""
    try:# Load environment variables
        # Create a cache key for this cuisine
        cache_key = hashlib.md5(f"cuisine-{cuisine}".encode()).hexdigest()KEY")  # Fetch API key from .env file
        cache_path = os.path.join(IMAGE_CACHE_DIR, f"{cache_key}.jpg")
        
        # If cached, return the path
        if os.path.exists(cache_path):
            return cache_path Model Client - use a model that actually exists
            
        # Use Unsplash source for cuisine images
        img_url = f"https://source.unsplash.com/600x400/?{cuisine},food,restaurant"# Header with animation and destination image
        response = requests.get(img_url, stream=True, timeout=5)tions")
        tion_header_image, use_column_width=True)
        if response.status_code == 200:afe_allow_html=True)
            img = Image.open(BytesIO(response.content))>", unsafe_allow_html=True)
            img = img.convert("RGB")
            img.save(cache_path, "JPEG", quality=85)tional information with improved styling
            return cache_path
    st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=120)
    except Exception as e:lign: center;'>AI Travel Assistant</h2>", unsafe_allow_html=True)
        print(f"Error fetching cuisine image: {e}")
    
    # Fallback to default food imageraries based on your preferences and provides booking options.")
    return "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327"

# Page configuration with improved themeAPI Configuration"):
st.set_page_config(ini API Key", 
    page_title="AI Travel Planner",PI_KEY if GEMINI_API_KEY else "", 
    page_icon="✈️",
    layout="wide",                                 help="Enter your Gemini API key to use the service")
    initial_sidebar_state="expanded"
)API_KEY = api_key_input
pi_key=GEMINI_API_KEY)
# Enhanced Custom CSS for better stylingkey configured successfully!")
st.markdown("""
<style>ow to use")
    .main-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #1E88E5, #5E35B1);
        -webkit-background-clip: text;elect your budget level
        -webkit-text-fill-color: transparent;4. Add your interests
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800; links for hotels
    }
    .subheader {
        font-size: 1.8rem;quick selection with images
        color: #5E35B1;
        margin-bottom: 1.2rem;
        text-align: center;
    }columns(2)
    .card {
        background-color: #f8f9fa;with dest_col1:
        border-radius: 12px;("Paris", 0)
        padding: 25px;
        margin-bottom: 24px;
        border-left: 6px solid #1E88E5;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);        
        transition: transform 0.3s ease, box-shadow 0.3s ease;n_image("New York", 0)
    }
    .card:hover {ork"):
        transform: translateY(-5px);            st.session_state.destination = "New York"
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    .highlight {d real images"""
        color: #E53935;, use_column_width=True)
        font-weight: bold;    if st.button("🇯🇵 Tokyo"):
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 18px;    st.image(rome_img, caption="Rome", use_column_width=True)
        border-radius: 8px; realistic hotel names for common destinationsbutton("🇮🇹 Rome"):
        margin-bottom: 18px;ion_state.destination = "Rome"
        border: 1px solid #BBDEFB;s": {
    }"Ibis Paris Montmartre"],
    .rating { Plaza Athénée", "Le Pavillon de la Reine"],"Email Address", placeholder="Enter email to receive itinerary")
        color: #FFB300;ns Hotel George V", "The Ritz Paris"], type="secondary"):
        font-weight: bold;
    }
            "Budget": ["Pod 51 Hotel", "Hotel 31"],
            "Mid-range": ["The Beekman", "Ace Hotel New York"],d {color: #FF9800; font-weight: bold;}.warning("Please enter an email address")
            "Luxury": ["The Plaza", "The St. Regis New York"]igh {color: #F44336; font-weight: bold;}
        },
        "Tokyo": {ng Streamlit and Google Gemini AI")
            "Budget": ["Hotel Gracery Shinjuku", "Sakura Hotel Ikebukuro"],
            "Mid-range": ["Park Hotel Tokyo", "The Prince Gallery Tokyo"],
            "Luxury": ["Aman Tokyo", "Hoshinoya Tokyo"]
        },
        "Rome": {align: center;hotels based on destination and budget with booking links"""
            "Budget": ["Hotel Centro Roma", "Generator Rome"],0.5)  # Simulate API latency
            "Mid-range": ["Hotel Artemide", "Palazzo Naiadi"],
            "Luxury": ["Hotel de Russie", "Villa Spalletti Trivelli"]r-left: 4px solid #1E88E5;encoded destination for MakeMyTrip URL
        }
    }trip.com/hotels/hotel-listing/?checkin=PLACEHOLDER&city={encoded_destination}"
    
    # Get destination-specific hotels if available
    if destination in hotel_names and budget in hotel_names[destination]:
        hotel_name_list = hotel_names[destination][budget]
    else:: 1px solid #e0e0e0;  "name": f"{destination} Budget Inn", 
        # Generic hotel namesr-radius: 8px;   "price": "$40", 
        hotel_name_list = [
            f"{destination} {budget} Hotel",ee WiFi", "Continental Breakfast"],
            f"{budget} Inn {destination}"cdn-icons-png.flaticon.com/512/2621/2621763.png",
        ]
    
    # Price ranges based on budget
    price_ranges = {   "name": f"{destination} Hostel Central", form: scale(1.02);
        "Budget": {"min": 30, "max": 80},      "price": "$30", x-shadow: 0 4px 8px rgba(0,0,0,0.1);
        "Mid-range": {"min": 100, "max": 250},ting": "3.5★", 
        "Luxury": {"min": 300, "max": 1000}   "amenities": ["Shared Kitchen", "Locker Storage"],btn {
    }n.com/512/2621/2621763.png",
    oking_base_url + "&price=0-3000"
    price_range = price_ranges.get(budget, price_ranges["Mid-range"])
    
    hotels = []
    for name in hotel_name_list:
        # Create a hotel object with more realistic data  "name": f"{destination} Comfort Hotel", -top: 10px;
        hotel = {   "price": "$100", weight: bold;
            "name": name,
            "price": f"${random.randint(price_range['min'], price_range['max'])}",ol", "Fitness Center", "Restaurant"],
            "rating": f"{random.uniform(3.5, 5.0):.1f}★",cdn-icons-png.flaticon.com/512/3774/3774106.png",
            "amenities": random.sample([
                "Free WiFi", "Breakfast Included", "Fitness Center", 
                "Pool", "Spa", "Room Service", "Airport Shuttle", 
                "Concierge", "Parking", "Restaurant", "Bar"   "name": f"{destination} City Suites", -items: center;
            ], k=random.randint(3, 6)),       "price": "$120", 
            "image": get_destination_image(f"{name} hotel {destination}"),           "rating": "4.3★", icon-text img {
            "booking_url": booking_base_url + f"&price={price_range['min']}-{price_range['max']}" Access", "Airport Shuttle"],
        }                "image": "https://cdn-icons-png.flaticon.com/512/3774/3774106.png",    }
        hotels.append(hotel)l + "&price=3001-7000"
    
    return hotels
    "Luxury": [    margin-top: 30px;
def fetch_attractions(destination, interests):
    """Fetch attractions based on interests"""lace {destination}", 
    time.sleep(0.5)  # Simulate API latency
           "rating": "4.8★", adding: 20px 0;
    # Handle both string and list inputs for interestscierge", "Spa", "Pool"],
    if isinstance(interests, str):            "image": "https://cdn-icons-png.flaticon.com/512/2296/2296470.png",yle>
        interests_list = [i.strip().lower() for i in interests.split(",")]ce=7001-50000"
    else:
        interests_list = [i.lower() for i in interests]s
       "name": f"{destination} Luxury Resort", 
    # Enhanced attractions with images and more details
    attractions = {
        "culture": [
            {
                "name": f"{destination} Historical Museum",  booking_base_url + "&price=7001-50000"
                "rating": "4.5★", nerative Model Client - use a model that actually exists
                "description": "Explore the rich history of the region with interactive exhibits",erativeModel("gemini-2.0-flash-exp")
                "image": "https://cdn-icons-png.flaticon.com/512/3460/3460261.png",
                "price": "$15"ls["Mid-range"])
            },
            {=True)
                "name": f"{destination} Art Gallery",  on interests"""
                "rating": "4.3★", p(0.5)  # Simulate API latencyar for additional information with improved styling
                "description": "Contemporary and classic art exhibitions from renowned artists",
                "image": "https://cdn-icons-png.flaticon.com/512/2942/2942539.png",ring and list inputs for interests//cdn-icons-png.flaticon.com/512/201/201623.png", width=120)
                "price": "$12"ance(interests, str):wn("<h2 style='text-align: center;'>AI Travel Assistant</h2>", unsafe_allow_html=True)
            }sts.split(",")]
        ],
        "history": [
            {
                "name": f"Ancient Ruins of {destination}", h images and more detailsr UI
                "rating": "4.7★", s = {pander("🔑 API Configuration"):
                "description": "Well-preserved ruins dating back centuries with guided tours available",ure": [ey_input = st.text_input("Gemini API Key", 
                "image": "https://cdn-icons-png.flaticon.com/512/2531/2531123.png",
                "price": "$20"tion} Historical Museum",    type="password",
            },
            {tive exhibits",
                "name": f"{destination} Historical Quarter", ://cdn-icons-png.flaticon.com/512/3460/3460261.png",i_key_input
                "rating": "4.4★",    "price": "$15"enai.configure(api_key=GEMINI_API_KEY)
                "description": "Walk through the streets of the old town with beautiful architecture",  },  st.success("API key configured successfully!")
                "image": "https://cdn-icons-png.flaticon.com/512/3075/3075886.png",
                "price": "Free"           "name": f"{destination} Art Gallery", t.markdown("### 🔍 How to use")
            }            "rating": "4.3★", st.markdown("""
        ], "description": "Contemporary and classic art exhibitions from renowned artists",ur destination
        # Additional categories omitted for brevitydn-icons-png.flaticon.com/512/2942/2942539.png",
    }
    
    result = []
    for interest in interests_list:
        if interest in attractions:
            for attraction in attractions[interest]:f {destination}", 
                # Add destination context to generic attractions            "rating": "4.7★", 
                if destination.lower() not in attraction["name"].lower(): centuries with guided tours available",
                    attraction["name"] = f"{attraction['name']} in {destination}"mage": "https://cdn-icons-png.flaticon.com/512/2531/2531123.png",## 🌍 Popular Destinations")
                result.append(attraction)ice": "$20"ns(2)
    
    # Add city tour as a default option if no matching interests
    if not result:
        result = [{
            "name": f"{destination} City Tour", on": "Walk through the streets of the old town with beautiful architecture", York"):
            "rating": "4.0★",       "image": "https://cdn-icons-png.flaticon.com/512/3075/3075886.png",.session_state.destination = "New York"
            "description": "See the highlights of the city with an experienced guide",            "price": "Free"if cols[1].button("Rome"):
            "image": "https://cdn-icons-png.flaticon.com/512/2916/2916150.png",ate.destination = "Rome"
            "price": "$25"        ],    
        }]
        }    st.text_input("Email Address", placeholder="Enter email to receive itinerary")
    return result

# The other functions remain largely the same but with improved response formatting

def fetch_restaurants(destination, cuisine):rest]:it and Google Gemini AI")
    """Fetch restaurants based on cuisine preference"""            # Add destination context to generic attractionsst.markdown("Version 2.1.0")
    time.sleep(0.5)  # Simulate API latencydestination.lower() not in attraction["name"].lower():
    price_options = ["$", "$$", "$$$", "$$$$"]           attraction["name"] = f"{attraction['name']} in {destination}"d Mock API functions with better data and makeMyTrip integration
    ratings = ["4.2★", "4.5★", "4.7★", "4.0★"]
    
    restaurants = [option if no matching interestsPI latency
        {
            "name": f"Local {cuisine} Diner in {destination}",
            "price": random.choice(price_options),)
            "rating": ratings[0],  "rating": "4.0★", g_base_url = f"https://www.makemytrip.com/hotels/hotel-listing/?checkin=PLACEHOLDER&city={encoded_destination}"
            "specialty": f"Traditional {cuisine} classics",   "description": "See the highlights of the city with an experienced guide",
            "image": "https://cdn-icons-png.flaticon.com/512/2922/2922037.png",om/512/2916/2916150.png",
            "address": f"123 Main St, {destination}"
        },
        {
            "name": f"Authentic {cuisine} Experience",
            "price": random.choice(price_options),
            "rating": ratings[1],r functions remain largely the same but with improved response formatting      "amenities": ["Free WiFi", "Continental Breakfast"],
            "specialty": f"Chef's {cuisine} tasting menu",mage": "https://cdn-icons-png.flaticon.com/512/2621/2621763.png",
            "image": "https://cdn-icons-png.flaticon.com/512/1046/1046857.png",
            "address": f"456 Boulevard, {destination}"ce"""
        },PI latency
        {
            "name": f"{cuisine} Fusion in {destination}",
            "price": random.choice(price_options),
            "rating": ratings[2],rants = [      "amenities": ["Shared Kitchen", "Locker Storage"],
            "specialty": f"Modern twist on {cuisine} classics",       "image": "https://cdn-icons-png.flaticon.com/512/2621/2621763.png",
            "image": "https://cdn-icons-png.flaticon.com/512/3170/3170733.png",ner in {destination}",ase_url + "&price=0-3000"
            "address": f"789 Food Street, {destination}"
        },
        {ssics",
            "name": f"Bistro {cuisine}",
            "price": random.choice(price_options),
            "rating": ratings[3],,       "price": "$100", 
            "specialty": f"Casual {cuisine} dining",   {           "rating": "4.2★", 
            "image": "https://cdn-icons-png.flaticon.com/512/4080/4080032.png",        "name": f"Authentic {cuisine} Experience",            "amenities": ["Pool", "Fitness Center", "Restaurant"],
            "address": f"101 Culinary Ave, {destination}"andom.choice(price_options),": "https://cdn-icons-png.flaticon.com/512/3774/3774106.png",
        }            "rating": ratings[1],                "booking_url": booking_base_url + "&price=3001-7000"
    ]sine} tasting menu",
    m/512/1046/1046857.png",
    return restaurantsstination}"y Suites", 
    },            "price": "$120", 
def fetch_weather(destination, dates):
    """Simulated weather forecast with improved data"""stination}", "Spa Access", "Airport Shuttle"],
    time.sleep(0.5)  # Simulate API latencyon.com/512/3774/3774106.png",
    001-7000"
    weather_conditions = [} classics",
        {"condition": "Sunny", "icon": "☀️"},com/512/3170/3170733.png",
        {"condition": "Partly Cloudy", "icon": "⛅"},destination}"
        {"condition": "Cloudy", "icon": "☁️"},   },       {
        {"condition": "Light Rain", "icon": "🌦️"},    {            "name": f"Grand Palace {destination}", 
        {"condition": "Thunderstorms", "icon": "⛈️"}, f"Bistro {cuisine}",ice": "$300", 
        {"condition": "Clear", "icon": "✨"}
    ]
           "specialty": f"Casual {cuisine} dining",           "image": "https://cdn-icons-png.flaticon.com/512/2296/2296470.png",
    temp_ranges = {        "image": "https://cdn-icons-png.flaticon.com/512/4080/4080032.png",            "booking_url": booking_base_url + "&price=7001-50000"
        "Paris": (15, 25), "Rome": (18, 30), "Tokyo": (15, 28),n}"
        "New York": (10, 25), "London": (12, 20), "Sydney": (18, 28)
    }]            "name": f"{destination} Luxury Resort", 
    
    low, high = temp_ranges.get(destination, (15, 25))rn restaurants        "rating": "4.9★", 
    days = 5  # Default forecast dayste Beach", "Helicopter Pad"],
    
    # Parse date range if providedted weather forecast with improved data"""   "booking_url": booking_base_url + "&price=7001-50000"
    try:ency
        if " to " in dates:
            start_date = datetime.strptime(dates.split(" to ")[0], "%Y-%m-%d")
        else:    {"condition": "Sunny", "icon": "☀️"},return hotels.get(budget, hotels["Mid-range"])
            start_date = datetime.now()on": "Partly Cloudy", "icon": "⛅"},
    except:oudy", "icon": "☁️"},tination, interests):
        start_date = datetime.now()
    ,
    forecast = []ear", "icon": "✨"}
    for i in range(days):interests
        weather_choice = random.choice(weather_conditions)
        day_date = start_date + pd.Timedelta(days=i)
        forecast.append({, "Tokyo": (15, 28),
            "day": i + 1,Sydney": (18, 28)sts]
            "date": day_date.strftime("%b %d"),
            "condition": weather_choice["condition"],
            "icon": weather_choice["icon"],igh = temp_ranges.get(destination, (15, 25))tions = {
            "high_temp": random.randint(low, high),days = 5  # Default forecast days    "culture": [
            "low_temp": random.randint(low - 5, low + 3),
            "humidity": random.randint(40, 90)    # Parse date range if provided                "name": f"{destination} Historical Museum", 
        })
    : "Explore the rich history of the region with interactive exhibits",
    return forecastlit(" to ")[0], "%Y-%m-%d")ticon.com/512/3460/3460261.png",

# Function to call Google Gemini API with improved error handling and fallback
def call_gemini_api(prompt):    except:            {
    """Call the Gemini API with the given prompt"""start_date = datetime.now()        "name": f"{destination} Art Gallery", 
    if not GEMINI_API_KEY:
        return "⚠️ API Key missing. Please provide a Gemini API key in the sidebar."mporary and classic art exhibitions from renowned artists",
range(days):   "image": "https://cdn-icons-png.flaticon.com/512/2942/2942539.png",
    try:ns)
        # Add fallback logic for safety
        safety_settings = [st.append({
            {day": i + 1,ory": [
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"on}", 
            },con": weather_choice["icon"],  "rating": "4.7★", 
            {high_temp": random.randint(low, high),   "description": "Well-preserved ruins dating back centuries with guided tours available",
                "category": "HARM_CATEGORY_HATE_SPEECH",31/2531123.png",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }, call Google Gemini API with improved error handling and fallback   "description": "Walk through the streets of the old town with beautiful architecture",
            {gemini_api(prompt):       "image": "https://cdn-icons-png.flaticon.com/512/3075/3075886.png",
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",all the Gemini API with the given prompt"""        "price": "Free"
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }issing. Please provide a Gemini API key in the sidebar."
        ]brevity
        
        generation_config = genai.types.GenerationConfig(or safety
            temperature=0.7,
            top_p=0.9,   {nterest in interests_list:
            top_k=40,        "category": "HARM_CATEGORY_HARASSMENT",if interest in attractions:
            candidate_count=1,_AND_ABOVE"interest]:
            max_output_tokens=2048stination context to generic attractions
        )
        HATE_SPEECH",{attraction['name']} in {destination}"
        response = model.generate_content(       "threshold": "BLOCK_MEDIUM_AND_ABOVE"       result.append(attraction)
            prompt,
            generation_config=generation_config,    {d city tour as a default option if no matching interests
            safety_settings=safety_settings: "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        )UM_AND_ABOVE"
        return response.text
        
    except Exception as e:                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",            "description": "See the highlights of the city with an experienced guide",
        st.error(f"API Error: {str(e)}")",
        # Fallback to generate a simple itinerary
        return generate_fallback_itinerary(destination, num_days, interests_str)

# Fallback function to generate a simple itinerary when API fails    generation_config = genai.types.GenerationConfig(return result
def generate_fallback_itinerary(destination, days, interests):
    """Generate a fallback itinerary when the API call fails"""roved response formatting
    itinerary = f"# 🗺️ Your {days}-Day {destination} Itinerary\n\n"    top_k=40,
    date_count=1,ants(destination, cuisine):
    for day in range(1, days + 1):ine preference"""
        itinerary += f"## Day {day}\n\n"
        
        # Morning
        itinerary += "### Morning\n"    prompt,
        itinerary += f"- Breakfast at your hotel\n"ion_config=generation_config,
        itinerary += f"- Explore local attractions in {destination}\n"tings
        itinerary += f"- Visit museums or historical sites\n\n"
        
        # Afternoon
        itinerary += "### Afternoon\n"pt Exception as e:    "specialty": f"Traditional {cuisine} classics",
        itinerary += f"- Enjoy lunch at a local restaurant\n"f"API Error: {str(e)}")e": "https://cdn-icons-png.flaticon.com/512/2922/2922037.png",
        itinerary += f"- Continue sightseeing around {destination}\n"ple itinerary, {destination}"
        itinerary += f"- Shopping or leisure time\n\n"s_str)
        
        # Eveningllback function to generate a simple itinerary when API fails        "name": f"Authentic {cuisine} Experience",
        itinerary += "### Evening\n"ts):
        itinerary += f"- Dinner at a restaurant featuring local cuisine\n""""
        itinerary += f"- Evening entertainment or relaxation\n\n"Itinerary\n\n"nu",
    
    itinerary += f"\n## Travel Tips for {destination}\n\n"for day in range(1, days + 1):        "address": f"456 Boulevard, {destination}"
    itinerary += "- Research local transportation options\n" f"## Day {day}\n\n"
    itinerary += "- Check for any travel advisories\n"                {
    itinerary += "- Pack appropriate clothing for the weather\n"
    Morning\n"m.choice(price_options),
    return itinerary        itinerary += f"- Breakfast at your hotel\n"            "rating": ratings[2],
inerary += f"- Explore local attractions in {destination}\n"  "specialty": f"Modern twist on {cuisine} classics",
# Create two columns for the input form with improved stylingn"3170/3170733.png",
col1, col2 = st.columns(2)            "address": f"789 Food Street, {destination}"

with col1:on\n"
    st.markdown("<div class='card'>", unsafe_allow_html=True) local restaurant\n"
    ination}\n"
    # Use session state for destination if set by quick linksitinerary += f"- Shopping or leisure time\n\n"    "rating": ratings[3],
    default_destination = "Paris"
    if 'destination' in st.session_state:
        default_destination = st.session_state.destinationation}"
        n"
    destination = st.text_input("📍 Destination", default_destination)or relaxation\n\n"
    travel_dates = st.text_input("📅 Travel Dates", "2025-06-15 to 2025-06-20")
    budget = st.select_slider("💰 Budget", ion}\n\n"
                             options=["Budget", "Mid-range", "Luxury"],     itinerary += "- Research local transportation options\n"
                             value="Mid-range",ary += "- Check for any travel advisories\n"weather(destination, dates):
                             help="Select your budget level for accommodations and activities")\n"
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True) with improved styling"☀️"},
    interests = st.multiselect(
        "🎯 Select your interests",condition": "Cloudy", "icon": "☁️"},
        options=["culture", "history", "food", "nature", "adventure", "shopping"],
        default=["culture", "history"],st.markdown("<div class='card'>", unsafe_allow_html=True)    {"condition": "Thunderstorms", "icon": "⛈️"},
        help="Choose activities that interest you the most"
    )
    interests_str = ", ".join(interests)
        if 'destination' in st.session_state:    temp_ranges = {
    cuisine = st.text_input("🍽️ Preferred Cuisine", "Local")
    num_days = st.slider("📆 Number of days", min_value=1, max_value=7, value=3)
    st.markdown("</div>", unsafe_allow_html=True)n", default_destination)
travel_dates = st.text_input("📅 Travel Dates", "2025-06-15 to 2025-06-20")
# Show hotels based on budget with improved display and booking links
with st.expander("🏨 Available Hotels"):
    hotels = fetch_hotels(destination, budget)                         value="Mid-range",
         help="Select your budget level for accommodations and activities")f provided
    # Create a nice display for hotels with booking links
    st.markdown("<div class='hotel-selection'>", unsafe_allow_html=True)
    2:    start_date = datetime.strptime(dates.split(" to ")[0], "%Y-%m-%d")
    for hotel in hotels: class='card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='hotel-card'>", unsafe_allow_html=True)
        cols = st.columns([1, 3])
        ons=["culture", "history", "food", "nature", "adventure", "shopping"],t_date = datetime.now()
        with cols[0]:ture", "history"],
            st.image(hotel["image"], width=80)terest you the most"
            st.markdown(f"<span class='rating'>{hotel['rating']}</span>", unsafe_allow_html=True)
            
        with cols[1]:tart_date + pd.Timedelta(days=i)
            st.subheader(hotel["name"])ne", "Local")
            st.markdown(f"**Price:** {hotel['price']} per night")
            st.markdown(f"**Amenities:** {', '.join(hotel['amenities'])}")
             weather_choice["condition"],
            # Add a booking link to Make My Tripnd booking links
            booking_url = hotel["booking_url"].replace("PLACEHOLDER", travel_dates.split(" to ")[0] if " to " in travel_dates else "2025-06-15")
            st.markdown(f"<a href='{booking_url}' target='_blank' class='booking-btn'>Book on MakeMyTrip</a>", unsafe_allow_html=True)hotels = fetch_hotels(destination, budget)        "low_temp": random.randint(low - 5, low + 3),
            
        st.markdown("</div>", unsafe_allow_html=True)    # Create a nice display for hotels with booking links        })
        st.markdown("<br>", unsafe_allow_html=True) unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)    for hotel in hotels:
(f"<div class='hotel-card'>", unsafe_allow_html=True)Google Gemini API with improved error handling and fallback
# Generate Itinerary Button and Processing Block
generate_button = st.button("🗺️ Generate My Perfect Itinerary", type="primary", use_container_width=True)
ith cols[0]:t GEMINI_API_KEY:
if generate_button:80)provide a Gemini API key in the sidebar."
    if not destination or not travel_dates:class='rating'>{hotel['rating']}</span>", unsafe_allow_html=True)
        st.error("⚠️ Please enter a destination and travel dates.")
    else:
        progress_container = st.container()st.subheader(hotel["name"])ty_settings = [
        with progress_container:['price']} per night")
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1: Gather travel detailsotel["booking_url"].replace("PLACEHOLDER", travel_dates.split(" to ")[0] if " to " in travel_dates else "2025-06-15")
            status_text.info("🏨 Step 1/4: Finding the best hotels for your stay...")st.markdown(f"<a href='{booking_url}' target='_blank' class='booking-btn'>Book on MakeMyTrip</a>", unsafe_allow_html=True)    "category": "HARM_CATEGORY_HATE_SPEECH",
            progress_bar.progress(25)
            hotels = fetch_hotels(destination, budget)
            time.sleep(0.8)low_html=True)
            
            # Step 2: Discover attractionsnsafe_allow_html=True): "BLOCK_MEDIUM_AND_ABOVE"
            status_text.info("🏛️ Step 2/4: Discovering attractions based on your interests...")
            progress_bar.progress(50)
            attractions = fetch_attractions(destination, interests_str)e_container_width=True)
            time.sleep(0.8)
            
            # Step 3: Get restaurant recommendations and weather forecast
            status_text.info("🍽️ Step 3/4: Finding the best local restaurants...") enter a destination and travel dates.")
            progress_bar.progress(75)ion_config = genai.types.GenerationConfig(
            restaurants = fetch_restaurants(destination, cuisine)
            weather = fetch_weather(destination, travel_dates)
            time.sleep(0.8)(0)
            status_text = st.empty()candidate_count=1,
            # Step 4: Generate itinerary with AI
            status_text.info("✨ Step 4/4: Creating your personalized itinerary with AI...")
            progress_bar.progress(100)status_text.info("🏨 Step 1/4: Finding the best hotels for your stay...")
            (25)_content(
            prompt = f"""ation, budget)
            Create a detailed {num_days}-day travel itinerary for {destination} from {travel_dates}.ig,
            safety_settings=safety_settings
            TRAVELER PREFERENCES:ttractions
            - Interests: {interests_str}based on your interests...")
            - Budget level: {budget}
            
            FORMAT INSTRUCTIONS:
            - Format using Markdown with clear headings for each day
            - For each day, include morning, afternoon, and evening sectionsorecastinterests_str)
            - Include 2 specific attractions each day from this list: {[attr['name'] for attr in attractions]}
            - Recommend specific restaurants for lunch and dinner each day from this list: {[rest['name'] for rest in restaurants]}gress_bar.progress(75)tion to generate a simple itinerary when API fails
            - Include practical tips about transportation and logisticsrestaurants = fetch_restaurants(destination, cuisine)_fallback_itinerary(destination, days, interests):
            - Adjust activities to match the {budget} budget level, travel_dates)PI call fails"""
            - Include a brief section at the end with useful travel tips specific to {destination}.ion} Itinerary\n\n"
            """    
            
            itinerary = call_gemini_api(prompt)    status_text.info("✨ Step 4/4: Creating your personalized itinerary with AI...")itinerary += f"## Day {day}\n\n"
            progress_container.empty()
            # Morning
        st.success("✅ Your personalized travel itinerary is ready!")f""""### Morning\n"
        stination} from {travel_dates}.
        tabs = st.tabs(["📝 Complete Itinerary", "🏨 Hotels", "🏛️ Attractions", "🍽️ Restaurants", "🌤️ Weather", "📊 Trip Summary"])
        ums or historical sites\n\n"
        with tabs[0]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader(f"🗺️ Your AI-Generated {destination} Travel Itinerary")oon\n"
            st.markdown(itinerary)t a local restaurant\n"
            st.markdown("</div>", unsafe_allow_html=True)for each daystination}\n"
            col1, col2 = st.columns(2) morning, afternoon, and evening sectionsr leisure time\n\n"
            with col1:: {[attr['name'] for attr in attractions]}
                st.download_button(nts for lunch and dinner each day from this list: {[rest['name'] for rest in restaurants]}
                    label="📥 Download Itinerary (PDF)",ransportation and logistics
                    data=itinerary,ust activities to match the {budget} budget level += f"- Dinner at a restaurant featuring local cuisine\n"
                    file_name=f"{destination.lower()}_itinerary.md",a brief section at the end with useful travel tips specific to {destination}."- Evening entertainment or relaxation\n\n"
                    mime="text/markdown",
                    use_container_width=True
                )    itinerary = call_gemini_api(prompt)erary += "- Research local transportation options\n"
            with col2:container.empty()heck for any travel advisories\n"
                if st.button("📱 Share via Email", use_container_width=True):
                    st.info("Email sharing will be available in the next update!")nalized travel itinerary is ready!")
        
        with tabs[1]:️ Attractions", "🍽️ Restaurants", "🌤️ Weather", "📊 Trip Summary"])
            st.subheader(f"🏨 Hotels in {destination}")
            for hotel in hotels:
                st.markdown(f"**{hotel['name']}** - {hotel['rating']}")    st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown(f"Price: {hotel['price']} per night")der(f"🗺️ Your AI-Generated {destination} Travel Itinerary")
                st.markdown(f"Amenities: {', '.join(hotel['amenities'])}")
                st.divider()llow_html=True)
        
        with tabs[2]:
            st.subheader(f"🏛️ Attractions in {destination}")button(ession_state:
            for attraction in attractions:            label="📥 Download Itinerary (PDF)",default_destination = st.session_state.destination
                st.markdown(f"**{attraction['name']}** - {attraction['rating']}")ata=itinerary,
                st.markdown(f"{attraction['description']}")
                st.divider() Dates", "2025-06-15 to 2025-06-20")
        rue, 
        with tabs[3]:dget", "Mid-range", "Luxury"], 
            st.subheader(f"🍽️ {cuisine} Restaurants in {destination}")
            for restaurant in restaurants:"📱 Share via Email", use_container_width=True):help="Select your budget level for accommodations and activities")
                cols = st.columns([1, 4]) in the next update!")
                with cols[0]:
                    st.image(restaurant.get("image", "https://cdn-icons-png.flaticon.com/512/2922/2922037.png"), width=100)
                with cols[1]:
                    st.markdown(f"### {restaurant['name']}")
                    st.markdown(f"<span class='rating'>{restaurant['rating']}</span> • <span>{restaurant['price']}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Specialty:** {restaurant['specialty']}")ht")enture", "shopping"],
                    st.markdown(f"**Address:** {restaurant['address']}")f"Amenities: {', '.join(hotel['amenities'])}")"history"],
                    food_url = f"https://www.opentable.com/s?covers=2&dateTime=2025-06-15T19%3A00&metroId=72&term={urllib.parse.quote(restaurant['name'])}"        st.divider()help="Choose activities that interest you the most"
                    st.markdown(f"<a href='{food_url}' target='_blank' class='booking-btn'>Reserve Table</a>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.divider(){destination}")
        
        with tabs[4]:ting']}")value=3)
            st.subheader(f"🌤️ Weather Forecast for {destination}")
            weather_df = pd.DataFrame(weather)
            weather_df['Date'] = pd.date_range(start=datetime.now(), periods=len(weather))
            weather_df['Date'] = weather_df['Date'].dt.strftime('%b %d')with tabs[3]:expander("🏨 Available Hotels"):
            st.bar_chart(data=weather_df, x='Date', y=['high_temp', 'low_temp'], use_container_width=True)der(f"🍽️ {cuisine} Restaurants in {destination}")tels(destination, budget)
            for day in weather:
                st.markdown(f"**Day {day['day']}**: {day['condition']} - High: {day['high_temp']}°C, Low: {day['low_temp']}°C")
        , unsafe_allow_html=True)
        with tabs[5]:.image(restaurant.get("image", "https://cdn-icons-png.flaticon.com/512/2922/2922037.png"), width=100)
            st.subheader("Your Trip at a Glance")
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)s='rating'>{restaurant['rating']}</span> • <span>{restaurant['price']}</span>", unsafe_allow_html=True)
            with col1:
                st.markdown("#### 📍 Destination")* {restaurant['address']}")
                st.markdown(f"<h2 style='margin-top:-10px'>{destination}</h2>", unsafe_allow_html=True)arse.quote(restaurant['name'])}"
                st.markdown("#### 📅 Dates")e)
                st.markdown(f"<p style='margin-top:-10px'>{travel_dates}</p>", unsafe_allow_html=True)kdown("</div>", unsafe_allow_html=True)
                st.markdown("#### 💰 Budget")
                budget_class = "budget-low" if budget=="Budget" else "budget-mid" if budget=="Mid-range" else "budget-high"
                st.markdown(f"<p style='margin-top:-10px'><span class='{budget_class}'>{budget}</span></p>", unsafe_allow_html=True)
            with col2:
                st.markdown("#### 🌡️ Expected Weather")
                st.markdown(f"<p style='margin-top:-10px'>{weather[0]['condition']} {weather[0].get('icon','')} - High: {weather[0]['high_temp']}°C / Low: {weather[0]['low_temp']}°C</p>", unsafe_allow_html=True)
                st.markdown("#### 🏨 Hotel Option")rftime('%b %d')LACEHOLDER", travel_dates.split(" to ")[0] if " to " in travel_dates else "2025-06-15")
                st.markdown(f"<p style='margin-top:-10px'>{hotels[0]['name']} ({hotels[0]['rating']})</p>", unsafe_allow_html=True)high_temp', 'low_temp'], use_container_width=True)='_blank' class='booking-btn'>Book on MakeMyTrip</a>", unsafe_allow_html=True)
                st.markdown("#### 🍽️ Cuisine")
                st.markdown(f"<p style='margin-top:-10px'>{cuisine}</p>", unsafe_allow_html=True)ay {day['day']}**: {day['condition']} - High: {day['high_temp']}°C, Low: {day['low_temp']}°C")afe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("### 🧳 Suggested Packing List")
            packing_cols = st.columns(3)
            with packing_cols[0]: unsafe_allow_html=True)
                st.markdown("#### Essentials")
                st.markdown("- Passport & ID")ype="primary", use_container_width=True)
                st.markdown("- Travel insurance") 📍 Destination")
                st.markdown("- Credit cards")gin-top:-10px'>{destination}</h2>", unsafe_allow_html=True)
                st.markdown("- Phone & charger")
                st.markdown("- Medications")>{travel_dates}</p>", unsafe_allow_html=True)l dates.")
            with packing_cols[1]:
                st.markdown("#### Clothing")" else "budget-mid" if budget=="Mid-range" else "budget-high"
                if any(w['high_temp'] > 25 for w in weather):<span class='{budget_class}'>{budget}</span></p>", unsafe_allow_html=True)
                    st.markdown("- Light summer clothes")
                    st.markdown("- Sun hat & sunglasses")rkdown("#### 🌡️ Expected Weather")xt = st.empty()
                elif any(w['low_temp'] < 10 for w in weather):p:-10px'>{weather[0]['condition']} {weather[0].get('icon','')} - High: {weather[0]['high_temp']}°C / Low: {weather[0]['low_temp']}°C</p>", unsafe_allow_html=True)
                    st.markdown("- Warm jackets & layers")")
                    st.markdown("- Hat & gloves")rating']})</p>", unsafe_allow_html=True)
                else:
                    st.markdown("- Light layers")style='margin-top:-10px'>{cuisine}</p>", unsafe_allow_html=True)(destination, budget)
                    st.markdown("- Light jacket")ml=True)
                if any(w['condition'] in ['Light Rain', 'Thunderstorms'] for w in weather):
                    st.markdown("- Umbrella & raincoat")
            with packing_cols[2]:nterests...")
                st.markdown("#### For this Trip")
                if "culture" in interests or "history" in interests:")destination, interests_str)
                    st.markdown("- Comfortable walking shoes")
                    st.markdown("- Camera & memory cards")
                    st.markdown("- Travel guidebook")nd weather forecast
                if "adventure" in interests: local restaurants...")
                    st.markdown("- Hiking shoes")
                    st.markdown("- Water bottle")
                    st.markdown("- Small backpack")h_temp'] > 25 for w in weather):eather(destination, travel_dates)
                if "beach" in interests_str.lower():
                    st.markdown("- Swimwear & beach towel")
            st.markdown("### 💵 Estimated Budget Breakdown")
            budget_values = {       st.markdown("- Warm jackets & layers")tatus_text.info("✨ Step 4/4: Creating your personalized itinerary with AI...")
                "Budget": {"Accommodation": "$30-50", "Food": "$20-40", "Activities": "$10-30", "Transportation": "$5-15"},
                "Mid-range": {"Accommodation": "$100-150", "Food": "$40-80", "Activities": "$30-70", "Transportation": "$15-30"},
                "Luxury": {"Accommodation": "$300-500", "Food": "$80-150", "Activities": "$70-150", "Transportation": "$30-100"}
            }
            budget_data = budget_values.get(budget, budget_values["Mid-range"])
            budget_df = pd.DataFrame([
                {"Category": "Accommodation", "Cost": int(budget_data["Accommodation"].split("-")[1].replace("$", ""))},th packing_cols[2]:Interests: {interests_str}
                {"Category": "Food", "Cost": int(budget_data["Food"].split("-")[1].replace("$", ""))},
                {"Category": "Activities", "Cost": int(budget_data["Activities"].split("-")[1].replace("$", ""))},nterests:
                {"Category": "Transportation", "Cost": int(budget_data["Transportation"].split("-")[1].replace("$", ""))}
            ])
            st.bar_chart(budget_df, x="Category", y="Cost", use_container_width=True)
            st.markdown("#### Daily Expenses (estimated):")
            st.markdown(f"- **Accommodation:** {budget_data['Accommodation']} per night")            st.markdown("- Hiking shoes")    - Recommend specific restaurants for lunch and dinner each day from this list: {[rest['name'] for rest in restaurants]}
            st.markdown(f"- **Food:** {budget_data['Food']} per day")kdown("- Water bottle")tical tips about transportation and logistics
            st.markdown(f"- **Activities:** {budget_data['Activities']} per day")
            st.markdown(f"- **Transportation:** {budget_data['Transportation']} per day")
        
        st.markdown("---")
        st.markdown("<h3 style='text-align:center'>🏨 Find More Hotels on MakeMyTrip</h3>", unsafe_allow_html=True)
        start_date = travel_dates.split(" to ")[0] if " to " in travel_dates else "2025-06-15"odation": "$30-50", "Food": "$20-40", "Activities": "$10-30", "Transportation": "$5-15"},ty()
        end_date = travel_dates.split(" to ")[1] if " to " in travel_dates else "2025-06-20"range": {"Accommodation": "$100-150", "Food": "$40-80", "Activities": "$30-70", "Transportation": "$15-30"},
        encoded_destination = urllib.parse.quote(destination)Accommodation": "$300-500", "Food": "$80-150", "Activities": "$70-150", "Transportation": "$30-100"}ersonalized travel itinerary is ready!")
        makemytrip_url = f"https://www.makemytrip.com/hotels/hotel-listing/?checkin={start_date}&checkout={end_date}&city={encoded_destination}&roomStayQualifier=2e0e&locusId=CTMY&locusType=city"
        cols = st.columns([1,2,1])
        with cols[1]:
            st.markdown(f"""tegory": "Accommodation", "Cost": int(budget_data["Accommodation"].split("-")[1].replace("$", ""))},:
            <div style='text-align:center'>Category": "Food", "Cost": int(budget_data["Food"].split("-")[1].replace("$", ""))},kdown("<div class='card'>", unsafe_allow_html=True)
                <a href='{makemytrip_url}' target='_blank' style='display: inline-block; background-color: #0066CC; color: white; padding: 12px 20px; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px auto;'>", "Cost": int(budget_data["Activities"].split("-")[1].replace("$", ""))},enerated {destination} Travel Itinerary")
                    Search Hotels on MakeMyTrip        {"Category": "Transportation", "Cost": int(budget_data["Transportation"].split("-")[1].replace("$", ""))}    st.markdown(itinerary)
                </a>
            </div>idth=True)
            """, unsafe_allow_html=True)
        t_data['Accommodation']} per night")
        st.markdown("<div class='footer'>", unsafe_allow_html=True)            st.markdown(f"- **Food:** {budget_data['Food']} per day")                    label="📥 Download Itinerary (PDF)",




        st.markdown("</div>", unsafe_allow_html=True)        st.markdown("<p style='font-size: 0.8rem; color: #666;'>Icons provided by Flaticon. Weather data is simulated.</p>", unsafe_allow_html=True)        st.markdown("Created with ❤️ using Streamlit and Google Gemini AI")























        st.markdown("</div>", unsafe_allow_html=True)        st.markdown("<p style='font-size: 0.8rem; color: #666;'>Icons provided by Flaticon. Weather data is simulated.</p>", unsafe_allow_html=True)        st.markdown("Created with ❤️ using Streamlit and Google Gemini AI")        st.markdown("<div class='footer'>", unsafe_allow_html=True)                    """, unsafe_allow_html=True)            </div>                </a>                    Search Hotels on MakeMyTrip                <a href='{makemytrip_url}' target='_blank' style='display: inline-block; background-color: #0066CC; color: white; padding: 12px 20px; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px auto;'>            <div style='text-align:center'>            st.markdown(f"""        with cols[1]:        cols = st.columns([1,2,1])        makemytrip_url = f"https://www.makemytrip.com/hotels/hotel-listing/?checkin={start_date}&checkout={end_date}&city={encoded_destination}&roomStayQualifier=2e0e&locusId=CTMY&locusType=city"        encoded_destination = urllib.parse.quote(destination)        end_date = travel_dates.split(" to ")[1] if " to " in travel_dates else "2025-06-20"        start_date = travel_dates.split(" to ")[0] if " to " in travel_dates else "2025-06-15"        st.markdown("<h3 style='text-align:center'>🏨 Find More Hotels on MakeMyTrip</h3>", unsafe_allow_html=True)        st.markdown("---")                    st.markdown(f"- **Transportation:** {budget_data['Transportation']} per day")            st.markdown(f"- **Activities:** {budget_data['Activities']} per day")                    data=itinerary,
                    file_name=f"{destination.lower()}_itinerary.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            with col2:
                if st.button("📱 Share via Email", use_container_width=True):
                    st.info("Email sharing will be available in the next update!")
        
        with tabs[1]:
            st.subheader(f"🏨 Hotels in {destination}")
            for hotel in hotels:
                st.markdown(f"**{hotel['name']}** - {hotel['rating']}")
                st.markdown(f"Price: {hotel['price']} per night")
                st.markdown(f"Amenities: {', '.join(hotel['amenities'])}")
                st.divider()
        
        with tabs[2]:
            st.subheader(f"🏛️ Attractions in {destination}")
            for attraction in attractions:
                st.markdown(f"**{attraction['name']}** - {attraction['rating']}")
                st.markdown(f"{attraction['description']}")
                st.divider()
        
        with tabs[3]:
            st.subheader(f"🍽️ {cuisine} Restaurants in {destination}")
            for restaurant in restaurants:
                cols = st.columns([1, 4])
                with cols[0]:
                    st.image(restaurant.get("image", "https://cdn-icons-png.flaticon.com/512/2922/2922037.png"), width=100)
                with cols[1]:
                    st.markdown(f"### {restaurant['name']}")
                    st.markdown(f"<span class='rating'>{restaurant['rating']}</span> • <span>{restaurant['price']}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Specialty:** {restaurant['specialty']}")
                    st.markdown(f"**Address:** {restaurant['address']}")
                    food_url = f"https://www.opentable.com/s?covers=2&dateTime=2025-06-15T19%3A00&metroId=72&term={urllib.parse.quote(restaurant['name'])}"
                    st.markdown(f"<a href='{food_url}' target='_blank' class='booking-btn'>Reserve Table</a>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                st.divider()
        
        with tabs[4]:
            st.subheader(f"🌤️ Weather Forecast for {destination}")
            weather_df = pd.DataFrame(weather)
            weather_df['Date'] = pd.date_range(start=datetime.now(), periods=len(weather))
            weather_df['Date'] = weather_df['Date'].dt.strftime('%b %d')
            st.bar_chart(data=weather_df, x='Date', y=['high_temp', 'low_temp'], use_container_width=True)
            for day in weather:
                st.markdown(f"**Day {day['day']}**: {day['condition']} - High: {day['high_temp']}°C, Low: {day['low_temp']}°C")
        
        with tabs[5]:
            st.subheader("Your Trip at a Glance")
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 📍 Destination")
                st.markdown(f"<h2 style='margin-top:-10px'>{destination}</h2>", unsafe_allow_html=True)
                st.markdown("#### 📅 Dates")
                st.markdown(f"<p style='margin-top:-10px'>{travel_dates}</p>", unsafe_allow_html=True)
                st.markdown("#### 💰 Budget")
                budget_class = "budget-low" if budget=="Budget" else "budget-mid" if budget=="Mid-range" else "budget-high"
                st.markdown(f"<p style='margin-top:-10px'><span class='{budget_class}'>{budget}</span></p>", unsafe_allow_html=True)
            with col2:
                st.markdown("#### 🌡️ Expected Weather")
                st.markdown(f"<p style='margin-top:-10px'>{weather[0]['condition']} {weather[0].get('icon','')} - High: {weather[0]['high_temp']}°C / Low: {weather[0]['low_temp']}°C</p>", unsafe_allow_html=True)
                st.markdown("#### 🏨 Hotel Option")
                st.markdown(f"<p style='margin-top:-10px'>{hotels[0]['name']} ({hotels[0]['rating']})</p>", unsafe_allow_html=True)
                st.markdown("#### 🍽️ Cuisine")
                st.markdown(f"<p style='margin-top:-10px'>{cuisine}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("### 🧳 Suggested Packing List")
            packing_cols = st.columns(3)
            with packing_cols[0]:
                st.markdown("#### Essentials")
                st.markdown("- Passport & ID")
                st.markdown("- Travel insurance")
                st.markdown("- Credit cards")
                st.markdown("- Phone & charger")
                st.markdown("- Medications")
            with packing_cols[1]:
                st.markdown("#### Clothing")
                if any(w['high_temp'] > 25 for w in weather):
                    st.markdown("- Light summer clothes")
                    st.markdown("- Sun hat & sunglasses")
                elif any(w['low_temp'] < 10 for w in weather):
                    st.markdown("- Warm jackets & layers")
                    st.markdown("- Hat & gloves")
                else:
                    st.markdown("- Light layers")
                    st.markdown("- Light jacket")
                if any(w['condition'] in ['Light Rain', 'Thunderstorms'] for w in weather):
                    st.markdown("- Umbrella & raincoat")
            with packing_cols[2]:
                st.markdown("#### For this Trip")
                if "culture" in interests or "history" in interests:
                    st.markdown("- Comfortable walking shoes")
                    st.markdown("- Camera & memory cards")
                    st.markdown("- Travel guidebook")
                if "adventure" in interests:
                    st.markdown("- Hiking shoes")
                    st.markdown("- Water bottle")
                    st.markdown("- Small backpack")
                if "beach" in interests_str.lower():
                    st.markdown("- Swimwear & beach towel")
            st.markdown("### 💵 Estimated Budget Breakdown")
            budget_values = {
                "Budget": {"Accommodation": "$30-50", "Food": "$20-40", "Activities": "$10-30", "Transportation": "$5-15"},
                "Mid-range": {"Accommodation": "$100-150", "Food": "$40-80", "Activities": "$30-70", "Transportation": "$15-30"},
                "Luxury": {"Accommodation": "$300-500", "Food": "$80-150", "Activities": "$70-150", "Transportation": "$30-100"}
            }
            budget_data = budget_values.get(budget, budget_values["Mid-range"])
            budget_df = pd.DataFrame([
                {"Category": "Accommodation", "Cost": int(budget_data["Accommodation"].split("-")[1].replace("$", ""))},
                {"Category": "Food", "Cost": int(budget_data["Food"].split("-")[1].replace("$", ""))},
                {"Category": "Activities", "Cost": int(budget_data["Activities"].split("-")[1].replace("$", ""))},
                {"Category": "Transportation", "Cost": int(budget_data["Transportation"].split("-")[1].replace("$", ""))}
            ])
            st.bar_chart(budget_df, x="Category", y="Cost", use_container_width=True)
            st.markdown("#### Daily Expenses (estimated):")
            st.markdown(f"- **Accommodation:** {budget_data['Accommodation']} per night")
            st.markdown(f"- **Food:** {budget_data['Food']} per day")
            st.markdown(f"- **Activities:** {budget_data['Activities']} per day")
            st.markdown(f"- **Transportation:** {budget_data['Transportation']} per day")
        
        st.markdown("---")
        st.markdown("<h3 style='text-align:center'>🏨 Find More Hotels on MakeMyTrip</h3>", unsafe_allow_html=True)
        start_date = travel_dates.split(" to ")[0] if " to " in travel_dates else "2025-06-15"
        end_date = travel_dates.split(" to ")[1] if " to " in travel_dates else "2025-06-20"
        encoded_destination = urllib.parse.quote(destination)
        makemytrip_url = f"https://www.makemytrip.com/hotels/hotel-listing/?checkin={start_date}&checkout={end_date}&city={encoded_destination}&roomStayQualifier=2e0e&locusId=CTMY&locusType=city"
        cols = st.columns([1,2,1])
        with cols[1]:
            st.markdown(f"""
            <div style='text-align:center'>
                <a href='{makemytrip_url}' target='_blank' style='display: inline-block; background-color: #0066CC; color: white; padding: 12px 20px; text-decoration: none; border-radius: 4px; font-weight: bold; margin: 20px auto;'>
                    Search Hotels on MakeMyTrip
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<div class='footer'>", unsafe_allow_html=True)
        st.markdown("Created with ❤️ using Streamlit and Google Gemini AI")
        st.markdown("<p style='font-size: 0.8rem; color: #666;'>Icons provided by Flaticon. Weather data is simulated.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
