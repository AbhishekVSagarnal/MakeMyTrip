export default function CostBreakdown({ data }) {
    if (!data) return null;
    const { cost, budget, days, travelers } = data;
    const categories = ['Accommodation', 'Food', 'Activities', 'Transportation'];

    return (
        <div>
            <div style={{ textAlign: 'center', marginBottom: 20, color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                <strong>{budget}</strong> budget · {days} day(s) · {travelers} traveler(s)
            </div>
            <div className="cost-grid stagger">
                {categories.map((cat, i) => (
                    <div key={cat} className="glass-card cost-item animate-fade-in-up">
                        <span className="cost-label">{['🏠', '🍽️', '🎯', '🚕'][i]} {cat}</span>
                        <span className="cost-value">${cost[cat]}</span>
                    </div>
                ))}
                <div className="cost-total animate-fade-in-up">
                    <div className="amount">${cost.total}</div>
                    <div className="label">Total Estimated Cost</div>
                    <div style={{ color: 'var(--text-muted)', fontSize: '0.8rem', marginTop: 4 }}>
                        ${cost.daily_per_person}/day per person
                    </div>
                </div>
            </div>
        </div>
    );
}
