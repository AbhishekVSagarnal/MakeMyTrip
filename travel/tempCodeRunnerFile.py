import streamlit as st
import requests

# Set API Key (Replace with your actual Gemini API key)
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText"

# Simulated API functions (Replace with real APIs later)
def fetch_hotels(destination, budget):
    return [{"name": "Budget Inn", "price": 60}, {"name": "Luxury Stay", "price": 200}]

def fetch_attractions(destination, interests):
    return [{"name": "Historical Museum", "type": "Culture"}, {"name": "Beachside", "type": "Nature"}]

def fetch_restaurants(destination, cuisine):
    return [{"name": "Local Diner", "type": cuisine}, {"name": "Fine Dining", "type": cuisine}]

# Call Google Gemini API
def call_gemini_api(prompt):
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    payload = {"prompt": prompt, "max_tokens": 500}

    response = requests.post(GEMINI_URL, json=payload, headers=headers, params=params)
    return response.json().get("generated_text", "Itinerary generation failed.") if response.status_code == 200 else "Error fetching data"

# Streamlit UI
st.title("✈️ AI Travel Itinerary Planner")
st.subheader("Generate a personalized travel itinerary with AI!")

# User inputs
destination = st.text_input("Enter Destination", "Paris")
travel_dates = st.text_input("Enter Travel Dates", "2025-06-15 to 2025-06-20")
budget = st.selectbox("Select Budget", ["Budget", "Mid-range", "Luxury"])
interests = st.text_area("Enter Interests (e.g., culture, adventure, food)", "Culture, History")
cuisine = st.text_input("Preferred Cuisine", "French")

# Generate Itinerary Button
if st.button("Generate Itinerary"):
    # Fetch travel details
    hotels = fetch_hotels(destination, budget)
    attractions = fetch_attractions(destination, interests)
    restaurants = fetch_restaurants(destination, cuisine)

    # Construct AI prompt
    prompt = f"""
    Generate a structured 3-day travel itinerary for {destination} from {travel_dates}.
    - Interests: {interests}
    - Budget: {budget}
    - Hotels: {hotels}
    - Attractions: {attractions}
    - Restaurants: {restaurants}
    Provide a breakdown for morning, afternoon, and evening activities.
    """

    # Call AI model
    itinerary = call_gemini_api(prompt)

    # Display itinerary
    st.subheader("🗺️ Your AI-Generated Travel Itinerary")
    st.write(itinerary)
