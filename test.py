import requests
import sys
from bs4 import BeautifulSoup as soup
r = requests.get("https://prnt.sc/104542", headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"})
TS = soup(r.content, "html.parser")

for tag in TS.find_all("img", {"class": "no-click screenshot-image"}):
    print(tag["src"])