import requests
import re #regular expressions
import os
user = input("Enter the name of the image: ")

#copy all the requered data by searching something on google and inspecting the page
useragent ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

url = f"https://search.brave.com/images?q={user}"

response = requests.get(url = url,headers = useragent).text
#after you get the info in your terminal we will apply regular expression here to filter the data
# print(response)


pattern = r'https://[^"]+\.jpg'

images = re.findall(pattern , response)
#print(images)
print(f"Total Images : {len(images)}")
no_of_images = int(input("Enter the number of images to download: "))+2
if images:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)

    else:
        os.chdir(user)

    for image_url in images[:no_of_images]:
        #here eval() helps us to convert the string into a list
        response = requests.get(url = image_url).content
        img_name = image_url.split('/')[-1]

        with open(img_name,"wb") as file:
            file.write(response)

#"https://static.vecteezy.com/system/resources/thumbnails/054/634/268/small/a-crescent-moon-on-a-white-background-vector.jpg"
