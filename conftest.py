import logging
import pytest
import allure
import json
import os

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, yandex",
    )
    parser.addoption(
        "--base_url",
        action="store",
        default="http://192.168.0.119:8081/",
        help="URL for OpenCart",
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        if rep.outcome != "passed":
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            item.session.config.driver.save_screenshot(screenshot_path)
            allure.attach(
                item.session.config.driver.get_screenshot_as_png(),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
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

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON,
    )

    driver.test_name = request.node.name
    driver.log_level = logging.INFO

    driver.maximize_window()
    driver.get(url)
    driver.url = url

    yield driver

    if getattr(request.node, "status", None) == "failed":
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG,
        )

    driver.quit()


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")
