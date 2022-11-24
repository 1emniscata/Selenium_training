import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def answer():
    return math.log(int(time.time()))


# link = "https://stepik.org/lesson/236895/step/1"
creds = {"mail": "aleksandrsuzen@gmail.com", "password": "Durak14open20001"}


@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_authorization(browser, link):
    # def test_authorization(browser):

    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.ID, "ember32").click()

    browser.find_element(By.ID, "id_login_email").send_keys(creds.get("mail"))
    browser.find_element(By.ID, "id_login_password").send_keys(creds.get("password"))
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

    # browser.find_element(By.ID, "ember90").send_keys(answer)
    # try:
    #     browser.find_element(By.CLASS_NAME, "again-btn.white").click()
    #     # browser.find_element(By.CLASS_NAME, "again-btn.white").click()
    #
    # except NoSuchElementException:
    #     pass

    time.sleep(13)

    # WebDriverWait(browser, 15).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")))

    # WebDriverWait(browser, 25).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")))

    # browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(answer)

    # browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(
    #     answer())
    browser.find_element(By.TAG_NAME, "textarea").send_keys(answer())

    # time.sleep(5)
    # submit_btn = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    # time.sleep(5)
    # submit_btn.click()

    # time.sleep(15)

    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    time.sleep(5)

    msg = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert msg == "Correct!"

    # time.sleep(300)

# ember32

# id_login_email
# id_login_password
# class sign-form__btn button_with-loader


# 'what they seem! OvO'
