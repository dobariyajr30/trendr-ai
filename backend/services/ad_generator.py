from google import genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_ad_copy(trend: dict, business: dict) -> dict:
    prompt = f"""
You are an expert social media ad copywriter.

A business wants to create an Instagram Reel ad that rides a current viral trend.

TRENDING CONTENT:
- Trend: {trend['trend_name']}
- Audio: {trend['audio']}
- Hashtags: {', '.join(trend['hashtags'])}
- Vibe: {trend['description']}
- Engagement Score: {trend['engagement_score']}/10

BUSINESS:
- Name: {business['name']}
- Product: {business['product']}
- Target Audience: {business['target_audience']}
- Tone: {business['tone']}
- Location: {business['city']}

Generate a complete Instagram Reel ad.
Respond ONLY in this exact JSON format, no extra text:
{{
  "headline": "...",
  "reel_script": "...",
  "caption": "...",
  "cta": "...",
  "hashtags": ["...", "...", "..."]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.replace("json", "", 1).strip()

    return json.loads(raw_text)




import hashlib


def get_cache_key(trend: dict, business: dict) -> str:
    combo = f"{trend['trend_name']}-{business['name']}"
    return hashlib.md5(combo.encode()).hexdigest()


def generate_ad_copy_cached(trend: dict, business: dict) -> dict:
    cache_key = f"cache/{get_cache_key(trend, business)}.json"

    if os.path.exists(cache_key):
        with open(cache_key) as f:
            return json.load(f)

    result = generate_ad_copy(trend, business)

    os.makedirs("cache", exist_ok=True)
    with open(cache_key, "w") as f:
        json.dump(result, f)

    return result