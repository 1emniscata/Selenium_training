from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
# button = browser.find_element_by_tag_name()
browser.execute_script("return argumnets[0].scrollIntoView(true);", button)
button.click()
