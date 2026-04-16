# Running Coach

A Streamlit dashboard that pulls your Strava data and lets you ask a Gemini-powered AI coach questions about your training.

## What it does

- Fetches your last 14 days of runs from Strava
- Displays charts for pace, distance, heart rate, and heart rate vs pace
- Sidebar chat lets you ask questions about your runs (powered by Gemini 2.0 Flash)
- Answers are grounded in both your recent run data and a hardcoded training plan

## Prerequisites

- Python 3.10+
- A [Strava API app](https://www.strava.com/settings/api) (free)
- A [Google Gemini API key](https://aistudio.google.com/app/apikey) (free)

## Setup

### 1. Clone and install dependencies

```bash
git clone <repo-url>
cd running_coach
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Create a Strava API app

1. Go to [strava.com/settings/api](https://www.strava.com/settings/api) and create an app
2. Set **Authorization Callback Domain** to `localhost` (required even for local use)
3. Note your **Client ID** and **Client Secret**

### 3. Get a Strava refresh token

The app uses the OAuth refresh token flow — you need a long-lived refresh token with `activity:read_all` scope.

The easiest way is [strava-token-generator](https://github.com/nicholasmello/strava-token-generator):

```bash
pip install stravalib
# or use the web tool at https://www.strava.com/oauth/authorize
```

Alternatively, follow Strava's [Getting Started guide](https://developers.strava.com/docs/getting-started/) to complete the OAuth flow manually and capture the `refresh_token` from the token exchange response.

### 4. Get a Gemini API key

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Create an API key — the free tier is sufficient

### 5. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```
STRAVA_CLIENT_ID=your_client_id
STRAVA_CLIENT_SECRET=your_client_secret
STRAVA_REFRESH_TOKEN=your_refresh_token
GEMINI_API_KEY=your_gemini_api_key
```

### 6. Run the app

```bash
streamlit run app.py
```

## Project structure

```
running_coach/
├── app.py          # Streamlit UI and charts
├── strava_api.py   # Strava API client (fetches last 14 days of activities)
├── parser.py       # Parses raw Strava data into run stats
├── context.py      # Builds the LLM prompt — includes a hardcoded training plan
├── llm.py          # Gemini API wrapper
└── requirements.txt
```

## Notes

- **Training plan is hardcoded** — `context.py` contains a specific 60km race training plan. Update the `training_plan` variable in that file to match your own plan before using the AI coach.
- Data is cached per session — restart the app to fetch fresh Strava data.
- Only `Run` type activities are relevant; other activity types fetched from Strava are passed through as-is.
