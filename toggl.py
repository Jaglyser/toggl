import json
from urllib import response
import requests as rq
from requests.auth import HTTPBasicAuth


class Toggl:
    def __init__(self, key: str) -> None:
        self.key = key
        self.password = 'api_token'
        self.headers = {"Content-Type": "application/json"}
        self.data = None

    def request(self, path: str, params: dict) -> dict:
        data = rq.get(url=path, params=params, headers=self.headers,
                      auth=HTTPBasicAuth(self.key, self.password))
        self.data = data
        return data

    def pretty_json(self, data: response) -> dict:
        return json.dumps(json.loads(data.text), indent=2)

    def handler(self, data: response, path: str):
        path_handle = path.rsplit("/", 1)[-1]