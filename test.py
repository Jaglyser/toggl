from toggl import Toggl
from sqlite3 import paramstyle
from pytest import param
import requests as rq
from requests.auth import HTTPBasicAuth
import json
import dotenv
dotenv.load_dotenv()

toggl = Toggl(API_KEY)
data = toggl.request(
    "https://api.track.toggl.com/reports/api/v2/project", params)
print(data)
json_data = toggl.pretty_json(data)
print(json_data)
