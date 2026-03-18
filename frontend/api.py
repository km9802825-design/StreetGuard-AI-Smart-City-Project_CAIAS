import os
import requests

BASE_URL = os.getenv("STREETGUARD_API_BASE_URL", "http://127.0.0.1:8000")
TIMEOUT = 10


def _request(method, path, **kwargs):
    try:
        response = requests.request(
            method=method,
            url=f"{BASE_URL}{path}",
            timeout=TIMEOUT,
            **kwargs
        )
        response.raise_for_status()
        return True, response.json()
    except requests.exceptions.RequestException as exc:
        return False, str(exc)


def send_sos(user, location, message):
    return _request("POST", "/emergency/", json={"user": user, "location": location, "message": message})


def create_report(user, description, address, lat=None, lng=None, image_file=None):
    form_data = {"user": user, "description": description, "address": address}
    if lat is not None:
        form_data["lat"] = str(lat)
    if lng is not None:
        form_data["lng"] = str(lng)
    files = None
    if image_file is not None:
        files = {"image": (image_file.name, image_file.getvalue(), image_file.type)}
    return _request("POST", "/reports/", data=form_data, files=files)


def get_reports():
    return _request("GET", "/reports/")


def get_route(start, end):
    return _request("GET", "/route/", params={"start": start, "end": end})


def get_ai_advice(situation):
    return _request("POST", "/ai/", json={"situation": situation})


def get_dashboard_stats():
    return _request("GET", "/dashboard/stats")


def get_sos_history():
    return _request("GET", "/emergency/history")
