import time
import os
from selenium import webdriver
WEBDRIVER_PATH = "C:/Program Files (x86)/chromedriver.exe"
MY_IMAGE_PATH = os.getcwd() + "/prntscraper/test/my_image.png"

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument("--headless")

def upload_image():
    driver = webdriver.Chrome(WEBDRIVER_PATH, chrome_options=options)
    driver.get("https://prnt.sc")
    
    time.sleep(.5)
    driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click() # Agree with cookies.
    time.sleep(.5)
    
    driver.find_element_by_xpath('//*[@id="fileupload"]/input').send_keys(MY_IMAGE_PATH) # Upload file.
    driver.implicitly_wait(10)
    print("Still loading please be patient...")
    
    time.sleep(15) # Make sure the user has uploaded the file fast enough
    
    link = driver.find_element_by_id("link-textbox").text
    ind = link.rfind("/") + 1 
    driver.close()
    
    return link[ind:ind+3] # get first three chars
