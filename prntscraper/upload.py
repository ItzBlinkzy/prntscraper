import time
import os
import prntscraper
import requests
from selenium import webdriver


WEBDRIVER_PATH = "C:/Program Files (x86)/chromedriver.exe"
MY_IMAGE_PATH = os.getcwd() + "/temp_image.png"

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument("--headless")


def __temp_download():
    """
    Temporarily downloads an image created by Blinkzy from Discord
    """
    
    img = requests.get("https://media.discordapp.net/attachments/561907232338608152/813235414370222080/my_image.png?width=1013&height=676")
    with open("./temp_image.png", "wb") as file:
        file.write(img.content)
        file.close()
    

def upload_image():
    """
    Uploads the temporary image to https://prnt.sc and takes the first three characters to be used to find recent images
    """
    
    __temp_download()
    
    driver = webdriver.Chrome(WEBDRIVER_PATH, chrome_options=options)
    driver.get("https://prnt.sc")
    
    time.sleep(.5)
    driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click() # Agree with cookies.
    time.sleep(.5)
    
    driver.find_element_by_xpath('//*[@id="fileupload"]/input').send_keys(MY_IMAGE_PATH) # Upload file.
    driver.implicitly_wait(10)
    print("Still loading please be patient...")
    
    time.sleep(55) # Make sure the user has uploaded the file fast enough
    
    link = driver.find_element_by_id("link-textbox").text
    ind = link.rfind("/") + 1 
    
    driver.close()
    os.remove("./temp_image.png")
    three_chars = link[ind:ind+3]
    
    if not three_chars:
        return False
    
    return three_chars
    
