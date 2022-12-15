import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(pytestconfig):
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": f"{pytestconfig.getoption('language')}"})
    # options.add_argument("--headless")
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")
