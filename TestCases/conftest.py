import pytest
import time
from utils import Utils
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request, browser, url):

    if browser == "CHROME":
        driver = webdriver.Chrome()
    elif browser == "FIREFOX":
        driver = webdriver.Firefox()
    elif browser == "EDGE":
        driver = webdriver.Edge()
    else:
        print("Using default browser FIREFOX.")
        print("Valid browsers are CHROME, FIREFOX, or EDGE.")
        driver = webdriver.Firefox()
        
    wait = WebDriverWait(driver, 15)
    driver.implicitly_wait(15)   
    driver.get(url)
    time.sleep(1)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def url(request):
    return request.config.getoption("--url")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or(report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"'\
                       'onclick="Window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra
        
def pytest_html_report_title(report):
    report.title = "FBtestReport"