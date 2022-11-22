import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    print(y)

    y_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobtn.click()

    submit_btn = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit_btn.click()


finally:
    time.sleep(3)
    browser.quit()
