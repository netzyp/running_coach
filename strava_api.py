import os
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.strava.com/api/v3"

def get_access_token():
    """Refreshes the access token using the refresh token from .env"""
    response = requests.post(
        "https://www.strava.com/oauth/token",
        data={
            'client_id': os.getenv('STRAVA_CLIENT_ID'),
            'client_secret': os.getenv('STRAVA_CLIENT_SECRET'),
            'refresh_token': os.getenv('STRAVA_REFRESH_TOKEN'),
            'grant_type': 'refresh_token'
        }
    )
    response.raise_for_status()
    return response.json()['access_token']

endpoint = f"{BASE_URL}/athlete/activities"

headers = {
    "Authorization": f"Bearer {get_access_token()}"
}


params = {
    "per_page": 5,
    "page": 1
}


response = requests.get(endpoint, headers=headers, params=params)


if not response.ok:
    print(f"API returned {response.status_code}: {response.text}")
response.raise_for_status()


activities = response.json()
print(json.dumps(activities, indent=2))