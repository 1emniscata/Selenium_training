import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()

    browser.execute_script("window.scrollTo(0, 500)")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    y_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_input.send_keys(y)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(3)
    browser.quit()

