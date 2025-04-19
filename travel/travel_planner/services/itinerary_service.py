import re
import google.generativeai as genai
from config.settings import GEMINI_API_KEY

# Configure Gemini API with your API key
genai.configure(api_key=GEMINI_API_KEY)

def generate_itinerary(source, destination, start_date, num_days, interests, budget_level, cuisine, dietary_restrictions, travel_style, attractions, restaurants):
    """
    Generates a structured travel itinerary using the Gemini API, instructing the model to embed image URLs for each day.
    If a day is missing an image, a default placeholder is added.
    """
    prompt = f"""
Create a detailed {num_days}-day travel itinerary for a trip from {source} to {destination} starting on {start_date}.

**TRAVELER PREFERENCES:**
- 🎭 Interests: {interests}
- 💰 Budget: {budget_level}
- 🍽️ Cuisine Preferences: {cuisine}
- 🥗 Dietary Restrictions: {dietary_restrictions}
- ✈️ Travel Style: {travel_style}

**ITINERARY REQUIREMENTS:**
1. Provide a day-by-day breakdown with headings like "## Day 1", "## Day 2", etc.
2. For each day, include morning, afternoon, and evening activities.
3. Include top attractions from this list: {', '.join(attractions)}.
4. Recommend restaurants for lunch and dinner from this list: {', '.join(restaurants)}.
5. For each day, embed a relevant image using Markdown (e.g., ![Day 1](https://example.com/image.jpg)). Please ensure the image URL comes from a reputable source not wikipedia use some other website .
6. Include direct Google Maps links for each location. For example:  
   📍 [Eiffel Tower](https://www.google.com/maps/search/?api=1&query=Eiffel+Tower)
7. Provide transportation tips, packing lists, budget breakdowns, and emergency info.
8. End with a summary of key tips and estimated costs.

**FORMAT GUIDELINES:**
- Use Markdown for headers, bullet points, and emphasis.
- Ensure each day's section starts with "## Day X".
- Embed a relevant image for each day using Markdown image syntax.
- Enhance visual appeal with emojis.
    """
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response = model.generate_content(prompt)
        itinerary_text = response.text if response.text else "⚠️ Unable to generate itinerary. Please try again."
    except Exception as e:
        itinerary_text = f"⚠️ Error: {str(e)}"

    # Post-process the itinerary text: Ensure each day includes an image.
    day_sections = re.split(r"(## Day \d+)", itinerary_text)
    final_itinerary = ""
    # day_sections may have an intro part, then pairs of heading and content.
    for i in range(1, len(day_sections), 2):
        heading = day_sections[i]  # e.g., "## Day 1"
        content = day_sections[i+1] if (i+1) < len(day_sections) else ""
        # If no image is embedded in this section, add a default placeholder.
        if not re.search(r'!\[.*?\]\(.*?\)', content):
            placeholder = f"https://via.placeholder.com/800x400?text=Day+{((i+1)//2)}+Image"
            content = f"![Day {((i+1)//2)} Image]({placeholder})\n\n" + content
        final_itinerary += heading + content
    return final_itinerary
