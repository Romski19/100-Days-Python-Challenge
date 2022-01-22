from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://en.wikipedia.org/wiki/Main_Page')

articles = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

print(articles.text)

driver.quit()
