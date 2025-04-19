import folium
from streamlit_folium import folium_static
import random

def create_travel_map(city: str, attractions: list, restaurants: list):
    """
    Create an interactive Folium map showing local attractions and restaurants.
    Coordinates are simulated or guessed for demonstration.
    """
    # Fake city center coordinates
    city_coords = {
        "Paris": (48.8566, 2.3522),
        "Rome": (41.9028, 12.4964),
        "Berlin": (52.5200, 13.4050),
        "New York": (40.7128, -74.0060),
        "Tokyo": (35.6762, 139.6503)
    }
    default_coords = (48.8566, 2.3522)  # Paris fallback
    lat, lon = city_coords.get(city, default_coords)
    
    m = folium.Map(location=[lat, lon], zoom_start=11)
    
    # Add attractions
    for a in attractions:
        lat_offset = random.uniform(-0.02, 0.02)
        lon_offset = random.uniform(-0.02, 0.02)
        folium.Marker(
            location=[lat + lat_offset, lon + lon_offset],
            popup=a["name"],
            tooltip=a["name"],
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
    
    # Add restaurants
    for r in restaurants:
        lat_offset = random.uniform(-0.02, 0.02)
        lon_offset = random.uniform(-0.02, 0.02)
        folium.Marker(
            location=[lat + lat_offset, lon + lon_offset],
            popup=r["name"],
            tooltip=r["name"],
            icon=folium.Icon(color="green", icon="cutlery")
        ).add_to(m)
    
    return m