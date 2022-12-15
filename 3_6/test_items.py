import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_btn_exists(browser):
    browser.implicitly_wait(5)

    browser.get(link)
    time.sleep(30)
    btn_exists = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed()
    assert btn_exists
