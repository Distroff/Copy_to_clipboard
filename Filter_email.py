from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://corp.mariinsky.ru/smail"
    browser = webdriver.Chrome()
    browser.get(link)

    srch = browser.find_element(By.ID, "filter2")
    srch.send_keys(r'калашни')

    time.sleep(600)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
