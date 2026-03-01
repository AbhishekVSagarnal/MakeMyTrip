import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

// Fix leaflet default marker icons
import L from 'leaflet';
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png',
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png',
});

export default function TravelMap({ destinations }) {
    if (!destinations?.length) return null;

    const center = [destinations[0].lat || 48.85, destinations[0].lng || 2.35];

    return (
        <div className="map-container">
            <MapContainer center={center} zoom={4} style={{ height: '100%', width: '100%' }}>
                <TileLayer
                    attribution='&copy; <a href="https://carto.com/">CARTO</a>'
                    url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
                />
                {destinations.map((d, i) => (
                    <Marker key={i} position={[d.lat || 48.85, d.lng || 2.35]}>
                        <Popup>
                            <strong>{d.city}</strong><br />{d.dates}
                        </Popup>
                    </Marker>
                ))}
            </MapContainer>
        </div>
    );
}
