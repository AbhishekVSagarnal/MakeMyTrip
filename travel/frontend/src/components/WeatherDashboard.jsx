export default function WeatherDashboard({ forecast }) {
    if (!forecast?.length) return null;

    return (
        <div className="weather-grid stagger">
            {forecast.map((day, i) => (
                <div key={i} className="glass-card weather-card animate-fade-in-up">
                    <div className="weather-icon">{day.icon}</div>
                    <div style={{ fontWeight: 600, fontSize: '0.9rem' }}>Day {day.day}</div>
                    <div className="weather-condition">{day.condition}</div>
                    <div className="weather-temps">
                        <span className="temp-high">{day.high_temp}°C</span>
                        <span className="temp-low">{day.low_temp}°C</span>
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 4 }}>
                        💧 {day.humidity}%
                    </div>
                </div>
            ))}
        </div>
    );
}
