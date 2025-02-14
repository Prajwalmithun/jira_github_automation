# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

ATTLASSIAN_SITE_URL = os.environ.get('ATTLASSIAN_SITE_URL')
EMAIL = os.environ.get('EMAIL')
API_TOKEN = os.environ.get('API_TOKEN')

url = ATTLASSIAN_SITE_URL + "/rest/api/3/issue"

auth = HTTPBasicAuth(EMAIL , API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "issuetype": {
      "id": "10003"
    },

    "project": {
      "key": "SCRUM"
    },

    "summary": "Issue 1 created by Python",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))