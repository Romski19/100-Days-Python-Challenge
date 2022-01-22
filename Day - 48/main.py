from hashlib import new
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.gmanetwork.com/news/')
just_in = driver.find_elements_by_class_name("just-in-story")
news_time = driver.find_elements_by_class_name("time")

news = {}

for n in range(len(just_in)):
    news[n] = {
        "time": news_time[n].text,
        "news": just_in[n].text,
    }

print(news)

# driver.close()
driver.quit()