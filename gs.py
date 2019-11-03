import requests
import json

auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : "be2457a2c0304ea6a0a046edd3df0dce",
    "client_secret" : "e7ffb80965e1bf787992a9c50a8a4d6118545bcd6011b175cf569b889ebb143f",
    "scope"         : "read_product_data"
}

session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

request_url = "https://api.marquee.gs.com/v1/assets"


###Use this request query to poll data.
# request_query = {
#                     "where": {
#                         "gsid": ["75154", "193067", "194688", "902608", "85627"]
#                     },
#                     "startDate": "2017-01-15",
#                     "endDate":"2018-01-15"
#                }
# request = session.post(url=request_url, json=request_query)

request = session.get(url=request_url)
results = json.loads(request.text)

print(results)