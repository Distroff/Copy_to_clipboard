from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "https://f.gamt.su"
    browser = webdriver.Chrome()
    browser.get(link)

    filename = browser.find_element(By.ID, "file_select")
    # filename.send_keys(r"D:\Download\24745.txt")
    filename.send_keys(r"V:\DATA\2\B\1\1B21208500_Корсар_20240703.mov")

    flag = WebDriverWait(browser, 1200).until(EC.text_to_be_present_in_element((By.ID, 'direct_link'), 'Прямая ссылка'))
    link = browser.find_element(By.ID, 'direct_link_text').text
    print(link) # works
    time.sleep(600)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
