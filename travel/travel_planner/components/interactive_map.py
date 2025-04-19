import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
from config.settings import MAPBOX_API_KEY

def get_lat_lon(destination):
    """ Get latitude and longitude from Mapbox API """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{destination}.json?access_token={MAPBOX_API_KEY}"
    response = requests.get(url).json()
    
    if response and "features" in response and response["features"]:
        return response["features"][0]["center"][1], response["features"][0]["center"][0]
    return 20.5937, 78.9629  # Default: India

def display_map(destination):
    lat, lon = get_lat_lon(destination)
    m = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=destination).add_to(m)
    folium_static(m)
