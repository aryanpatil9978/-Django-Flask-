import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
                    }
        self.response = requests.get(url = self.url, headers = self.user_agent).text
        self.soup = BeautifulSoup(self.response, 'lxml')

    def product_title(self):
        title = self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Title not Found"

    def product_price(self):
        price = self.soup.find("span",{"class":"a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Price Not Found"

    def product_image(self,image_name):
        image_url = self.soup.find('img', class_="a-dynamic-image a-stretch-horizontal media-block-image-tag")['src']
        img_name = image_name.split('(')[0].replace("|","")
        img_url = requests.get(image_url)
        f = open(img_name,"wb")
        f.write(img_url.content)
        return image_url


devices = [PriceTracer("https://www.amazon.in/Xiaomi-13-Pro-Ceramic-Professional/dp/B0BVMP4NGL/ref=pd_sbs_d_sccl_1_3/525-6473318-2151432"),
           PriceTracer("https://www.amazon.in/Xiaomi-Couture-Storage-Snapdragon-Flagship/dp/B09XB9DCY4/ref=pd_sbs_d_sccl_1_3/525-6473318-2151432?psc=1"),
           PriceTracer("https://www.amazon.in/XIAOMI-Flagship-Cameras-UltraPure-Segment/dp/B0GYY8ZNP3/ref=pd_sbs_d_sccl_1_3/525-6473318-2151432?psc=1")
           ]

for device in devices:
    product_name = device.product_title()
    print(product_name)
    productprice = device.product_price()
    print("₹"+productprice)
    print(device.product_image(product_name))
    target_price = 50000
    print("Target Price: ",target_price)
    price = productprice.replace(",","").replace(".","")
    if int(price) <= target_price:
        print("Product is Affortable")
    else:
        print("Product is Not Affortable")
    print("\n")