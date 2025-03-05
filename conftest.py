import pytest

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, yandex"
    )
    parser.addoption(
        "--base_url",
        action="store",
        default="http://192.168.0.119:8081/",
        help="URL for OpenCart"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--base_url")

    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["firefox", "ff"]:
        options = FFOptions()
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["yandex", "ya"]:
        options = ChromeOptions()
        service = ChromiumService(
            executable_path="/Users/userqa/Documents/drivers/yandexdriver"
        )
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.get(url)
    driver.url = url

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")

