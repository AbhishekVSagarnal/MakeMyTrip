# components/input_form.py
import streamlit as st

def get_user_inputs():
    st.sidebar.header("✈️ AI Travel Planner")
    source = st.sidebar.text_input("🏠 Source Location", "Bangalore")
    destination = st.sidebar.text_input("📍 Destination", "Bagalkote")
    start_date = st.sidebar.date_input("📅 Start Date")
    num_days = st.sidebar.number_input("📆 Number of Days", min_value=1, max_value=30, value=2)
    interests = st.sidebar.text_input("🎭 Interests", "Culture, History, Food")
    budget_level = st.sidebar.selectbox("💰 Budget Level", ["Budget", "Mid-range", "Luxury"])
    cuisine = st.sidebar.text_input("🍽️ Cuisine Preferences", "Local, Italian")
    dietary_restrictions = st.sidebar.text_input("🥗 Dietary Restrictions", "Vegetarian")
    travel_style = st.sidebar.selectbox("🚀 Travel Style", ["Relaxed", "Fast-paced", "Family-friendly"])
    attractions = st.sidebar.text_area("🏛️ Attractions (comma separated)", "Eiffel Tower, Louvre Museum, Notre-Dame")
    restaurants = st.sidebar.text_area("🍴 Restaurants (comma separated)", "Le Meurice, L'Ambroisie")

    if st.sidebar.button("Generate Itinerary"):
        attractions_list = [item.strip() for item in attractions.split(",") if item.strip()]
        restaurants_list = [item.strip() for item in restaurants.split(",") if item.strip()]
        return source, destination, start_date, num_days, interests, budget_level, cuisine, dietary_restrictions, travel_style, attractions_list, restaurants_list
    return None
