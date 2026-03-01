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
                    <div className="glass-card enhanced-timeline-content" style={{ padding: 40, position: 'relative', overflow: 'hidden' }}>
                        <div style={{ position: 'absolute', top: 0, left: 0, width: '4px', height: '100%', background: 'var(--gradient-main)' }} />
                        <Markdown>{dest.itinerary}</Markdown>
                    </div>
                </div>
            ))}
        </div>
    );
}
