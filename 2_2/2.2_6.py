import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    y_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()


    radiobtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()

    submit_btn = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()

