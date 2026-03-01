# ✈️ MakeMyTrip AI Travel Planner


An AI-powered travel planning companion that generates personalized itineraries based on your interests, budget, and travel dates. Includes integrated mock integrations with real hotel/restaurant booking logic and custom generative models.

## 📌 Architecture Setup

This project is now fully decoupled from the root Agentic webhook logic. The Travel Planner can be run in two separate modes:

1. **Option 1: Streamlit Dashboard**
   A fast, interactive, strictly Python AI travel assistant UI.
2. **Option 2: Modern React App + FastAPI Backend**
   A polished frontend React experience integrated with a custom FastAPI backend.

---

## 🛠️ How to Run

Before running either option, ensure your `.env` file at the root correctly sets:
```env
GEMINI_API_KEY=your_google_genai_key
```

### Option A: Streamlit App
If you'd like a quick, pure-Python dashboard UI.

```bash
cd MakeMyTrip/travel
streamlit run travel_app.py
```
This will launch the application locally at `http://localhost:8501`.

### Option B: React Frontend + FastAPI Backend
If you prefer running the decoupled modern web-app.

**1. Start the API Backend**
The backend handles GenAI prompt resolution and API serving. Currently running on port `8001` to avoid conflicting with the root Webhook Agent.
```bash
cd MakeMyTrip/travel
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

**2. Start the React Frontend**
Open a new terminal session.
```bash
cd MakeMyTrip/travel/frontend
npm install
npm run dev
```
Access the application on `http://localhost:5173`.

---

## 🚀 Key Features
- **Generative AI Responses:** Leverages Google Gemini `gemini-2.5-flash` natively.
- **Folium Interactive Maps:** Visualizes destinations directly.
- **Cost Estimation:** Generates dynamic pricing metrics based on chosen dates, budget, and duration.
- **Dynamic Weather Forecasting:** Basic integration for high/low temps in target locations.
