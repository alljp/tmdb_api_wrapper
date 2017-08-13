import os
import requests
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = config["API"]["Key"]


class APIKeyMissingError(Exception):
    pass


if not API_KEY:
    raise APIKeyMissingError(
        "API key missing! All methods require an API key.")
session = requests.Session()
session.params = {}
session.params['api_key'] = API_KEY

from .tv import TV
from .movie import Movie
from .people import People
