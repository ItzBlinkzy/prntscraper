# prntscraper

* *prntscraper* will allow you to scrape images from the prnt.sc website as they have predictable subheadings we can freely attempt to get random images or images in a sequential order from a specified amount to a max limit and download them into a folder. This process is also known as [Fuskering](https://en.wikipedia.org/wiki/Fusker)  This is a security issue from their end as It's highly common people store sensitive information that could easily be stolen if these images are found by the wrong people.

## This module is no longer being worked on.

* **DISCLAIMER** I am not responsible for the information that may be found with this package.
# Installation
***This module is compatible with Python3+.***

- Install the latest version from git repository using pip:
```bash
$ pip install git+https://github.com/ItzBlinkzy/prntscraper.git
```

- Install from PyPI:
```bash
$ pip install prntscraper
```

## **How to use**

Copy the below code into a python file and run it. This should automatically create a folder called **"images"** in the same directory as this file. This is also why it is advised you make a new folder for ease of access.

```py
from prntscraper import PrntScraper


my_scraper = PrntScraper()

# Gets random images and store them in ./images folder
random_images = my_scraper.get_random_images()
print(random_images)

# Gets the newest images and stores them in ./images folder  || MUST HAVE CHROMEDRIVER INSTALLED TO WORK || 
new_random_images = my_scraper.get_random_images(newest=True)
print(new_random_images)

# Takes inputted images and stores them in ./images folder.
input_images = my_scraper.get_input_images()
print(input_images)

# Gets the count of all the images in the ./images folder.
size = my_scraper.folder_size()
print(size)
```

# Outputs:
**get_random_images()`**
```py
How many images would you like?: 5
Completed: 100%|██████████████████████████████████████████████████| 6/6 [00:09<00:00,  1.58s/images]
Successfully downloaded 5 images. Look at ./images folder. 
```
`get_random_images(newest=True)`
*  To use the "**newest**" parameter you must have **Chromedriver** installed and inserted into **PATH** `(C:\Program Files (x86)`
     The version of **Chromedriver** must be less than or equal to your current Chrome browser version. 
    * To find your version type `chrome://version` in the search bar
    
**get_input_images()**
```py
Enter any two random letters in the alphabet. Example [gy]: vk
Enter a Point below 9999 to start from: 100
Enter an End Point (inclusive) below 9999 to end: 109
Completed: 100%|██████████████████████████████████████████████████| 10/10 [00:13<00:00,  1.31s/images]
Successfully downloaded 10 images. Look at ./images folder.
```
**folder_size()**
```py
There are currently 15 images in the folder.
```

Pretty simple right?

## Issues
Feel free to open an issue or make a pull request if you have any problems using this module.

## Credits
 * [ItzBlinkzy](https://github.com/ItzBlinkzy/)
      * You can be here too if you'd like to contribute.
        

## Repo
    * https://github.com/ItzBlinkzy/prntscraper/

## License
GNU General Public License v3
