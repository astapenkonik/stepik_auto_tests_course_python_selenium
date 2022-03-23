from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new= browser.window_handles[1]

    browser.switch_to.window(new)

    x = browser.find_element_by_id("input_value").text
    summ = log(abs(12 * sin(int(x))))

    pole = browser.find_element_by_id("answer")
    pole.send_keys(str(summ))

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()