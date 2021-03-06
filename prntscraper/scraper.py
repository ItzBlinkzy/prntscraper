import requests
import string
import os
import random
from tqdm import tqdm
from bs4 import BeautifulSoup
from prntscraper.upload import upload_image
from prntscraper.Exceptions import NoImageFolderError, ValueTooSmallError, ValueTooLargeError, NotAnIntegerError, AlphabeticCharsOnlyError

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"


class PrntScraper:
    def __download_image(self, filename, link):

        """
        Makes two requests to https://prnt.sc, downloads the file and stores them in ./images folder.
        """

        html_req = requests.get(link, headers={"User-Agent": user_agent}, allow_redirects=False)  # user agent because cloudflare provides [error 520] without it

        if not os.path.exists(os.getcwd() + "/images"):
            raise NoImageFolderError()

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

    def get_random_images(self, newest=False):

        """
        #### Gets images and stores them in ./images folder
        ###  MUST HAVE CHROMEDRIVER INSTALLED TO GET NEWEST IMAGES 
        """

        img_count = 0
        limit = input("\x1b[0;33;40m" " How many images would you like?: " "\x1b[0m")
        three_chars = None

        if newest:
            print(
                "\x1b[1;35;40m" "You have selected the newest images, it may take approximately 55 - 60 seconds to start. " "\x1b[0m")
            file_chars = upload_image()

            if not file_chars:
                return "Could not upload image to https://prnt.sc in time, please try again."

            three_chars = file_chars

        if not limit.isdigit():
            raise NotAnIntegerError(limit)

        limit = int(limit)

        if limit < 1:
            raise ValueTooSmallError(limit)

        alphanum = string.ascii_lowercase + "1234567890"

        with tqdm(total=limit, unit="images", desc="Processing...",
                  bar_format='{desc}{percentage:3.0f}%|{bar:50}{r_bar}') as pbar:  # Creating a PROGRESS BAR
            while img_count < limit:
                rand_chars = None

                if newest:
                    rand_chars = three_chars + "".join([alphanum[alphanum.index(random.choice(alphanum))] for i in range(4)])

                if not newest:
                    rand_chars = "".join([alphanum[alphanum.index(random.choice(alphanum))] for i in range(6)])

                img_link = f"https://prnt.sc/{rand_chars}"
                downloaded = self.__download_image(rand_chars, img_link)
                pbar.set_description(f"Downloading {img_link}")

                if downloaded:
                    img_count += 1
                    pbar.update(1)

                elif downloaded == 302:
                    pbar.set_description(f"\x1b[0;31;40m" f"{img_link} does not exist" "\x1b[0m")

                elif not downloaded:
                    pbar.set_description("\x1b[0;36;40m" f"{img_link} is removed" "\x1b[0m")
            pbar.set_description("Completed")

        return "\x1b[0;32;40m" f"Successfully downloaded {img_count} images. Look at ./images folder."  "\x1b[0m"

    def get_input_images(self):
        """
        Takes inputted images and stores them in ./images folder.
        """

        try:
            success_img_count = 0
            two_chars = input("\x1b[0;33;40m" "Enter any two random letters in the alphabet. Example [gy]: " "\x1b[0m").lower()
            point_from = int(input("\x1b[0;33;40m" "Enter a Point below 9999 to start from: " "\x1b[0m"))
            point_max = int(input("\x1b[0;33;40m" "Enter an End Point (inclusive) below 9999 to end: " "\x1b[0m"))
            limit = (point_max - point_from) + 1

            # INPUT ERROR HANDLING
            if point_from > 9999:
                raise ValueTooLargeError(point_from)

            if point_max > 9999:
                raise ValueTooLargeError(point_max)

            if not two_chars.isalpha():
                raise AlphabeticCharsOnlyError(two_chars)

            if len(two_chars) != 2:
                return "\x1b[0;31;40m" f"Expected (2) characters got {len(two_chars)}" "\x1b[0m"

            if point_from >= point_max:
                raise ValueTooLargeError(point_from)

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
        """
        Returns the amount of images in the `./images` folder.
        """

        size = len(os.listdir(os.getcwd() + "/images"))
        return "\x1b[0;32;40m" f"There are currently {size} images in the folder."  "\x1b[0m"
