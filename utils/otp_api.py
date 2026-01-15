# utils/otp_api.py
import requests

def fetch_otp(username):
    response = requests.get(
        f"https://api-test.company.com/test/get-otp/{username}"
    )
    return response.json()["otp"]