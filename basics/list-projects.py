# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

ATTLASSIAN_SITE_URL = os.environ.get('ATTLASSIAN_SITE_URL')
EMAIL = os.environ.get('EMAIL')
API_TOKEN = os.environ.get('API_TOKEN')

url = ATTLASSIAN_SITE_URL + "/rest/api/3/project"

auth = HTTPBasicAuth(EMAIL , API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

response_dict = json.loads(response.text)

project_name = response_dict[1]["name"]

print(project_name)