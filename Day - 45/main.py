import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")
news = response.text

soup = BeautifulSoup(news, "html.parser")
# x = 0
# for headlines in soup.find_all(name="a", class_="titlelink"):
#     x += 1
#     print(f"{x}", headlines.getText())


news_titles = [text.getText() for text in soup.find_all(name="a", class_="titlelink")]    
upvote_score = [int(scores.get_text().split()[0]) for scores in soup.find_all(name="span", class_="score")]


# print(news_titles)
print(upvote_score)

# getting the highest score
highest = max(upvote_score)
# getting the index of the highest upvote score
index_of_highest_score = upvote_score.index(highest)
# getting the title of the highest upvote score
title_of_highest_upvote = news_titles[index_of_highest_score]
print(title_of_highest_upvote)


# ETHICS of WEB SCRAPPING - Check the url/robots.txt
