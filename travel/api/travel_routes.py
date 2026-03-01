"""FastAPI routes for the AI Travel Planner."""
import os
import random
import time
import urllib.parse
import datetime as dt
from fastapi import APIRouter
from google import genai
from google.genai import types
from dotenv import load_dotenv
from .models import TripRequest, HotelQuery, AttractionQuery, RestaurantQuery, WeatherQuery, CostQuery, CityQuery

load_dotenv()
router = APIRouter(prefix="/api/travel", tags=["travel"])

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------------------------------------------------------------------------
# City coordinate data for maps
# ---------------------------------------------------------------------------
CITY_COORDS = {
    "Paris": (48.8566, 2.3522), "Rome": (41.9028, 12.4964),
    "Berlin": (52.5200, 13.4050), "New York": (40.7128, -74.0060),
    "Tokyo": (35.6762, 139.6503), "London": (51.5074, -0.1278),
    "Sydney": (-33.8688, 151.2093), "Dubai": (25.2048, 55.2708),
    "Bangkok": (13.7563, 100.5018), "Singapore": (1.3521, 103.8198),
    "Barcelona": (41.3874, 2.1686), "Istanbul": (41.0082, 28.9784),
    "Mumbai": (19.0760, 72.8777), "Bangalore": (12.9716, 77.5946),
    "Delhi": (28.7041, 77.1025), "Goa": (15.2993, 74.1240),
}

# ---------------------------------------------------------------------------
# Hotel data
# ---------------------------------------------------------------------------
HOTEL_DATABASE = {
    "Paris": {
        "Budget":    ["Ibis Paris Montmartre", "Generator Paris"],
        "Mid-range": ["Hôtel Plaza Athénée", "Le Pavillon de la Reine"],
        "Luxury":    ["Four Seasons Hotel George V", "The Ritz Paris"],
    },
    "Rome": {
        "Budget":    ["Hotel Centro Roma", "Generator Rome"],
        "Mid-range": ["Hotel Artemide", "Palazzo Naiadi"],
        "Luxury":    ["Hotel de Russie", "Villa Spalletti Trivelli"],
    },
    "Tokyo": {
        "Budget":    ["Hotel Gracery Shinjuku", "Sakura Hotel Ikebukuro"],
        "Mid-range": ["Park Hotel Tokyo", "The Prince Gallery Tokyo"],
        "Luxury":    ["Aman Tokyo", "Hoshinoya Tokyo"],
    },
    "New York": {
        "Budget":    ["Pod 51 Hotel", "Hotel 31"],
        "Mid-range": ["The Beekman", "Ace Hotel New York"],
        "Luxury":    ["The Plaza", "The St. Regis New York"],
    },
    "London": {
        "Budget":    ["Point A Hotel London", "Hub by Premier Inn"],
        "Mid-range": ["The Hoxton Holborn", "Citizen M Tower"],
        "Luxury":    ["The Savoy", "Claridge's"],
    },
}

PRICE_RANGES = {
    "Budget":    {"min": 30,  "max": 80},
    "Mid-range": {"min": 100, "max": 250},
    "Luxury":    {"min": 300, "max": 1000},
}

AMENITY_POOL = [
    "Free WiFi", "Breakfast Included", "Fitness Center",
    "Pool", "Spa", "Room Service", "Airport Shuttle",
    "Concierge", "Parking", "Restaurant", "Bar",
]


# ---------------------------------------------------------------------------
# Attraction data
# ---------------------------------------------------------------------------
ATTRACTIONS = {
    "culture": [
        {"name": "{city} Historical Museum", "rating": "4.5★",
         "description": "Explore the rich history of the region with interactive exhibits", "price": "$15"},
        {"name": "{city} Art Gallery", "rating": "4.3★",
         "description": "Contemporary and classic art exhibitions from renowned artists", "price": "$12"},
    ],
    "history": [
        {"name": "Ancient Ruins of {city}", "rating": "4.7★",
         "description": "Well-preserved ruins dating back centuries with guided tours available", "price": "$20"},
        {"name": "{city} Historical Quarter", "rating": "4.4★",
         "description": "Walk through the streets of the old town with beautiful architecture", "price": "Free"},
    ],
    "food": [
        {"name": "{city} Food Market", "rating": "4.6★",
         "description": "Bustling local market with fresh produce and street food stalls", "price": "Free"},
        {"name": "{city} Culinary Experience", "rating": "4.8★",
         "description": "Hands-on cooking classes with local chefs", "price": "$45"},
    ],
    "nature": [
        {"name": "{city} Botanical Gardens", "rating": "4.5★",
         "description": "Lush gardens with rare plant species and walking trails", "price": "$8"},
        {"name": "{city} National Park", "rating": "4.9★",
         "description": "Stunning natural landscapes with hiking and wildlife viewing", "price": "$10"},
    ],
    "adventure": [
        {"name": "{city} Adventure Park", "rating": "4.4★",
         "description": "Zip-lining, rock climbing, and outdoor adventures", "price": "$35"},
        {"name": "{city} Water Sports Center", "rating": "4.3★",
         "description": "Kayaking, surfing, and more water-based activities", "price": "$30"},
    ],
    "shopping": [
        {"name": "{city} Grand Bazaar", "rating": "4.2★",
         "description": "Traditional market with artisan crafts and souvenirs", "price": "Free"},
        {"name": "{city} Designer District", "rating": "4.1★",
         "description": "High-end fashion boutiques and luxury brands", "price": "Free"},
    ],
}


# ---------------------------------------------------------------------------
# Helper: Call Gemini API
# ---------------------------------------------------------------------------
def _call_gemini(prompt: str) -> str:
    api_key = GEMINI_API_KEY
    if not api_key:
        return "⚠️ API Key missing. Set GEMINI_API_KEY in .env."
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7, top_p=0.9, top_k=40,
                candidate_count=1, max_output_tokens=4096,
            ),
        )
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {e}"


def _fallback_itinerary(city: str, days: int, interests: list[str]) -> str:
    lines = [f"# 🗺️ Your {days}-Day {city} Itinerary\n"]
    for d in range(1, days + 1):
        lines.append(f"## Day {d}\n")
        lines.append("### Morning\n- Breakfast at your hotel\n- Explore local attractions\n")
        lines.append("### Afternoon\n- Enjoy lunch at a local restaurant\n- Continue sightseeing\n")
        lines.append("### Evening\n- Dinner at a recommended restaurant\n- Evening entertainment\n")
    return "\n".join(lines)


# ============================= ROUTES =====================================

@router.post("/generate")
async def generate_itinerary(req: TripRequest):
    """Generate a full multi-city AI-powered itinerary."""
    results = []
    trip_start = dt.datetime.strptime(req.start_date, "%Y-%m-%d")

    for idx, city in enumerate(req.destinations):
        city_start = trip_start + dt.timedelta(days=req.days_per_city * idx)
        city_end = city_start + dt.timedelta(days=req.days_per_city)
        date_range = f"{city_start.strftime('%Y-%m-%d')} to {city_end.strftime('%Y-%m-%d')}"

        departure_info = f"Departing from {req.source}" if idx == 0 else f"Traveling from {req.destinations[idx - 1]}"

        prompt = f"""
{departure_info} to {city}.
Create a detailed {req.days_per_city}-day travel itinerary for {city} from {date_range}.

TRAVELER PREFERENCES:
- Interests: {', '.join(req.interests)}
- Budget level: {req.budget}
- Cuisine preference: {req.cuisine}

FORMAT INSTRUCTIONS:
- Format using Markdown with headings like ## Day 1, ## Day 2, etc.
- For each day include Morning, Afternoon, and Evening sections
- Include 2-3 specific attractions per day
- Recommend specific restaurants for lunch and dinner
- Include practical tips about transportation and logistics
- Adjust activities to match the {req.budget} budget level
- Include a brief section at the end with useful travel tips specific to {city}
"""
        itinerary_text = _call_gemini(prompt)
        if "⚠️" in itinerary_text:
            itinerary_text = _fallback_itinerary(city, req.days_per_city, req.interests)

        coords = CITY_COORDS.get(city, (48.8566, 2.3522))
        results.append({
            "city": city,
            "dates": date_range,
            "itinerary": itinerary_text,
            "lat": coords[0],
            "lng": coords[1],
        })

    return {"destinations": results}


@router.post("/hotels")
async def get_hotels(q: HotelQuery):
    price_range = PRICE_RANGES.get(q.budget, PRICE_RANGES["Mid-range"])
    hotel_names = HOTEL_DATABASE.get(q.destination, {}).get(q.budget, [
        f"{q.destination} {q.budget} Hotel", f"{q.budget} Inn {q.destination}",
    ])

    encoded = urllib.parse.quote(q.destination)
    booking_base = f"https://www.makemytrip.com/hotels/hotel-listing/?checkin=2025-06-15&city={encoded}"

    hotels = []
    for name in hotel_names:
        hotels.append({
            "name": name,
            "price": random.randint(price_range["min"], price_range["max"]),
            "rating": round(random.uniform(3.5, 5.0), 1),
            "amenities": random.sample(AMENITY_POOL, k=random.randint(3, 6)),
            "booking_url": f"{booking_base}&price={price_range['min']}-{price_range['max']}",
        })

    return {"hotels": hotels}


@router.post("/attractions")
async def get_attractions(q: AttractionQuery):
    result = []
    for interest in q.interests:
        templates = ATTRACTIONS.get(interest.lower(), [])
        for tmpl in templates:
            item = {k: v.replace("{city}", q.destination) if isinstance(v, str) else v for k, v in tmpl.items()}
            result.append(item)

    if not result:
        result = [{"name": f"{q.destination} City Tour", "rating": "4.0★",
                    "description": "See the highlights of the city with an experienced guide", "price": "$25"}]

    return {"attractions": result}


@router.post("/restaurants")
async def get_restaurants(q: RestaurantQuery):
    price_symbols = ["$", "$$", "$$$", "$$$$"]
    restaurants = [
        {"name": f"Local {q.cuisine} Diner in {q.destination}",
         "price": random.choice(price_symbols), "rating": round(random.uniform(3.8, 5.0), 1),
         "specialty": f"Traditional {q.cuisine} classics",
         "address": f"123 Main St, {q.destination}"},
        {"name": f"Authentic {q.cuisine} Experience",
         "price": random.choice(price_symbols), "rating": round(random.uniform(3.8, 5.0), 1),
         "specialty": f"Chef's {q.cuisine} tasting menu",
         "address": f"456 Boulevard, {q.destination}"},
        {"name": f"{q.cuisine} Fusion in {q.destination}",
         "price": random.choice(price_symbols), "rating": round(random.uniform(3.8, 5.0), 1),
         "specialty": f"Modern twist on {q.cuisine} classics",
         "address": f"789 Food Street, {q.destination}"},
    ]
    return {"restaurants": restaurants}


@router.post("/weather")
async def get_weather(q: WeatherQuery):
    temp_ranges = {
        "Paris": (15, 25), "Rome": (18, 30), "Tokyo": (15, 28),
        "New York": (10, 25), "London": (12, 20), "Sydney": (18, 28),
        "Dubai": (25, 42), "Bangkok": (26, 35), "Singapore": (24, 32),
    }
    conditions = [
        {"condition": "Sunny", "icon": "☀️"},
        {"condition": "Partly Cloudy", "icon": "⛅"},
        {"condition": "Cloudy", "icon": "☁️"},
        {"condition": "Light Rain", "icon": "🌦️"},
        {"condition": "Clear", "icon": "✨"},
    ]
    low, high = temp_ranges.get(q.destination, (15, 25))
    forecast = []
    for i in range(5):
        w = random.choice(conditions)
        forecast.append({
            "day": i + 1, "condition": w["condition"], "icon": w["icon"],
            "high_temp": random.randint(low, high),
            "low_temp": random.randint(low - 5, low + 3),
            "humidity": random.randint(40, 90),
        })
    return {"forecast": forecast}


@router.post("/cost")
async def estimate_cost(q: CostQuery):
    daily_costs = {
        "Budget":    {"Accommodation": 40, "Food": 25, "Activities": 15, "Transportation": 10},
        "Mid-range": {"Accommodation": 120, "Food": 50, "Activities": 40, "Transportation": 20},
        "Luxury":    {"Accommodation": 350, "Food": 100, "Activities": 80, "Transportation": 40},
    }
    selected = daily_costs.get(q.budget, daily_costs["Mid-range"])
    breakdown = {k: v * q.days * q.travelers for k, v in selected.items()}
    breakdown["total"] = sum(breakdown.values())
    breakdown["daily_per_person"] = sum(selected.values())
    return {"cost": breakdown, "budget": q.budget, "days": q.days, "travelers": q.travelers}


@router.post("/transit")
async def get_transit(q: CityQuery):
    # Simulated transit suggestions
    transit_options = [
        {"type": "Metro/Subway", "description": f"The local metro in {q.destination} is the fastest way to get around the city center.", "cost_estimate": "$2-4 per ride"},
        {"type": "Bus", "description": "Extensive bus networks cover areas the metro doesn't reach. Great for sightseeing.", "cost_estimate": "$1.50-3 per ride"},
        {"type": "Taxi/Rideshare", "description": "Available everywhere. Useful for late-night travel or airport transfers.", "cost_estimate": "Moderate to High"},
    ]
    return {"suggestions": transit_options}


@router.post("/packing")
async def get_packing(q: CityQuery):
    # Basic simulated packing list
    essentials = ["Passport & ID", "Travel insurance documents", "Universal power adapter", "Comfortable walking shoes"]
    clothing = ["Layered clothing", "Light jacket", "Evening wear for dinners", "Swimwear (if applicable)"]
    toiletries = ["Toothbrush & paste", "Sunscreen (SPF 30+)", "Basic first-aid kit", "Deodorant & Skincare"]
    
    return {
        "packing_list": {
            "Essentials": essentials,
            "Clothing": clothing,
            "Toiletries": toiletries
        }
    }
