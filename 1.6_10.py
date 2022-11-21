from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


def validate_input(item):
    if not item.get_attribute("required"):
        raise NoSuchElementException


browser = webdriver.Chrome()

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    first_name = browser.find_element(By.CLASS_NAME, "form-control.first")
    validate_input(first_name)
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CLASS_NAME, "form-control.second")
    validate_input(last_name)
    last_name.send_keys("Pupkin")

    email = browser.find_element(By.CLASS_NAME, "form-control.third")
    validate_input(email)
    email.send_keys("pupkin@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()


