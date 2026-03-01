const API_BASE = 'http://localhost:8001/api/travel';

export async function generateItinerary(data) {
    const res = await fetch(`${API_BASE}/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
    return res.json();
}

export async function fetchHotels(destination, budget) {
    const res = await fetch(`${API_BASE}/hotels`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination, budget }),
    });
    return res.json();
}

export async function fetchAttractions(destination, interests) {
    const res = await fetch(`${API_BASE}/attractions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination, interests }),
    });
    return res.json();
}

export async function fetchRestaurants(destination, cuisine) {
    const res = await fetch(`${API_BASE}/restaurants`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination, cuisine }),
    });
    return res.json();
}

export async function fetchWeather(destination) {
    const res = await fetch(`${API_BASE}/weather`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination }),
    });
    return res.json();
}

export async function fetchCost(budget, days, travelers) {
    const res = await fetch(`${API_BASE}/cost`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget, days, travelers }),
    });
    return res.json();
}

export async function fetchTransit(destination) {
    const res = await fetch(`${API_BASE}/transit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination }),
    });
    return res.json();
}

export async function fetchPackingList(destination) {
    const res = await fetch(`${API_BASE}/packing`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ destination }),
    });
    return res.json();
}
