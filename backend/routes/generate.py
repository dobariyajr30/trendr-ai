from fastapi import APIRouter

router = APIRouter()


@router.post("/generate-ad")
def generate_ad(business_name: str, trend_id: str):
    return {
        "status": "coming soon"
    }