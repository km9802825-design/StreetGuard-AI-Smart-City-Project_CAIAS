import requests

BASE_URL = "http://127.0.0.1:8000"

def send_sos(data):
    return requests.post(f"{BASE_URL}/emergency/", json=data)

def create_report(data, files=None):
    return requests.post(f"{BASE_URL}/reports/", data=data, files=files)

def get_reports():
    return requests.get(f"{BASE_URL}/reports/")

def get_ai_advice(data):
    return requests.post(f"{BASE_URL}/ai", json=data)