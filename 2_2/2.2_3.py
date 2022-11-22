import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    submit_btn = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit_btn.click()

finally:
    time.sleep(3)
    browser.quit()