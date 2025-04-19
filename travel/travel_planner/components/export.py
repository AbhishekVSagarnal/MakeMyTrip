# components/export.py
import streamlit as st

def export_itinerary(itinerary, destination):
    st.download_button(
        label="📥 Download Itinerary (PDF)",
        data=itinerary,
        file_name=f"{destination.lower()}_itinerary.md",
        mime="text/markdown",
        use_container_width=True
    )
