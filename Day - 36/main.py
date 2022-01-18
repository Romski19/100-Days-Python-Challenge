import requests
import itertools
import os
from twilio.rest import Client

account_sid = os.environ['TW_SID']
auth_token = "7fea9e33da8a4ce86181711592992b85"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_APIKEY = os.environ['STOCK_API']
NEWS_APIKEY = os.environ['NEW_API']

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_APIKEY
}

news_parameters = {
    "apiKey": NEWS_APIKEY,
    "q": COMPANY_NAME

}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
stock_dict = response.json()["Time Series (Daily)"]
two_days_stock = dict(itertools.islice(stock_dict.items(), 2))
yesterday = float(list(two_days_stock.items())[0][1]["4. close"])
a_day_before = float(list(two_days_stock.items())[1][1]["4. close"])

# percentage calculator (increase/decrease)
stock_percentage = int(((yesterday - a_day_before) / a_day_before) * 100)

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

r = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
r.raise_for_status()
news_headline = r.json()["articles"][0]["title"]
news_brief = r.json()["articles"][0]["description"]

# Send a separate message with the percentage change and each article's title and description to your phone number.

client = Client(account_sid, auth_token)

if stock_percentage >= 1:
    message = client.messages \
        .create(
        body=f"TSLA: ▲{stock_percentage}% \n\n "
             f"Headline: {news_headline} \n"
             f"Brief: {news_brief}",
        from_='+14439513240',
        to='+66617164061',
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body=f"TSLA: ▼{stock_percentage}% \n\n "
             f"Headline: {news_headline} \n"
             f"Brief: {news_brief}",
        from_='+14439513240',
        to='+66800785607',
    )

    print(message.status)

    # print(f"TSLA: ▼{abs(stock_percentage)}%")
    # print(f"Headline: {news_headline}")
    # print(f"Brief: {news_brief}")

# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
