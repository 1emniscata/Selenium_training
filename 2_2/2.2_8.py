import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")

try:
    browser.get("https://suninjuly.github.io/file_input.html")
    elements = browser.find_elements(By.CLASS_NAME, "form-control")
    for element in elements:
        element.send_keys("T")

    # first_name = browser.find_element(By.CLASS_NAME, "form-control.first")
    # first_name.send_keys("Ivan")
    #
    # last_name = browser.find_element(By.CLASS_NAME, "form-control.second")
    # last_name.send_keys("Pupkin")
    #
    # email = browser.find_element(By.CLASS_NAME, "form-control.third")
    # email.send_keys("pupkin@gmail.com")

    file_btn = browser.find_element(By.CSS_SELECTOR, "#file")
    file_btn.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()