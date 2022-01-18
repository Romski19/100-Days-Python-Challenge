from pydoc import source_synopsis
from socket import timeout
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

WEB_SITE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_PAGE = "Day - 45/site.html"
SAVED_MOVIES = "Day - 45/saved.txt"


# response = requests.get(WEB_SITE)

# content = response.text

# soup = BeautifulSoup(content, "html.parser")

# data = soup.findAll("a", rel="noopener noreferrer")
# movielist = []
# for txt in data:
#     movielist.append(txt)
#     print(movielist[2])



def get_web_page():

    session = HTMLSession()
    response = session.get(WEB_SITE)
    # Run JavaScript code on webpage
    response.html.render(timeout=8000)

    with open(WEB_PAGE, mode="w", encoding="UTF-8") as save_site:
        save_site.write(response.html.html)


def read_web_page():
    try:
        open(WEB_PAGE)
    except FileNotFoundError:
        get_web_page()
    finally:    
        with open(WEB_PAGE, mode="r", encoding="windows-1252") as site:
            content = site.read()
        return BeautifulSoup(content, "html.parser")

# result = read_web_page()

with open(WEB_PAGE, "r") as read_wp:
    content = read_wp.read()

soup = BeautifulSoup(content, "html.parser")
x = 101
for title in reversed(soup.find_all("h3")):
    movies = title.getText()
    with open(SAVED_MOVIES, "a") as saved_movies:
        saved_movies.write(movies + "\n")



