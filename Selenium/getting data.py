from selenium import webdriver
from selenium.webdriver.common.by import By
import time

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = webdriver.ChromeOptions()
options.binary_location= brave_path
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.amazon.com')

time.sleep(5)
driver.find_element('id','twotabsearchtextbox').send_keys('Iphone')
driver.find_element('id','nav-search-submit-button').click()

products = driver.find_elements(
    By.CLASS_NAME,
    "a-size-medium"
)
for product in products:
    print(product.text)