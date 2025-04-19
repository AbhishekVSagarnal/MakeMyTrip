# services/cost_estimator.py
def estimate_cost(budget_level, num_days):
    cost_map = {
        "Budget": {"Accommodation": 30, "Food": 20, "Activities": 10, "Transportation": 5},
        "Mid-range": {"Accommodation": 100, "Food": 40, "Activities": 30, "Transportation": 15},
        "Luxury": {"Accommodation": 300, "Food": 80, "Activities": 70, "Transportation": 30}
    }
    
    selected = cost_map.get(budget_level, cost_map["Mid-range"])
    daily_cost = sum(selected.values())
    total_cost = daily_cost * num_days
    breakdown = {k: v * num_days for k, v in selected.items()}
    breakdown["Total"] = total_cost
    return breakdown
