import Markdown from 'react-markdown';

export default function ItineraryTimeline({ destinations }) {
    if (!destinations?.length) return null;

    return (
        <div>
            {destinations.map((dest, dIdx) => (
                <div key={dIdx} className="animate-fade-in-up" style={{ marginBottom: 48, animationDelay: `${dIdx * 0.15}s` }}>
                    <h3 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.4rem', marginBottom: 8 }}>
                        📍 {dest.city}
                    </h3>
                    <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: 20 }}>
                        {dest.dates}
                    </p>
                    <div className="glass-card itinerary-content" style={{ padding: 28 }}>
                        <Markdown>{dest.itinerary}</Markdown>
                    </div>
                </div>
            ))}
        </div>
    );
}
