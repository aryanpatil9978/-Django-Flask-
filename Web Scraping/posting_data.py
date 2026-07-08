import requests
url = "http://127.0.0.1:8000/posts/?limit=5"

payload = {
    "title":"Posting Data",
    "content":"Posting this data via python using the requests librabry."
}
#This will not get posted to our blog website since it requres a login first
response = requests.post(url = url , data = payload)
print(response.status_code) #403 permission issue
print(response.text)