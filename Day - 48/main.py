from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com')

# driver.close()
driver.quit()