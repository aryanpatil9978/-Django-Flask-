import requests
#will not again work on our website since login is required
url ="http://127.0.0.1:8000/posts/?offset=5"

params = {
    "offset":"5"
}

response = requests.get(url =url, params =params)

print(response.text)