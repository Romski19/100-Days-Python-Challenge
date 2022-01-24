import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')
btn = driver.find_element(By.XPATH, "//*[@id='bigCookie']")
# timeout = 5
# end = 300   # 5 minutes from now



# def game():
#     interval_time = time.time()
#     while time.time() < interval_time + timeout:
#         test = 0
#         btn.click()
#         if test == timeout:
#             break
#         test -= 1

# main_time = time.time()
# while time.time() < main_time + end:
#     test = 0
#     game()
#     if test == end:
#         break
#     test -= 1


timeout = 5
count_down = 300
time_int = 8

current_time = datetime.datetime.now()
time_change = datetime.timedelta(seconds=count_down)

def game():
        # x = 0
        interval_time = time.time()
        while time.time() < interval_time + time_int:
            test = 0
            # x += 1
            # print(x) 
            btn.click()
            if test == time_int:
                break
            test -= 1
            
while current_time != time_change:
    game()
    time.sleep(timeout)
    # check the score
    driver.find_element(By.XPATH, '//*[@id="product0"]').click()
    

driver.quit()

# do something