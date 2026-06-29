import json
import os

# This path is relative to where you RUN the script from (the backend/ folder)
TRENDS_FOLDER = "mock_data/trends"


def load_all_mock_trends():
    """Loads every trend JSON file in mock_data/trends and returns them as a list of dicts."""
    trends = []
    for filename in os.listdir(TRENDS_FOLDER):
        if filename.endswith(".json"):
            with open(f"{TRENDS_FOLDER}/{filename}") as f:
                trends.append(json.load(f))
    return trends


def load_trend_by_id(trend_id: str):
    """Loads a single trend by its id, e.g. 'trend_001'. Returns None if not found."""
    path = f"{TRENDS_FOLDER}/{trend_id}.json"
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None


if __name__ == "__main__":
    # Quick self-test when you run: python trend_loader.py
    all_trends = load_all_mock_trends()
    print(f"Loaded {len(all_trends)} trends:\n")
    for t in all_trends:
        print(f"  {t['id']} -> {t['trend_name']}")

    print("\nTesting load_trend_by_id('trend_003'):")
    print(load_trend_by_id("trend_003"))
