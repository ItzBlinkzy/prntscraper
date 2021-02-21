import requests
import string
import os
import random
from tqdm import tqdm
from bs4 import BeautifulSoup


user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"


class PrntScraper:
    def __download_image(self, filename, link):
        html_req = requests.get(link, headers={"User-Agent": user_agent}, allow_redirects=False)  # user agent because cloudflare provides [error 520] without it

        if not os.path.exists(os.getcwd()+"/images"):
           raise Exception("\x1b[0;31;40m" "There is no ./images folder in this directory" "\x1b[0m")
        
        if html_req.status_code == 302:
            return 302
        
        soup = BeautifulSoup(html_req.content, "html.parser")
        images = soup.find_all("img", {"class": "no-click screenshot-image"})

        for tag in images:
            src_img_from_html = tag["src"]
            
            if not src_img_from_html.startswith("http"):
                return False
            
            img = requests.get(src_img_from_html)
                    
            with open(f"./images/{filename}.png", "wb") as file:
                file.write(img.content)
                file.close()
                
        return True
    
    

    def get_random_images(self):
        img_count = 0
        limit = input("\x1b[0;33;40m" " How many images would you like?: " "\x1b[0m")
        
        if not limit.isdigit():
            return "\x1b[0;31;40m" "You must enter an integer for the limit" "\x1b[0m"
        
        limit = int(limit)
        
        if limit < 1:
            return "\x1b[0;31;40m" "Below minimum limit (1)" "\x1b[0m"
        
        alphanum = string.ascii_lowercase + "1234567890"
        
        with tqdm(total=limit, unit="images", desc="Processing...", bar_format='{desc}{percentage:3.0f}%|{bar:50}{r_bar}') as pbar:   # Creating a PROGRESS BAR
            while img_count < limit:
                randchars = "".join([alphanum[alphanum.index(random.choice(alphanum))] for i in range(6)])
                img_link = f"https://prnt.sc/{randchars}"
                downloaded = self.__download_image(randchars, img_link)
                pbar.set_description(f"Downloading {img_link}")
                
                if downloaded == True:
                    img_count += 1
                    pbar.update(1)
                    
                elif downloaded == 302:
                    pbar.set_description(f"\x1b[0;31;40m" f"{img_link} does not exist" "\x1b[0m")
                
                elif downloaded == False:
                    pbar.set_description(f"{img_link} is removed..")  
            pbar.set_description("Completed")
            
        return "\x1b[0;32;40m" f"Successfully downloaded {img_count} images. Look at ./images folder."  "\x1b[0m"



    def get_input_images(self):
        try:
            success_img_count = 0
            two_chars = input("\x1b[0;33;40m" "Enter any two random letters in the alphabet. Example [gy]: " "\x1b[0m").lower()
            point_from = int(input("\x1b[0;33;40m" "Enter a Point below 9999 to start from: " "\x1b[0m"))
            point_max = int(input("\x1b[0;33;40m" "Enter an End Point (inclusive) below 9999 to end: " "\x1b[0m"))
            limit = (point_max - point_from) + 1
            
            # INPUT ERROR HANDLING
            if point_from > 9999 or point_max > 9999:
                return "\x1b[0;31;40m" "Must be below 9999" "\x1b[0m"

            if not two_chars.isalpha():
                return "\x1b[0;31;40m" "Alphabetic characters only." "\x1b[0m"

            if len(two_chars) != 2:
                return "\x1b[0;31;40m" f"Expected (2) characters got {len(two_chars)}" "\x1b[0m"

            if point_from >= point_max:
                return "\x1b[0;31;40m" "Start point must be lower than end." "\x1b[0m"
            
            with tqdm(total=limit, unit="images", desc="Processing...", bar_format='{desc}{percentage:3.0f}%|{bar:50}{r_bar}') as pbar: # PROGRESS BAR
                
                while point_from <= point_max:
                    octal_version = str(point_from).zfill(4)
                    img_link = f"https://prnt.sc/{two_chars}{octal_version}"
                    downloaded = self.__download_image(img_link[15:], img_link)
                    pbar.set_description(f"Downloading {img_link}")
                    
                    if downloaded == True:
                        pbar.update(1)
                        success_img_count += 1
                        
                    elif downloaded == 302:
                        pbar.set_description("\x1b[0;31;40m" f"{img_link} does not exist" "\x1b[0m")
                        pbar.update(1)
                    
                    elif downloaded == False:
                        pbar.set_description("\x1b[0;36;40m" f"{img_link} is removed" "\x1b[0m")
                        pbar.update(1)
                        
                    point_from += 1
                pbar.set_description("Completed")
                    
            return "\x1b[0;32;40m" f"Successfully downloaded {success_img_count} images. Look at ./images folder."  "\x1b[0m"
        
        except ValueError:
            return "\x1b[0;31;40m" "Start and End points must be integers." "\x1b[0m"
        
    
    def folder_size(self):
        size = len(os.listdir(os.getcwd()+"/images"))
        return "\x1b[0;32;40m" f"There are currently {size} images in the folder."  "\x1b[0m"


if __name__ == "__main__":
    choose_input = input("\x1b[0;33;40m" " Would you like to customize your input [Input]. [Random] for random: " "\x1b[0m").lower()
    
    if choose_input == "random":
        m1 = PrntScraper().get_random_images()
        print(m1)
    
    elif choose_input == "input":
        m2 = PrntScraper().get_input_images()
        print(m2)
        
    else:
        print("You did not enter 'input' or 'random'")

# make multiple class instances and then use threading for both of them simulataneously
#put all \x1b[0;33;40m and \x1b[0m in vars or use a color moduleq