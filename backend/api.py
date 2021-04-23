from typing import List

from ninja import Router

from backend.schemas import TrackSchema, ErrorMessage
from backend.util import read_file_as_json, get_random_artist, spotify_token_generator, get_access_token, \
    get_tracks_from_spotify, sorted_list_of_tracks

router = Router()


@router.get("/tracks/{genre}", response={200: List[TrackSchema], 400: ErrorMessage})
def get_tracks(request, genre: str):
    try:
        file_path = "backend/static/genres.json"
        data: dict = read_file_as_json(file_path)
    except FileNotFoundError:
        return 400, {"errors": {"file": "File not found"}}
    except Exception as exc:
        return 400, {"errors": {"error": str(exc)}}

    genre = genre.lower()
    if genre in data.keys():
        try:
            artist = get_random_artist(data, genre)
            basic_auth = spotify_token_generator()
            access_token = get_access_token(basic_auth)
            tracks = get_tracks_from_spotify(access_token=access_token, artist=artist)
            sorted_tracks_list = sorted_list_of_tracks(tracks['tracks']['items'])
        except Exception as exc:
            return 400, {"errors": {"util_error": str(exc)}}

    else:
        return 400, {"errors": {"genre": "Genre could not found"}}
    print(sorted_tracks_list)
    return 200, sorted_tracks_list
