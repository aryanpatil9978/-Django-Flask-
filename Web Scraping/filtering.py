import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

#this is required as its in the policy for them to use a User Agent for a robot
user = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

response = requests.get(url = url,headers = user).content
soup = BeautifulSoup(response, "lxml")
tag = soup.find("div", {"id":"mp-right"})
#scraping the sub data under this div tag
h = tag.find("h2")#will find the first h2 tag and return it
h = tag.find_all("h2") #will find all the h2 tags and return them
#print(tag)
print(h)
