# prnt.sc-scraper

* *prnt.sc-scraper* will allow you to scrape images from the prnt.sc website as they have predictable subheadings we can freely attempt to get random images or images in a sequential order from a specified amount to a max limit and download them into a folder. This is a security issue from their end as It's highly common people store sensitive information that could easily be stolen if these images are found by the wrong people

# Installation
***This module is compatible with Python3+.***

- Install latest version from git repository using pip:
```bash
$ pip install git+https://github.com/ItzBlinkzy/prnt.sc-scraper.git
```

- Install from PyPI:
```bash
$ pip install prnt.sc-scraper
```

## **How to use**
  * When setting this up make sure you have a folder called **"images"** in the same directory as the file importing the module.

```py
from scraper import PrntScraper

# Get random images and store them in ./images folder
my_scraper = PrntScraper()
result = my_scraper.get_random_images()
print(result)

# Take inputted images and store them in ./images folder.
my_scraper = PrntScraper()
result = my_scraper.get_input_images()
print(result)
```

# Outputs:
**get_random_images()**

```py
How many images would you like?: 5
Downloaded https://prnt.sc/odchh5
Downloaded https://prnt.sc/2n833q
Downloaded https://prnt.sc/n2w4x9
Downloaded https://prnt.sc/cy2cgi
Downloaded https://prnt.sc/w0a6bn
Successfully downloaded 5 images. Look at ./images folder. 
```
**get_input_images()**
```py
Enter any two random letters in the alphabet. Example [gy]: vk
Enter a Point below 9999 to start from: 100
Enter an End Point below 9999 to end: 105
Downloaded https://prnt.sc/vk0100
Downloaded https://prnt.sc/vk0101
Downloaded https://prnt.sc/vk0102
Downloaded https://prnt.sc/vk0103
Downloaded https://prnt.sc/vk0104
Downloaded https://prnt.sc/vk0105
Successfully downloaded 6 images. Look at ./images folder.
```
Pretty simple right?

## Issues
Feel free to open an issue or make a pull request if you have any problems using this module.

## Credits
 * [ItzBlinkzy](https://github.com/ItzBlinkzy/)
      * You can be here too if you'd like to contribute.
        

## Repo
    * https://github.com/ItzBlinkzy/prnt.sc-scraper/

## License
MIT