import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Remote(
            command_executor="http://192.168.0.229:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
                "browserVersion": "latest",
                "video": "True",
                "platform": "WIN10",
                "platformName": "windows",
            })
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Remote(
            command_executor="http://192.168.0.229:4444/wd/hub",
            desired_capabilities={
                "browserName": "firefox",
                "browserVersion": "latest",
                "video": "True",
                "platform": "WIN10",
                "platformName": "windows",
            })
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
