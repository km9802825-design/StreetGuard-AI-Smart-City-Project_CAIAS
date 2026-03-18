import requests
from datetime import datetime

# 🌍 Default location (Bangalore)
DEFAULT_LAT = 12.9716
DEFAULT_LNG = 77.5946


# 🕒 Format time nicely
def format_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 📍 Convert address → coordinates (basic version)
def get_coordinates(address):
    """
    Simple placeholder (can upgrade to real geocoding later)
    """
    if address:
        return DEFAULT_LAT, DEFAULT_LNG
    return DEFAULT_LAT, DEFAULT_LNG


# 🔥 Safe API call (no crash)
def safe_post(url, data=None, files=None, json=None):
    try:
        res = requests.post(url, data=data, files=files, json=json)
        return res
    except Exception as e:
        return {"error": str(e)}


def safe_get(url):
    try:
        res = requests.get(url)
        return res
    except Exception as e:
        return {"error": str(e)}