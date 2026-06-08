import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://open.uds-staging-test.abzt.de"
COURSE_KEY = "course-v1:GermanUDS+Task4+2026_Q2"

def get_access_token():
    client_id = os.environ["OPENEDX_CLIENT_ID"]
    client_secret = os.environ["OPENEDX_CLIENT_SECRET"]

    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    response = requests.post(
        f"{BASE_URL}/oauth2/access_token",
        headers={"Authorization": f"Basic {encoded_credentials}"},
        data={
            "grant_type": "client_credentials",
            "token_type": "jwt",
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()["access_token"]

def get_deadlines():
    token = get_access_token()

    response = requests.get(
        f"{BASE_URL}/api/course_experience/v1/course_deadlines_info/{COURSE_KEY}",
        headers={"Authorization": f"JWT {token}"},
        timeout=10,
    )

    response.raise_for_status()
    return response.json()