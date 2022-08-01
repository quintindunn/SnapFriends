from .Friend import Friend
import requests
import io
from PIL import Image


def friends_from_dict(data: dict) -> list:
    """
    Creates a list of Friend objects from a dictionary.
    :param data: The dictionary containing the friends.
    :return: A list of Friend objects.
    """
    friends = []
    if data.get('friends'):
        for friend in data.get('friends'):
            friends.append(Friend.from_dict(friend))
    return friends


def get_bitmoji_image(url: str) -> Image:
    """
    Returns the image data from a bitmoji url.
    :param url: The url of the bitmoji.
    :return Image: The pillow image object.
    """
    bytes_io = io.BytesIO()
    req = requests.get(url, stream=True)
    for chunk in req.iter_content(chunk_size=1024):
        if chunk:
            bytes_io.write(chunk)

    im = Image.open(bytes_io)
    return im
