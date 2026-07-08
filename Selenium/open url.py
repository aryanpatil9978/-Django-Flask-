from selenium import webdriver
import time

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
#changing the browser from chrome to brave
options = webdriver.ChromeOptions()
options.binary_location= brave_path
#helps to keep the browser open even when the program has been executed
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#makes the broswer fullscreen
driver.maximize_window()
#opening a url
driver.get('https://www.google.com')
#the name attribute for the search box to locate it and pass a value to search
input = driver.find_element('name','q')
#types 'Python' into the search box
input.send_keys('Python')
button = driver.find_element('name','btnK')
#waits 5 sec
time.sleep(5)
button.click()
time.sleep(5)
#going back to the previous page (besides reload option on browser)
driver.back()
time.sleep(2)
# refreshes the page
driver.refresh()
time.sleep(5)
#going back to the next page (besides reload option on browser)
driver.forward()
time.sleep(5)
driver.quit()