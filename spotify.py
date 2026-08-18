import requests
import sys

CLIENT_ID = "105adc1917f7412c9eed0f569495de52"
CLIENT_SECRET = "e8600589047d4becaaa7a05205f8e0ef"
PERSON_NAME = "Robert William Fisher"

url = "https://api.spotify.com/v1/search"
ACCESS_TOKEN = ""


auth_response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={"grant_type": "client_credentials"},
    auth=(CLIENT_ID, CLIENT_SECRET),
)

ACCESS_TOKEN = auth_response.json()["access_token"]

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
params = {
    "q": f'"{PERSON_NAME}"',
    "type": "episode",
    "market": "US",
    "limit": 50,
}

response = requests.get(url, headers=headers, params="podcast")
# data = response.raise_for_status()

print(response)