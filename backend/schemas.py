from typing import Dict, Any, List

from ninja import Schema


class TrackSchema(Schema):
    artist: str
    track: str
    album_image_url: str
    preview_url: str


class ErrorMessage(Schema):
    errors: Dict[str, Any]
