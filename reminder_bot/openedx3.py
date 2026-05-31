import base64
import requests
import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'creds.env'))


def get_access_token():

    client_id = os.environ["OPENEDX_CLIENT_ID"]
    client_secret = os.environ["OPENEDX_CLIENT_SECRET"]

    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(
        credentials.encode()
    ).decode()

    response = requests.post(
        "https://open.uds-staging-test.abzt.de/oauth2/access_token/",
        headers={
            "Authorization": f"Basic {encoded_credentials}"
        },
        data={
            "grant_type": "client_credentials",
            "token_type": "JWT",
        },
        timeout=10,
    )

    #print(response.status_code)
    #print(response.text)

    response.raise_for_status()

    return response.json()["access_token"]


def get_deadlines():

    token = get_access_token()

    response = requests.get(
        "https://open.uds-staging-test.abzt.de/api/course_experience/v1/course_deadlines_info/course-v1:GermanUDS+Task4+2026_Q2",
        headers={
            "Authorization": f"JWT {token}"
        },
        timeout=10,
    )

    #print(response.status_code)
    #print(response.text)

    response.raise_for_status()

    return response.json()

def get_dates():

    token = get_access_token()

    response = requests.get(
        "https://open.uds-staging-test.abzt.de/api/course_home/dates/course-v1:GermanUDS+Task4+2026_Q2",
        headers={
            "Authorization": f"JWT {token}"
        },
        timeout=10,
    )
    data=response.json()


    #print(response)
    #print(response.status_code)
    # this print the json answer as raw data
    #print(response.text)

    #response.raise_for_status()

    return data

#this is enabling printing json raw data for testing
if __name__ == "__main__":
    result = get_dates()
    print("Final result:", result)

