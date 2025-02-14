from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

ATTLASSIAN_SITE_URL = os.environ.get('ATTLASSIAN_SITE_URL')
EMAIL = os.environ.get('EMAIL')
API_TOKEN = os.environ.get('API_TOKEN')

@app.route('/create-jira-ticket', methods=['POST'])
def createJiraTicket():
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
        "summary": "Issue 2 created by Python",
    },
    "update": {}
    } )

    # Get the incoming data from the request (Return Type is Dictionary)
    data = request.get_json()
    
    # Create a Jira Ticket only when the comment is /jira
    if data["comment"]["body"] == "/jira":
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    return jsonify(
        {
            "error": "No Jira Ticket Created. Please type /jira to create a Jira Ticket"
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)