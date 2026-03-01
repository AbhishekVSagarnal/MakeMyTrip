const ALL_INTERESTS = ['culture', 'history', 'food', 'nature', 'adventure', 'shopping'];
const INTEREST_EMOJIS = { culture: '🎭', history: '🏛️', food: '🍜', nature: '🌿', adventure: '⛰️', shopping: '🛍️' };

export default function TripForm({ form, setForm, onSubmit, loading }) {
    const toggleInterest = (interest) => {
        setForm(prev => ({
            ...prev,
            interests: prev.interests.includes(interest)
                ? prev.interests.filter(i => i !== interest)
                : [...prev.interests, interest],
        }));
    };

    return (
        <section className="section">
            <div className="app-container">
                <h2 className="section-title"><span className="emoji">🗺️</span> Plan Your Trip</h2>
                <form className="trip-form" onSubmit={e => { e.preventDefault(); onSubmit(); }}>
                    <div className="glass-card animate-fade-in-up">
                        <div className="form-group">
                            <label>🔹 Source City</label>
                            <input value={form.source} onChange={e => setForm(p => ({ ...p, source: e.target.value }))} placeholder="New York" />
                        </div>
                        <div className="form-group" style={{ marginTop: 16 }}>
                            <label>🔹 Destinations (comma-separated)</label>
                            <input value={form.destinations} onChange={e => setForm(p => ({ ...p, destinations: e.target.value }))} placeholder="Paris, Rome, Berlin" />
                        </div>
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginTop: 16 }}>
                            <div className="form-group">
                                <label>📅 Start Date</label>
                                <input type="date" value={form.start_date} onChange={e => setForm(p => ({ ...p, start_date: e.target.value }))} />
                            </div>
                            <div className="form-group">
                                <label>📆 Days per City</label>
                                <input type="number" min={1} max={14} value={form.days_per_city} onChange={e => setForm(p => ({ ...p, days_per_city: +e.target.value }))} />
                            </div>
                        </div>
                    </div>

                    <div className="glass-card animate-fade-in-up" style={{ animationDelay: '0.1s' }}>
                        <div className="form-group">
                            <label>💰 Budget Level</label>
                            <select value={form.budget} onChange={e => setForm(p => ({ ...p, budget: e.target.value }))}>
                                <option>Budget</option>
                                <option>Mid-range</option>
                                <option>Luxury</option>
                            </select>
                        </div>
                        <div className="form-group" style={{ marginTop: 16 }}>
                            <label>🍽️ Cuisine Preference</label>
                            <input value={form.cuisine} onChange={e => setForm(p => ({ ...p, cuisine: e.target.value }))} placeholder="Local" />
                        </div>
                        <div className="form-group" style={{ marginTop: 16 }}>
                            <label>🎯 Interests</label>
                            <div className="interests-grid">
                                {ALL_INTERESTS.map(i => (
                                    <button key={i} type="button" className={`interest-pill ${form.interests.includes(i) ? 'active' : ''}`}
                                        onClick={() => toggleInterest(i)}>
                                        {INTEREST_EMOJIS[i]} {i}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </div>

                    <div style={{ gridColumn: '1 / -1', textAlign: 'center', marginTop: 8 }}>
                        <button type="submit" className="btn-primary" disabled={loading}>
                            {loading ? '✨ Generating...' : '🗺️ Generate My Perfect Itinerary'}
                        </button>
                    </div>
                </form>
            </div>
        </section>
    );
}
