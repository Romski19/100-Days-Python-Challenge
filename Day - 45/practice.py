from os import link
from bs4 import BeautifulSoup
# import lxml

with open("Day - 45/website.html","r", encoding="UTF-8") as site:
    contents = site.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.a)

# Find All Sample

# print(soup.find_all('p'))
# for ps in soup.find_all('p'):
#     print(ps.get_text())

# for ps in soup.find_all('a'):
#     print(ps.getText())
#     print(ps.get('href'))

# Specific Search
# print(soup.find(name="h1",id="name"))
#  REMEMBER to PUT _ after class(since its an attib)
# print(soup.find(name="h3", class_="heading"))

# you can also use - select

# form_tag = soup.select('p')
# max_lenght = form_tag.get("maxlength")
