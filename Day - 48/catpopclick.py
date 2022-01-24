from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://popcat.click/")
btn = driver.find_element_by_class_name("cat-img ")
x = 5000

while x != 0:
    btn.click()
    x -=1