import React, { useState } from 'react';
import './index.css';
import HeroSection from './components/HeroSection';
import TripForm from './components/TripForm';
import ProgressStepper from './components/ProgressStepper';
import ItineraryTimeline from './components/ItineraryTimeline';
import HotelCard from './components/HotelCard';
import WeatherDashboard from './components/WeatherDashboard';
import CostBreakdown from './components/CostBreakdown';
import TravelMap from './components/TravelMap';
import ThemeToggle from './components/ThemeToggle';
import { generateItinerary, fetchHotels, fetchAttractions, fetchRestaurants, fetchWeather, fetchCost, fetchTransit, fetchPackingList } from './api';

const today = new Date();
const defaultDate = new Date(today.getTime() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0];

export default function App() {
    const [form, setForm] = useState({
        source: 'New York',
        destinations: 'Paris, Rome',
        start_date: defaultDate,
        days_per_city: 3,
        budget: 'Mid-range',
        interests: ['culture', 'history'],
        cuisine: 'Local',
    });

    const [theme, setTheme] = React.useState('dark');

    React.useEffect(() => {
        document.documentElement.setAttribute('data-theme', theme);
    }, [theme]);

    const toggleTheme = () => setTheme(prev => prev === 'dark' ? 'light' : 'dark');

    const [loading, setLoading] = useState(false);
    const [step, setStep] = useState(-1);
    const [results, setResults] = useState(null);
    const [activeTab, setActiveTab] = useState('itinerary');

    const handleGenerate = async () => {
        const dests = form.destinations.split(',').map(d => d.trim()).filter(Boolean);
        if (!dests.length) return;

        setLoading(true);
        setResults(null);
        setStep(0);

        try {
            // Step 1: Hotels
            const allHotels = [];
            for (const city of dests) {
                const h = await fetchHotels(city, form.budget);
                allHotels.push({ city, hotels: h.hotels });
            }
            setStep(1);

            // Step 2: Attractions
            const allAttractions = [];
            for (const city of dests) {
                const a = await fetchAttractions(city, form.interests);
                allAttractions.push({ city, attractions: a.attractions });
            }
            setStep(2);

            // Step 3: Restaurants + Weather + Transit + Packing
            const allRestaurants = [];
            const allWeather = [];
            const allTransit = [];
            const allPacking = [];
            for (const city of dests) {
                const r = await fetchRestaurants(city, form.cuisine);
                allRestaurants.push({ city, restaurants: r.restaurants });
                const w = await fetchWeather(city);
                allWeather.push({ city, forecast: w.forecast });
                const t = await fetchTransit(city);
                allTransit.push({ city, suggestions: t.suggestions });
                const p = await fetchPackingList(city);
                allPacking.push({ city, packing_list: p.packing_list });
            }
            setStep(3);

            // Step 4: AI Itinerary
            const itinData = await generateItinerary({
                source: form.source,
                destinations: dests,
                start_date: form.start_date,
                days_per_city: form.days_per_city,
                budget: form.budget,
                interests: form.interests,
                cuisine: form.cuisine,
            });

            // Cost
            const costData = await fetchCost(form.budget, form.days_per_city * dests.length, 1);

            setResults({
                destinations: itinData.destinations,
                hotels: allHotels,
                attractions: allAttractions,
                restaurants: allRestaurants,
                weather: allWeather,
                transit: allTransit,
                packing: allPacking,
                cost: costData,
            });
            setStep(4);
        } catch (err) {
            console.error('Error generating itinerary:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleDownload = () => {
        if (!results) return;
        let content = `# AI Travel Itinerary\n\n`;
        results.destinations.forEach(d => {
            content += `## ${d.city} (${d.dates})\n\n`;
            content += `${d.itinerary}\n\n---\n\n`;
        });
        content += `\n### Estimated Total Cost: $${results.cost.total}\n`;
        const blob = new Blob([content], { type: 'text/markdown' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'MyItinerary.md';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    };

    const TABS = [
        { id: 'itinerary', label: '📝 Itinerary' },
        { id: 'hotels', label: '🏨 Hotels' },
        { id: 'attractions', label: '🏛️ Attractions' },
        { id: 'restaurants', label: '🍽️ Restaurants' },
        { id: 'weather', label: '🌤️ Weather' },
        { id: 'map', label: '🗺️ Map' },
        { id: 'transit', label: '🚇 Transit' },
        { id: 'packing', label: '🎒 Packing List' },
        { id: 'cost', label: '💰 Budget' },
    ];

    return (
        <div>
            <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
            <HeroSection />
            <TripForm form={form} setForm={setForm} onSubmit={handleGenerate} loading={loading} />

            {(loading || step >= 0) && (
                <div className="app-container">
                    <ProgressStepper currentStep={step} />
                </div>
            )}

            {loading && (
                <div className="loader-overlay">
                    <div className="loader-spinner" />
                    <div className="loader-text">
                        {step === 0 && '🏨 Finding the best hotels...'}
                        {step === 1 && '🏛️ Discovering attractions...'}
                        {step === 2 && '🍽️ Fetching restaurants & weather...'}
                        {step === 3 && '✨ Creating your personalized itinerary with AI...'}
                    </div>
                </div>
            )}

            {results && !loading && (
                <div className="app-container section animate-fade-in">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', marginBottom: '20px' }}>
                        <div className="tabs" style={{ marginBottom: 0 }}>
                            {TABS.map(t => (
                                <button key={t.id} className={`tab-btn ${activeTab === t.id ? 'active' : ''}`}
                                    onClick={() => setActiveTab(t.id)}>
                                    {t.label}
                                </button>
                            ))}
                        </div>
                        <button onClick={handleDownload} className="btn-primary" style={{ padding: '10px 16px', fontSize: '0.9rem' }}>
                            💾 Download Markdown
                        </button>
                    </div>

                    {activeTab === 'itinerary' && (
                        <ItineraryTimeline destinations={results.destinations} />
                    )}

                    {activeTab === 'hotels' && (
                        <div className="stagger">
                            {results.hotels.map((cityH, ci) => (
                                <div key={ci} style={{ marginBottom: 32 }}>
                                    <h3 style={{ fontFamily: 'var(--font-heading)', marginBottom: 16 }}>
                                        📍 Hotels in {cityH.city}
                                    </h3>
                                    {cityH.hotels.map((hotel, hi) => (
                                        <HotelCard key={hi} hotel={hotel} travelDates={form.start_date} />
                                    ))}
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'attractions' && (
                        <div className="stagger">
                            {results.attractions.map((cityA, ci) => (
                                <div key={ci} style={{ marginBottom: 32 }}>
                                    <h3 style={{ fontFamily: 'var(--font-heading)', marginBottom: 16 }}>
                                        📍 Attractions in {cityA.city}
                                    </h3>
                                    {cityA.attractions.map((attr, ai) => (
                                        <div key={ai} className="glass-card attraction-card animate-fade-in-up"
                                            style={{ marginBottom: 12, animationDelay: `${ai * 0.08}s` }}>
                                            <h3>{attr.name}</h3>
                                            <div className="attraction-meta">
                                                <span className="rating">★ {attr.rating}</span>
                                                <span className="price">{attr.price}</span>
                                            </div>
                                            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>{attr.description}</p>
                                        </div>
                                    ))}
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'restaurants' && (
                        <div className="stagger">
                            {results.restaurants.map((cityR, ci) => (
                                <div key={ci} style={{ marginBottom: 32 }}>
                                    <h3 style={{ fontFamily: 'var(--font-heading)', marginBottom: 16 }}>
                                        📍 Restaurants in {cityR.city}
                                    </h3>
                                    {cityR.restaurants.map((rest, ri) => (
                                        <div key={ri} className="glass-card restaurant-card animate-fade-in-up"
                                            style={{ marginBottom: 12, animationDelay: `${ri * 0.08}s` }}>
                                            <div className="restaurant-info">
                                                <h3>{rest.name}</h3>
                                                <div className="restaurant-meta">
                                                    <span className="rating">★ {rest.rating}</span>
                                                    <span>{rest.price}</span>
                                                    <span>📍 {rest.address}</span>
                                                </div>
                                                <div className="restaurant-specialty">{rest.specialty}</div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'weather' && (
                        <div className="stagger">
                            {results.weather.map((cityW, ci) => (
                                <div key={ci} style={{ marginBottom: 32 }}>
                                    <h3 style={{ fontFamily: 'var(--font-heading)', marginBottom: 16 }}>
                                        🌤️ Weather in {cityW.city}
                                    </h3>
                                    <WeatherDashboard forecast={cityW.forecast} />
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'map' && (
                        <TravelMap destinations={results.destinations} />
                    )}

                    {activeTab === 'transit' && (
                        <div className="stagger">
                            {results.transit.map((cityT, ci) => (
                                <div key={ci} style={{ marginBottom: 32 }}>
                                    <h3 style={{ fontFamily: 'var(--font-heading)', marginBottom: 16 }}>
                                        🚇 Transit in {cityT.city}
                                    </h3>
                                    {cityT.suggestions.map((sug, si) => (
                                        <div key={si} className="glass-card animate-fade-in-up" style={{ marginBottom: 12, animationDelay: `${si * 0.08}s` }}>
                                            <h4>{sug.type}</h4>
                                            <p>{sug.description}</p>
                                            <div style={{ color: 'var(--brand)', fontWeight: 'bold' }}>{sug.cost_estimate}</div>
                                        </div>
                                    ))}
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'packing' && (
                        <div className="stagger">
                            {results.packing.map((cityP, ci) => (
                                <div key={ci} style={{ marginBottom: 32 }}>
                                    <h3 style={{ fontFamily: 'var(--font-heading)', marginBottom: 16 }}>
                                        🎒 Packing List for {cityP.city}
                                    </h3>
                                    <div className="glass-card animate-fade-in-up" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px' }}>
                                        {Object.entries(cityP.packing_list).map(([cat, items], idx) => (
                                            <div key={idx}>
                                                <h4 style={{ color: 'var(--primary)', marginBottom: '8px' }}>{cat}</h4>
                                                <ul style={{ paddingLeft: '20px', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
                                                    {items.map((item, i) => <li key={i}>{item}</li>)}
                                                </ul>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}

                    {activeTab === 'cost' && (
                        <CostBreakdown data={results.cost} />
                    )}

                    {/* MakeMyTrip CTA */}
                    <div className="cta-banner animate-fade-in-up">
                        <h2>🏨 Find More Hotels on MakeMyTrip</h2>
                        <a
                            href={`https://www.makemytrip.com/hotels/hotel-listing/?checkin=${form.start_date}&city=${encodeURIComponent(form.destinations.split(',')[0]?.trim())}`}
                            target="_blank" rel="noopener noreferrer"
                            className="btn-primary" style={{ display: 'inline-block', marginTop: 8, textDecoration: 'none' }}>
                            Search Hotels on MakeMyTrip →
                        </a>
                    </div>
                </div>
            )}

            <footer className="footer">
                <p>© 2025 AI Travel Planner · Powered by Google Gemini AI & MakeMyTrip</p>
            </footer>
        </div>
    );
}
