from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://f.gamt.su"
    browser = webdriver.Chrome()
    browser.get(link)

    filename = browser.find_element(By.ID, "file_select")
    filename.send_keys(r"V:\DATA\2\B\1\1B21220300_Бахчисарайский_Фонтан_20240927.mov")

    time.sleep(600)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
