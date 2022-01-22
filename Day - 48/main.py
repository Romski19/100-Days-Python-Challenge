from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.gmanetwork.com/news/')
just_in = driver.find_elements_by_class_name("just-in-story")

for j_news in just_in:
    print(j_news.text)

# driver.close()
driver.quit()