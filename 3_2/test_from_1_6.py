import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestOld(unittest.TestCase):

    @staticmethod
    def _validate_input(item):
        if not item.get_attribute("required"):
            raise NoSuchElementException

    def page_stuff(self, link) -> str:

        options = Options()
        options.headless = True

        browser = webdriver.Chrome(options=options)
        browser.get(link)

        first_name = browser.find_element(By.CLASS_NAME, "form-control.first")
        self._validate_input(first_name)
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CLASS_NAME, "form-control.second")
        self._validate_input(last_name)
        last_name.send_keys("Pupkin")

        email = browser.find_element(By.CLASS_NAME, "form-control.third")
        self._validate_input(email)
        email.send_keys("pupkin@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        return welcome_text

    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        msg = "Congratulations! You have successfully registered!"
        self.assertEqual(self.page_stuff(link), msg, "Problems")

    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        msg = "Congratulations! You have successfully registered!"
        self.assertEqual(self.page_stuff(link), msg, "Problems")

# if __name__ == "__main__":
#     unittest.main()