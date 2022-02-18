from toggl import Toggl
from sqlite3 import paramstyle
from pytest import param
import requests as rq
from requests.auth import HTTPBasicAuth
import json

params = {
    "user_agent": "joel.wallner-blomster@triggerfish.se",
    "workspace_id": "598248",
    "calculate": "time"
}

headers = {
    "Content-Type": "text",
}

auth = {
    "username": "api_token",
    "password": "024e1d7952cfc53aa6aa94644168f363"
}

toggl = Toggl("024e1d7952cfc53aa6aa94644168f363")
data = toggl.request(
    "https://api.track.toggl.com/reports/api/v2/project", params)
print(data)
json_data = toggl.pretty_json(data)
print(json_data)
