export default function HotelCard({ hotel, travelDates }) {
    const bookingUrl = hotel.booking_url?.replace('PLACEHOLDER', travelDates || '2025-06-15') || '#';

    return (
        <div className="glass-card hotel-card animate-fade-in-up">
            <div className="hotel-info">
                <h3>{hotel.name}</h3>
                <div className="hotel-meta">
                    <span className="hotel-price">${hotel.price}<small>/night</small></span>
                    <span className="hotel-rating">★ {hotel.rating}</span>
                </div>
                <div className="amenities">
                    {hotel.amenities?.map((a, i) => (
                        <span key={i} className="amenity-tag">{a}</span>
                    ))}
                </div>
                <a href={bookingUrl} target="_blank" rel="noopener noreferrer" className="btn-booking" style={{ marginTop: 8 }}>
                    Book on MakeMyTrip →
                </a>
            </div>
        </div>
    );
}
