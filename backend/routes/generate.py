from fastapi import APIRouter
from services.ad_generator import generate_ad_copy_cached
router = APIRouter()

# Temporary mock data — Vishakha's real trend JSONs will replace this later
MOCK_TREND = {
    "trend_name": "POV its Monday morning",
    "audio": "Espresso - Sabrina Carpenter",
    "hashtags": ["#MondayMood", "#CoffeeTime", "#Aesthetic"],
    "description": "People doing their morning routine in a dreamy slow-mo style",
    "engagement_score": 9.2,
    "region": "IN",
    "vertical_tags": ["food", "lifestyle", "wellness"]
}

MOCK_BUSINESS = {
    "name": "Brew & Co",
    "product": "Specialty coffee",
    "target_audience": "Young professionals aged 22-32",
    "tone": "Warm, aspirational, slightly witty",
    "city": "Ahmedabad"
}


@router.post("/generate-ad")
def generate_ad(business_name: str, trend_id: str):
    result = generate_ad_copy_cached(MOCK_TREND, MOCK_BUSINESS)
    return result