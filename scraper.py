import requests
import threading
from bs4 import BeautifulSoup
import string

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
ascii_lowercase = string.ascii_lowercase

class ImageScraper:
    def __init__(self, two_chars, point_from, point_max):
        self.two_chars = two_chars
        self.point_from = point_from
        self.point_max = point_max

    def download_image(self, filename, link): 
        html_req = requests.get(link, headers={"User-Agent": user_agent}, allow_redirects=False) # I have to use a user agent because cloudflare security is gay
        if html_req.status_code == 302:
            print('\x1b[0;30;41m' + 'Link does not exist' + '\x1b[0m'+"\n to fix please follow the instructions in the github repo. [link it here bai]")
            return
        soup = BeautifulSoup(html_req.content, "html.parser")
        images = soup.find_all("img", {"class": "no-click screenshot-image"})
        
        for tag in images:
            src_img_from_html = tag["src"]
            if not src_img_from_html.startswith("http"):
                print('\x1b[0;33;40m' + 'Link is invalid or removed' + '\x1b[0m', link)
                return
            img = requests.get(src_img_from_html)
        
            with open(f"./images/{filename}.png", "wb") as file:
                file.write(img.content)
                file.close()
                print(f"Downloaded {link}")
        return
    
    
    def get_all_images(self):
        if len(self.two_chars) != 2:
           raise Exception('\x1b[0;31;40m' + f'Expected (2) characters got {len(self.two_chars)}' + '\x1b[0m')
       
        elif not self.two_chars.lower().isalpha():
            raise Exception('\x1b[0;31;40m' + 'Alphabetic characters only.' + '\x1b[0m')
        
        while self.point_from <= self.point_max:
            octal_version = str(self.point_from).zfill(4)
            img_link = f"https://prnt.sc/{self.two_chars}{octal_version}"
            self.download_image(img_link[15:], img_link)
            self.point_from += 1
        print('\x1b[0;32;40m' + 'Completed, look at ./images folder.' + '\x1b[0m')


m1 = ImageScraper("##", 250, 400).get_all_images()
m1 = ImageScraper("ly", 500, 670).get_all_images()
#make multiple instance and then use threading.Thread for both of them 0_0