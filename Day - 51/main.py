from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os



chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(60)

driver.get('https://th.speedtest.net/')
btn = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
btn.click()

# Twitter Driver
# tw = driver.get('https://twitter.com/i/flow/login')

