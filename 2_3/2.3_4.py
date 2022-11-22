import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    y_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_input.send_keys(y)

    submit_btn = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
