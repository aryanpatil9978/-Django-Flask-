import requests

url = 'http://127.0.0.1:5000/'

response = requests.get(url = url)


print(type(response.text))
print(response.text)# return us in the form of string