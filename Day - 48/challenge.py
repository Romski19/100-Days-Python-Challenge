from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Romski")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("Asomar")
e_mail =driver.find_element_by_name("email")
e_mail.send_keys("testingtestromeo@gmail.com")

btn = driver.find_element_by_class_name("btn-block")
btn.click()