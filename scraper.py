import requests
import threading
import string
import random
from bs4 import BeautifulSoup
from multiprocessing import Process

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"

class ImageScraper:
    def download_image(self, filename, link):
        html_req = requests.get(link, headers={"User-Agent": user_agent}, allow_redirects=False)  # user agent because cloudflare security is gay

        if html_req.status_code == 302:
            print("\x1b[0;30;41m" "Link does not exist" "\x1b[0m", link)
            return False
        soup = BeautifulSoup(html_req.content, "html.parser")
        images = soup.find_all("img", {"class": "no-click screenshot-image"})

        for tag in images:
            src_img_from_html = tag["src"]
            if not src_img_from_html.startswith("http"):
                print("\x1b[0;36;40m" "Screenshot is removed." "\x1b[0m", link)
                return False
            img = requests.get(src_img_from_html)

            with open(f"./images/{filename}.png", "wb") as file:
                file.write(img.content)
                file.close()
                print(f"Downloaded {link}")
        return True
    
    
    def get_random_images(self, limit):
        count = 0
        if limit < 1:
            print("\x1b[0;31;40m" "Below minimum limit (1)" "\x1b[0m")
            return
        alphanum = string.ascii_lowercase + "1234567890"
        
        while count < limit:
            randchars = "".join([alphanum[alphanum.index(random.choice(alphanum))] for i in range(6)])
            img_link = f"https://prnt.sc/{randchars}"
            downloaded = self.download_image(randchars, img_link)
            
            if downloaded:
                count += 1
            print(count)
        print("\x1b[0;32;40m" "Completed, look at ./images folder." "\x1b[0m")


    def get_input_images(self, two_chars, point_from, point_max):
        if not two_chars.isalpha():
            raise Exception("\x1b[0;31;40m" "Alphabetic characters only." "\x1b[0m")

        if len(two_chars) != 2:
            raise Exception("\x1b[0;31;40m" f"Expected (2) characters got {len(two_chars)}" "\x1b[0m")

        if point_from >= point_max:
            raise Exception("\x1b[0;31;40m" "Start point must be lower than end." "\x1b[0m")

        while point_from <= point_max:
            octal_version = str(point_from).zfill(4)
            img_link = f"https://prnt.sc/{two_chars}{octal_version}"
            downloaded = self.download_image(img_link[15:], img_link)
            if downloaded:
                point_from += 1

        print("\x1b[0;32;40m" "Completed, look at ./images folder." "\x1b[0m")


if __name__ == "__main__":
    choose_input = input("\x1b[0;33;40m" " Would you like to customize your input [Input]. [Random] for random: " "\x1b[0m").lower()
    if choose_input == "random":
        try:
            limit = int(input("\x1b[0;33;40m" " How many images would you like?: " "\x1b[0m"))
            m1 = ImageScraper().get_random_images(limit)
            
        except ValueError:
            raise Exception("\x1b[0;31;40m" "Limit must be integers." "\x1b[0m")
    
    elif choose_input == "input":
        try:
            chars = input("\x1b[0;33;40m" "Enter any two random letters in the alphabet. Example [gy]: " "\x1b[0m")
            start_point = int(input("\x1b[0;33;40m" "Enter a Point below 9999 to start from: " "\x1b[0m"))
            end_point = int(input("\x1b[0;33;40m" "Enter an End Point below 9999 to end: " "\x1b[0m"))

            m2 = ImageScraper().get_input_images(chars, start_point, end_point)
        except ValueError:
            raise Exception("\x1b[0;31;40m" "Start and End points must be integers." "\x1b[0m")
    else:
        print("You did not enter 'input' or 'random'")

# make multiple class instances and then use threading for both of them simulataneously
