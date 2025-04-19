# app.py
import streamlit as st
import re
from components.input_form import get_user_inputs
from services.itinerary_service import generate_itinerary
from services.cost_estimator import estimate_cost
from services.image_service import get_relevant_image
from components.export import export_itinerary

st.set_page_config(page_title="AI-Powered Travel Planner", layout="wide")

# Custom CSS for a beautiful timeline roadmap with curved connectors
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
        color: #1E88E5;
    }
    .timeline {
        position: relative;
        margin: 20px 0;
        padding-left: 50px;
    }
    .timeline::before {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        left: 25px;
        width: 2px;
        background: #1E88E5;
    }
    .day-card {
        background: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 40px;
        position: relative;
    }
    .day-card::before {
        content: "";
        position: absolute;
        top: 20px;
        left: -37px;
        width: 20px;
        height: 20px;
        background: #1E88E5;
        border-radius: 50%;
    }
    .svg-curve {
        display: block;
        margin: -20px auto 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI-Powered Travel Planner")

def display_roadmap(itinerary, destination):
    # Split itinerary by "## Day" headings (the AI prompt outputs "## Day 1", etc.)
    days = itinerary.split("## Day")
    if len(days) <= 1:
        st.markdown(itinerary, unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown("<div class='timeline'>", unsafe_allow_html=True)
            for i, day_text in enumerate(days[1:], start=1):
                st.markdown("<div class='day-card'>", unsafe_allow_html=True)
                st.markdown(f"<h3>Day {i}</h3>", unsafe_allow_html=True)
                # First, try to extract an image URL from the day's text
                image_match = re.search(r'!\[.*?\]\((.*?)\)', day_text)
                if image_match:
                    image_url = image_match.group(1)
                else:
                    # If no image is found, call the image service for a relevant image
                    query = f"Day {i} itinerary {destination}"
                    image_url = get_relevant_image(query)
                    if not image_url:
                        image_url = f"https://via.placeholder.com/800x400?text=Day+{i}+Image"
                st.image(image_url, use_column_width=True)
                # Remove any image markdown from the day's text
                day_text_clean = re.sub(r'!\[.*?\]\(.*?\)', '', day_text)
                st.markdown(day_text_clean, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                # Add a curved SVG connector between days
                if i < len(days) - 0:
                    st.markdown("""
                    <svg class="svg-curve" width="50" height="60">
                        <path d="M25 0 C10 30, 40 30, 25 60" stroke="#1E88E5" stroke-width="2" fill="none" />
                    </svg>
                    """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# Get user inputs
inputs = get_user_inputs()

if inputs:
    (source, destination, start_date, num_days, interests, budget_level, cuisine,
     dietary_restrictions, travel_style, attractions, restaurants) = inputs

    st.info(f"🗺️ Generating a {num_days}-day itinerary from {source} to {destination} starting on {start_date}...")
    
    # Generate the itinerary using Gemini API
    itinerary = generate_itinerary(source, destination, start_date, num_days, interests, budget_level, cuisine, dietary_restrictions, travel_style, attractions, restaurants)
    
    # Estimate trip cost
    cost_breakdown = estimate_cost(budget_level, num_days)
    
    # Display results using tabs
    tabs = st.tabs(["📝 Itinerary", "📊 Cost Breakdown", "🛣️ Roadmap", "📥 Export"])
    
    with tabs[0]:
        st.subheader(f"Your AI-Generated Itinerary for {destination}")
        st.markdown(itinerary, unsafe_allow_html=True)
    
    with tabs[1]:
        st.subheader("Estimated Trip Cost Breakdown")
        st.json(cost_breakdown)
    
    with tabs[2]:
        st.subheader("Trip Roadmap")
        display_roadmap(itinerary, destination)
    
    with tabs[3]:
        st.subheader("Export Your Itinerary")
        export_itinerary(itinerary, destination)
