import streamlit as st
import os
import time
import random
import pandas as pd
import datetime as dt
import urllib.parse
from dotenv import load_dotenv

# Local imports from utils
from utils.api_utils import call_gemini_api
from utils.travel_utils import (
    fetch_hotels, fetch_attractions, fetch_restaurants,
    fetch_weather, generate_fallback_itinerary, 
    create_transit_suggestions, 
    compute_trip_cost
)
from utils.map_utils import create_travel_map, folium_static

# ---------------------------------------------------------------------
# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Streamlit page
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------------
# Sidebar UI
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=120)
    st.markdown("<h2 style='text-align: center;'>AI Travel Assistant</h2>", unsafe_allow_html=True)

    st.info("This app uses Google's Gemini AI to create personalized travel itineraries.")

    with st.expander("🔑 API Configuration"):
        api_key_input = st.text_input("Gemini API Key",
                                      value=GEMINI_API_KEY if GEMINI_API_KEY else "",
                                      type="password",
                                      help="Enter your Gemini API key here")
        if api_key_input:
            GEMINI_API_KEY = api_key_input
            st.session_state.gemini_api_key = GEMINI_API_KEY
            st.success("API key configured successfully!")

    st.markdown("### 📱 Share Your Plan")
    share_email = st.text_input("Email Address", placeholder="Enter email to receive itinerary")
    if st.button("Share Itinerary"):
        # Placeholder for sharing logic
        if share_email:
            st.success(f"Itinerary sent to {share_email} (simulation).")
        else:
            st.warning("Please enter an email address.")

    st.markdown("### 🙏 About")
    st.markdown("Created with ❤️ using Streamlit and Google Gemini AI")
    st.markdown("Version 3.0.0")

# ---------------------------------------------------------------------
# Main Header
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        background: linear-gradient(90deg, #1E88E5, #5E35B1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
    }
    .subheader {
        font-size: 1.8rem;
        color: #5E35B1;
        margin-bottom: 1.2rem;
        text-align: center;
    }
    .card {
        background-color: blue;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 24px;
        border-left: 6px solid #1E88E5;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .booking-btn {
        background-color: blue;
        color: white;
        padding: 8px 16px;
        border-radius: 4px;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
        font-weight: bold;
    }
    .booking-btn:hover {
        background-color: #E64A19;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>✈️ AI Travel Itinerary Planner</div>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Plan the perfect trip across multiple destinations!</p>", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# Inputs for trip details
st.markdown("## 1️⃣ Trip Details")

col1, col2 = st.columns(2)

with col1:
    # 1) Source & Destination (multi-city)
    source_city = st.text_input("🔹 Source Location", "New York")
    multi_destinations_input = st.text_area("🔹 Destination(s)", "Paris\nRome\nBerlin",
        help="Enter each city on a new line if you have multiple destinations.")

    # Parse multiple destinations
    destinations = [d.strip() for d in multi_destinations_input.split("\n") if d.strip()]

    # 2) Trip Start Date & Time
    start_date = st.date_input("🔹 Start Date", dt.date.today() + dt.timedelta(days=30))
    start_time = st.time_input("🔹 Departure Time", dt.time(8, 0))  # 8:00 AM default

with col2:
    # 3) Number of days in each city (simple approach)
    days_per_city = st.number_input("🔹 Days per City", min_value=1, max_value=14, value=3)
    # Budget level
    budget = st.select_slider("🔹 Budget",
                              options=["Budget", "Mid-range", "Luxury"],
                              value="Mid-range")
    # Interests
    interests = st.multiselect(
        "🔹 Interests",
        ["culture", "history", "food", "nature", "adventure", "shopping"],
        default=["culture", "history"]
    )
    cuisine = st.text_input("🔹 Preferred Cuisine", "Local")

# ---------------------------------------------------------------------
# 4) Generate Itinerary
st.markdown("## 2️⃣ Generate Your Itinerary")

if st.button("Generate Multi-Destination Itinerary"):
    if not destinations:
        st.error("Please provide at least one destination.")
    else:
        # For each city, fetch restaurants, attractions, hotels, weather, etc.
        full_itinerary_text = ""
        city_data_list = []

        # Combine date & time for departure
        trip_start_dt = datetime.datetime.combine(start_date, start_time)

        for idx, city in enumerate(destinations):
            st.info(f"Fetching data for **{city}**...")
            with st.spinner(f"Preparing {city} details..."):

                hotels = fetch_hotels(city, budget)
                attractions = fetch_attractions(city, interests)
                restaurants = fetch_restaurants(city, cuisine)

                # Calculate travel dates for each city (basic additive approach)
                city_start_dt = trip_start_dt + datetime.timedelta(days=days_per_city * idx)
                city_end_dt   = city_start_dt + datetime.timedelta(days=days_per_city)
                date_range_str = f"{city_start_dt.strftime('%Y-%m-%d')} to {city_end_dt.strftime('%Y-%m-%d')}"

                # 5) Real-time Weather (simulated)
                weather = fetch_weather(city, date_range_str)

                # AI prompt
                departure_info = f"Departing from {source_city}" if idx == 0 else f"Traveling from {destinations[idx-1]}"
                prompt = f"""
                {departure_info} to {city}.
                Create a {days_per_city}-day itinerary for {city} from {date_range_str}.
                Interests: {', '.join(interests)}.
                Budget: {budget}.
                Cuisine preference: {cuisine}.
                Do not exceed 7 days for each city.
                Include morning, afternoon, evening breakdown, references to these attractions:
                {', '.join([a['name'] for a in attractions])}
                And these restaurants:
                {', '.join([r['name'] for r in restaurants])}
                """

                # 8) AI-powered restaurant recommendations (Gemini)
                city_itinerary = call_gemini_api(prompt)
                if "missing" in city_itinerary.lower():
                    # Fallback
                    city_itinerary = generate_fallback_itinerary(city, days_per_city, interests)

                # Save data for building the final structured output
                city_info = {
                    "city": city,
                    "days": days_per_city,
                    "dates": date_range_str,
                    "hotels": hotels,
                    "attractions": attractions,
                    "restaurants": restaurants,
                    "weather": weather,
                    "itinerary_text": city_itinerary
                }
                city_data_list.append(city_info)
        
        # Combine full itinerary
        for cdata in city_data_list:
            full_itinerary_text += f"\n\n### {cdata['city']} ({cdata['dates']})\n"
            full_itinerary_text += cdata['itinerary_text']
        
        st.success("Multi-destination itinerary generated!")
        # 7) Customizable itinerary - basic editing text area:
        final_itinerary = st.text_area("📝 Your Full Itinerary (editable)", full_itinerary_text, height=300)

        # 9) Share & export
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            st.download_button(
                label="Download Itinerary (Markdown)",
                data=final_itinerary,
                file_name="multi_destination_itinerary.md",
                mime="text/markdown"
            )
        with col_share2:
            if st.button("Email Itinerary"):
                if share_email:
                    st.success(f"Itinerary emailed to {share_email} (simulation).")
                else:
                    st.warning("Please provide an email address in the sidebar.")

        # 10) Trip Cost Estimator
        st.markdown("## 3️⃣ Trip Cost Estimator")
        travelers = st.number_input("Number of Travelers", min_value=1, max_value=10, value=2)
        total_cost_estimate = 0
        
        for cdata in city_data_list:
            city_cost = compute_trip_cost(budget, cdata['days'], travelers)
            total_cost_estimate += city_cost
            st.write(f"Estimated cost in **{cdata['city']}** for {travelers} traveler(s) over {cdata['days']} day(s): **${city_cost}**")

        st.write(f"### Total Estimated Cost for Entire Trip: **${total_cost_estimate}**")

        # 4) Interactive Maps & 6) Transit suggestions
        st.markdown("## 4️⃣ Maps & Transportation")
        for cdata in city_data_list:
            st.subheader(f"Map for {cdata['city']}")
            map_obj = create_travel_map(cdata['city'], cdata['attractions'], cdata['restaurants'])
            folium_static(map_obj, width=700, height=400)

            st.markdown("**Transit Suggestions**")
            transit_text = create_transit_suggestions(cdata['city'])
            st.info(transit_text)

st.markdown("---")
st.markdown("<p style='text-align:center; color: #666;'>© 2025 AI Travel Planner</p>", unsafe_allow_html=True)