import os
import requests
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




def return_strava_data():
    auth = get_access_token()
    endpoint = f"{BASE_URL}/athlete/activities"

    headers = {
        "Authorization": f"Bearer {auth}"
    }
    params = {
        "after": int(datetime.now() - timedelta(days=14).timestamp()),
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if not response.ok:
        print(f"API returned {response.status_code}: {response.text}")
        response.raise_for_status()


    activities = response.json()
    return activities