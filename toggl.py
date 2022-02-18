import json
import requests as rq
from requests.auth import HTTPBasicAuth


class Toggl:
    def __init__(self, key: str) -> None:
        self.key = key
        self.password = 'api_token'
        self.headers = {"Content-Type": "application/json"}
        self.detailed = None
        self.weekly = None

    def request(self, path: str, params: dict) -> dict:
        data = rq.get(url=path, params=params, headers=self.headers,
                      auth=HTTPBasicAuth(self.key, self.password))
        self.handler(path)
        return data

    def pretty_json(self, data) -> dict:
        return json.dumps(json.loads(data.text), indent=2)

    def handler(self, path: str, data):
        path_handle = path.rsplit("/", 1)[-1]
        handle = {
            "weekly": self.set_weekly(data),
            "details": self.set_detailed(data)
        }
        handle[path_handle]

    def set_weekly(self, data):
        self.weekly = data

    def set_detailed(self, data):
        self.detailed = data
