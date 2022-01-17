from cgitb import html

from bs4 import BeautifulSoup

with open("Day - 45/website.html","r", encoding="UTF-8") as site:
    contents = site.read()

print(contents)