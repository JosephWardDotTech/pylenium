import threading

from selenium.webdriver.remote import webelement

from pylenium.config.config import PyleniumConfig
from pylenium.drivers.driver_manager import PyleniumDriver
from pylenium.drivers.driver_strategy import *
from pylenium.page_objects.py_locator import PyLocator

config = PyleniumConfig()
driver = threading.local()
driver.x = None


# Test entry point! just simply... get started, provide us a URL and we will get you a thread local driver if necessary!
def start(url: str) -> PyleniumDriver:
    if isinstance(driver.x, PyleniumDriver):
        return driver.x.goto(url)
    print('Calling start when the thread already contains a driver, getting threaded driver instead')
    driver.x = PyleniumDriver(PyleniumConfig(), ChromeBrowserStrategy())
    return driver.x.goto(url)


def find(py_locator: PyLocator) -> webelement:
    return driver.x.find_element(py_locator.lookup())