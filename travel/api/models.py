"""Pydantic models for the Travel Planner API."""
from pydantic import BaseModel, Field
from typing import Optional


class TripRequest(BaseModel):
    """Request model for generating a travel itinerary."""
    source: str = Field(..., description="Source/departure city")
    destinations: list[str] = Field(..., description="List of destination cities")
    start_date: str = Field(..., description="Trip start date (YYYY-MM-DD)")
    days_per_city: int = Field(3, ge=1, le=14, description="Number of days in each city")
    budget: str = Field("Mid-range", description="Budget level: Budget, Mid-range, or Luxury")
    interests: list[str] = Field(default_factory=lambda: ["culture", "history"])
    cuisine: str = Field("Local", description="Preferred cuisine type")


class HotelQuery(BaseModel):
    destination: str
    budget: str = "Mid-range"


class AttractionQuery(BaseModel):
    destination: str
    interests: list[str] = ["culture"]


class RestaurantQuery(BaseModel):
    destination: str
    cuisine: str = "Local"


class WeatherQuery(BaseModel):
    destination: str
    date_range: str = ""


class CostQuery(BaseModel):
    budget: str = "Mid-range"
    days: int = 3
    travelers: int = 1


class CityQuery(BaseModel):
    destination: str
