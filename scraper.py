import requests
import threading
from bs4 import BeautifulSoup
from multiprocessing import Process

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"


class ImageScraper:
    def __init__(self, two_chars, point_from, point_max):
        self.two_chars = two_chars
        self.point_from = point_from
        self.point_max = point_max

    def download_image(self, filename, link):
        html_req = requests.get(link, headers={"User-Agent": user_agent}, allow_redirects=False)  # user agent because cloudflare security is gay

        if html_req.status_code == 302:
            print("\x1b[0;30;41m" "Link does not exist" "\x1b[0m"". To fix please follow the instructions in the github repo.")
            return
        soup = BeautifulSoup(html_req.content, "html.parser")
        images = soup.find_all("img", {"class": "no-click screenshot-image"})

        for tag in images:
            src_img_from_html = tag["src"]
            if not src_img_from_html.startswith("http"):
                print("\x1b[0;36;40m" "Screenshot is removed." "\x1b[0m", link)
                return
            img = requests.get(src_img_from_html)

            with open(f"./images/{filename}.png", "wb") as file:
                file.write(img.content)
                file.close()
                print(f"Downloaded {link}")
        return

    def get_all_images(self):
        if not self.two_chars.isalpha():
            raise Exception("\x1b[0;31;40m" "Alphabetic characters only." "\x1b[0m")

        if len(self.two_chars) != 2:
            raise Exception("\x1b[0;31;40m" f"Expected (2) characters got {len(self.two_chars)}" "\x1b[0m")

        if self.point_from >= self.point_max:
            raise Exception("\x1b[0;31;40m" "Start point must be lower than end." "\x1b[0m")

        while self.point_from <= self.point_max:
            octal_version = str(self.point_from).zfill(4)
            img_link = f"https://prnt.sc/{self.two_chars}{octal_version}"
            self.download_image(img_link[15:], img_link)
            self.point_from += 1

        print("\x1b[0;32;40m" "Completed, look at ./images folder." "\x1b[0m")


if __name__ == "__main__":
    try:
        chars = input("\x1b[0;33;40m" "Enter any two random letters in the alphabet. Example [gy] ""\x1b[0m")
        start_point = int(input("\x1b[0;33;40m" "Enter a Point below 9999 to start from: " "\x1b[0m"))
        end_point = int(input("\x1b[0;33;40m" "Enter an End Point below 9999 to end: " "\x1b[0m"))

        m1 = ImageScraper(chars, start_point, end_point).get_all_images()
    except ValueError:
        raise Exception("\x1b[0;31;40m" "Start and End points must be integers." "\x1b[0m")

# make multiple class instances and then use threading for both of them simulataneously
