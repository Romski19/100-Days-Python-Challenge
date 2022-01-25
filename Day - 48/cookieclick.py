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
btn = driver.find_element(By.XPATH, "//*[@id='bigCookie']")


timeout = 5
count_down = 300
time_int = 8

current_time = datetime.datetime.now()
time_change = datetime.timedelta(seconds=count_down)


def check_upgrade(cookie_count):

    if cookie_count >= 330000000:
        btn8 = driver.find_element(By.XPATH,'//*[@id="productPrice7"]')
        btn8.click()
        print(cookie_count)
    elif cookie_count >= 20000000:
        btn7 = driver.find_element(By.XPATH, '//*[@id="product6"]/div[3]')
        btn7.click()
        print(cookie_count)
    elif cookie_count >= 1400000:
        btn6 = driver.find_element(By.XPATH,'//*[@id="productPrice5"]')
        btn6.click()
        print(cookie_count)
    elif cookie_count >= 130000:
        btn5 = driver.find_element(By.XPATH,'//*[@id="product4"]/div[3]')
        btn5.click()
        print(cookie_count)
    elif cookie_count >= 64204:
        btn4 = driver.find_element(By.XPATH,'//*[@id="product3"]/div[3]')
        btn4.click()
        print(cookie_count)
    elif cookie_count >= 1673:
        btn3 = driver.find_element(By.XPATH,'//*[@id="product2"]/div[3]')
        btn3.click()
        print(cookie_count)
    elif cookie_count >= 153:
        btn2 = driver.find_element(By.XPATH, '//*[@id="product1"]/div[3]')
        btn2.click()
        print(cookie_count)
    elif cookie_count >= 40:
        btn1 = driver.find_element(By.XPATH, '//*[@id="product0"]/div[3]')
        btn1.click()
        print(cookie_count)

    else:
        pass


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
    cookie_number = driver.find_element(By.CSS_SELECTOR,'#cookies').text
    str_cookie = cookie_number.split()[0]
    if ',' in str_cookie:
        cookies = int(str_cookie.replace(',',''))
    else:
        cookies = int(str_cookie)
    check_upgrade(cookies)
    

    

driver.quit()

