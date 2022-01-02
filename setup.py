from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prntscraper",
    version="2.5.6",
    description="Pulls random images from https://prnt.sc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ItzBlinkzy/prnt.sc-scraper",
    author="Itz Blinkzy",
    author_email="legendarystone12@gmail.com",
    license="GNU",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords="scraper prnt.sc prntscraper fuskering",
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=["requests", "bs4", "tqdm", "selenium"],
)