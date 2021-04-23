import base64
import json
from random import randint

import requests

from djangospotify import settings


def read_file_as_json(file_path):
    with open(file_path, "r") as f:
        return json.loads(f.read())


def get_random_artist(json_data, genre):
    random_index = randint(0, len(json_data[genre]) - 1)
    return json_data[genre][random_index]


def spotify_token_generator():
    client_id = settings.SPOTIFY_CLIENT_ID
    client_secret = settings.SPOTIFY_CLINT_SECRET
    client_combined_credentials = f"{client_id}:{client_secret}"
    byte_data = client_combined_credentials.encode("ascii")
    base64_bytes = base64.b64encode(byte_data)
    base64_string = base64_bytes.decode("ascii")
    authorization = f"Basic {base64_string}"
    return authorization


def get_access_token(basic_auth):
    url = "https://accounts.spotify.com/api/token"

    payload = "grant_type=client_credentials"
    headers = {
        'authorization': basic_auth,
        'content-type': "application/x-www-form-urlencoded",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()['access_token']


def get_tracks_from_spotify(access_token, artist):
    url = "https://api.spotify.com/v1/search"

    querystring = {"q": f"{artist}", "type": "track", "offset": 50}

    headers = {
        'authorization': f"Bearer {access_token}",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def sorted_list_of_tracks(tracks_list: list):
    sorted_tracks_list = []
    sorted_tracks_by_popularity = sorted(tracks_list, key=lambda k: k['popularity'], reverse=True)
    for item in sorted_tracks_by_popularity:
        sorted_tracks_list.append({
            'artist': item['album']['artists'][0]['name'],
            'track': item['name'],
            'album_image_url': item['album']['images'][1]['url'],
            'preview_url': item['preview_url'] if item['preview_url'] else ""
        })
    return sorted_tracks_list[0:10]
