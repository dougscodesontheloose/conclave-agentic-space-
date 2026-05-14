import os
import json
import urllib.parse
import urllib.request

CLIENT_ID = "77jkpqncli74jq"
CLIENT_SECRET = "<linkedin_client_secret>"

data = urllib.parse.urlencode({
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}).encode('utf-8')

req = urllib.request.Request("https://www.linkedin.com/oauth/v2/accessToken", data=data)
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print(e)
