from cgitb import text
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(60)
driver.get('https://orteil.dashnet.org/cookieclicker/')
btn = driver.find_element(By.XPATH,"//*[@id='bigCookie']")


timeout = 5
count_down = 300
time_int = 8

current_time = datetime.datetime.now()
time_change = datetime.timedelta(seconds=count_down)


def check_upgrade():
    add_ons_list = driver.find_elements(By.CSS_SELECTOR, "#products .unlocked.enabled")
    add_ons_list[-1].click()

def game():
        interval_time = time.time()
        while time.time() < interval_time + time_int:
            test = 0
            btn.click()
            if test == time_int:
                break
            test -= 1
            
while current_time != time_change:
    game()
    time.sleep(timeout)
    # check the score
    # cookie_number = driver.find_element_by_id("bigCookie").text
    # str_cookie = cookie_number.split()[0]
    # if ',' in str_cookie:
    #     cookies = int(str_cookie.replace(',',''))
    # else:
    #     cookies = int(str_cookie)
    check_upgrade()
    

    

driver.quit()

