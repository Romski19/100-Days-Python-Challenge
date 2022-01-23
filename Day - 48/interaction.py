from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://en.wikipedia.org/wiki/Main_Page')
# fist challenge
# articles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# print(articles.text)

articles = driver.find_element_by_link_text("All portals")

# to interact with element - click
# articles.click()

# input keys
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()
