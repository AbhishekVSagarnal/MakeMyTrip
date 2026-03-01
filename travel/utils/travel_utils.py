import random
import datetime

def fetch_hotels(city, budget):
    # Simulated hotel data
    prices = {"Budget": 50, "Mid-range": 150, "Luxury": 400}
    base_price = prices.get(budget, 150)
    return [
        {"name": f"{city} {budget} Hotel 1", "rating": "4.2", "price": base_price + random.randint(-20, 20), "amenities": ["WiFi", "Breakfast"]},
        {"name": f"{city} {budget} Hotel 2", "rating": "4.5", "price": base_price + random.randint(0, 50), "amenities": ["Pool", "Gym"]}
    ]

def fetch_attractions(city, interests):
    return [
        {"name": f"{city} Central Museum", "rating": "4.8", "description": "A must visit historical place.", "price": "15$"},
        {"name": f"{city} Cultural Park", "rating": "4.5", "description": "Beautiful scenery and local culture.", "price": "Free"}
    ]

def fetch_restaurants(city, cuisine):
    return [
        {"name": f"The {cuisine} Spot in {city}", "rating": "4.7", "specialty": f"Authentic {cuisine}", "address": "Downtown", "price": "$$"},
        {"name": f"{city} {cuisine} Fine Dining", "rating": "4.9", "specialty": "Chef's special", "address": "Uptown", "price": "$$$"}
    ]

def fetch_weather(city, date_range_str):
    return [
        {"day": 1, "condition": "Sunny", "high_temp": 25, "low_temp": 15, "icon": "☀️"},
        {"day": 2, "condition": "Partly Cloudy", "high_temp": 22, "low_temp": 14, "icon": "⛅"}
    ]

def generate_fallback_itinerary(city, days, interests):
    return f"Fallback itinerary for {city} for {days} days, focusing on {interests}."

def create_transit_suggestions(city):
    return f"We suggest using the public metro system in {city}. It is reliable and cheap!"

def compute_trip_cost(budget, days_per_city, travelers):
    daily = {"Budget": 100, "Mid-range": 250, "Luxury": 600}
    return daily.get(budget, 250) * days_per_city * travelers
