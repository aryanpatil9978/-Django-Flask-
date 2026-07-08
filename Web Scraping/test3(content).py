import requests

url = "http://127.0.0.1:5000/static/Author.png"

user ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

response = requests.get(url = url , headers = user)
pic = response.content  #return the data in the form of bytes
f = open("test.png", "wb")
f.write(pic)
