'''
THIS FILE CONTAINS THE FIXTURES FOR ALL THE TESTS
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import os


# -----------------------------------------------------------------------------------------------------------------------
# Start browser through manual choice
# -----------------------------------------------------------------------------------------------------------------------

@pytest.fixture
def browser(request):
    test_name = request.node.name

    print(
        "\033[93m\n********************************************************************\n\033[0m"
        f"\033[93mSTART BROWSER FOR TEST:\033[0m \033[92m{test_name}\033[0m\n"
        "\033[93m********************************************************************\n\033[0m"
    )

    user_language = request.config.getoption("language")
    headless_mode = request.config.getoption("--headless")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    options.add_argument("--ignore-certificate-errors-spki-list")
    options.add_argument("--ignore-ssl-errors=true")
    options.add_argument("--start-maximized")
    # options.add_argument("--start-fullscreen")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")

    if headless_mode:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    # driver.execute_script("window.localStorage.clear();")
    # driver.execute_script("window.sessionStorage.clear();")
    yield driver
    print(
        "\033[93m\n********************************************************************\n\033[0m"
        f"\033[93mQUIT BROWSER FOR TEST:\033[0m \033[92m{test_name}\033[0m\n"
        "\033[93m********************************************************************\n\033[0m"
    )
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Specify the language for the test run",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode",
    )

# -----------------------------------------------------------------------------------------------------------------------
# Start browser through Selenoid
# -----------------------------------------------------------------------------------------------------------------------

# def pytest_addoption(parser):
#     parser.addoption("--executor", action="store", default="localhost")
#
#
# @pytest.fixture(params=["chrome", "firefox"])
# def browser(request):
#     executor = request.config.getoption("--executor")
#     browser_name = request.param
#     if browser_name == "chrome":
#         options = webdriver.ChromeOptions()
#         options.set_capability("browserVersion", "120.0")
#         options.set_capability("selenoid:options", {"enableVNC": True})
#         options.set_capability("selenoid:options", {"screenResolution": "1280x1024x24"})
#         options.set_capability("selenoid:options", {"enableVideo": False})
#     elif browser_name == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.set_capability("browserVersion", "120.0")
#         options.set_capability("selenoid:options", {"enableVNC": True})
#         options.set_capability("selenoid:options", {"screenResolution": "1280x1024x24"})
#         options.set_capability("selenoid:options", {"enableVideo": False})
#
#     driver = webdriver.Remote(
#         command_executor=f"http://{executor}:4444/wd/hub",
#         options=options,
#     )
#     yield driver
#     driver.quit()


# -----------------------------------------------------------------------------------------------------------------------
# Start browser through Selenium Grid
# -----------------------------------------------------------------------------------------------------------------------

#
# def pytest_addoption(parser):
#     parser.addoption("--executor", action="store", default="localhost")
#
#
# @pytest.fixture(params=["chrome", "firefox", "MicrosoftEdge"])
# def browser(request):
#     executor = request.config.getoption("--executor")
#     browser_name = request.param
#     if browser_name == "chrome":
#         options = webdriver.ChromeOptions()
#         options.set_capability("browserName", "chrome")
#         options.set_capability("platformName", "Windows 10")
#
#     elif browser_name == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.set_capability("browserName", "firefox")
#         options.set_capability("platformName", "Windows 10")
#
#     elif browser_name == "MicrosoftEdge":
#         options = webdriver.FirefoxOptions()
#         options.set_capability("browserName", "MicrosoftEdge")
#         options.set_capability("platformName", "Windows 10")
#
#     driver = webdriver.Remote(
#         command_executor=f"http://{executor}:4444",
#         options=options,
#     )
#     yield driver
#     driver.quit()

# -----------------------------------------------------------------------------------------------------------------------
# Start browser through BrowserStack
# Before run: Create new account in BrowserStack and insert your BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY
# -----------------------------------------------------------------------------------------------------------------------

# URL = "https://hub-cloud.browserstack.com/wd/hub"
# BUILD_NAME = "browserstack-build-1"
# BROWSERSTACK_USERNAME = "YOUR_USERNAME"
# BROWSERSTACK_ACCESS_KEY = "YOUR_ACCESS_KEY"
#
# @pytest.fixture(params=["chrome", "firefox", "safari"])
# def browser(request):
#     browser_name = request.param
#     options = None
#
#     if browser_name == "chrome":
#         options = webdriver.ChromeOptions()
#         options.set_capability("browserName", "chrome")
#         options.set_capability("browserVersion", "103.0")
#         options.set_capability("os", "Windows")
#         options.set_capability("osVersion", "11")
#         options.set_capability("sessionName", "BStack Python sample parallel")
#         options.set_capability("buildName", BUILD_NAME)
#         options.set_capability("bstack:options", {
#             "userName": BROWSERSTACK_USERNAME,
#             "accessKey": BROWSERSTACK_ACCESS_KEY
#         })
#     elif browser_name == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.set_capability("browserName", "firefox")
#         options.set_capability("browserVersion", "102.0")
#         options.set_capability("os", "Windows")
#         options.set_capability("osVersion", "10")
#         options.set_capability("sessionName", "BStack Python sample parallel")
#         options.set_capability("buildName", BUILD_NAME)
#         options.set_capability("bstack:options", {
#             "userName": BROWSERSTACK_USERNAME,
#             "accessKey": BROWSERSTACK_ACCESS_KEY
#         })
#     elif browser_name == "safari":
#         options = webdriver.SafariOptions()
#         options.set_capability("browserName", "safari")
#         options.set_capability("browserVersion", "14.1")
#         options.set_capability("os", "OS X")
#         options.set_capability("osVersion", "Big Sur")
#         options.set_capability("sessionName", "BStack Python sample parallel")
#         options.set_capability("buildName", BUILD_NAME)
#         options.set_capability("bstack:options", {
#             "userName": BROWSERSTACK_USERNAME,
#             "accessKey": BROWSERSTACK_ACCESS_KEY
#         })
#
#     driver = webdriver.Remote(
#         command_executor=URL,
#         options=options
#     )
#     yield driver
#     driver.quit()
