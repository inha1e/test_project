import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language:
        print(f"\nstart test for {language} language..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
        time.sleep(2)
    else:
        raise pytest.UsageError("Please use --language (example: --language=fr)")
    yield browser
    print("\nquit browser..")
    browser.quit()