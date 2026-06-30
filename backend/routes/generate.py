from fastapi import APIRouter
from services.ad_generator import generate_ad_copy_cached
from services.trend_loader import load_trend_by_id

router = APIRouter()

MOCK_BUSINESS = {
    "name": "Brew & Co",
    "product": "Specialty coffee",
    "target_audience": "Young professionals aged 22-32",
    "tone": "Warm, aspirational, slightly witty",
    "city": "Ahmedabad"
}


@router.post("/generate-ad")
def generate_ad(business_name: str, trend_id: str):
    trend = load_trend_by_id(trend_id)
    if trend is None:
        return {"error": f"Trend '{trend_id}' not found"}

    result = generate_ad_copy_cached(trend, MOCK_BUSINESS)
    return result