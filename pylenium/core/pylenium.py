import threading
from typing import List

from selenium.webdriver.common.by import By

from pylenium.config.config import PyleniumConfig
from pylenium.core.pyelement import PyElement
from pylenium.drivers.driver_manager import PyleniumDriver
from pylenium.drivers.driver_strategy import *


config = PyleniumConfig()
driver = threading.local()
driver.x = None


# Test entry point! just simply... get started, provide us a URL and we will get you a thread local driver if necessary!
def start(url: str) -> PyleniumDriver:
    if isinstance(driver.x, PyleniumDriver):
        return driver.x.goto(url)
    driver.x = PyleniumDriver(PyleniumConfig(), ChromeBrowserStrategy()).maximize()
    return driver.x.goto(url)


def terminate() -> None:
    driver.x.quit()


def find(by: By, selector: str) -> PyElement:
    return driver.x.find_element((by, selector))


def find_all(by: By, selector: str) -> List[PyElement]:
    return driver.x.find_element((by, selector))
