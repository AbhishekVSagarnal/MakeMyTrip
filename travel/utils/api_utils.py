import streamlit as st
import google.generativeai as genai
from .travel_utils import generate_fallback_itinerary

def call_gemini_api(prompt: str) -> str:
    """
    Call the Gemini API to generate text based on the prompt.
    Returns the API's response text or fallback itinerary if an error occurs.
    """
    try:
        # If configured in travel_app (set in st.session_state), reuse that key
        gemini_api_key = st.session_state.get("gemini_api_key", None)
        if not gemini_api_key:
            return "⚠️ API Key missing. Provide a Gemini API key to use advanced AI features."

        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT",        "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH",       "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]

        generation_config = genai.types.GenerationConfig(
            temperature=0.7,
            top_p=0.9,
            top_k=40,
            candidate_count=1,
            max_output_tokens=2048
        )

        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        return response.text

    except Exception as e:
        st.error(f"Gemini API Error: {str(e)}")
        # Basic fallback
        return "⚠️ Gemini API Error"