from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os



chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(60)

driver.get('https://www.facebook.com/')

username = driver.find_element(By.XPATH, '//*[@id="email"]')
username.send_keys("")
password = driver.find_element(By.XPATH, "//*[@id='pass']")
password.send_keys("")
password.send_keys(Keys.ENTER)