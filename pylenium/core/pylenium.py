import threading

from pylenium.config.config import PyleniumConfig
from pylenium.drivers.driver_manager import PyleniumDriver
from pylenium.drivers.driver_strategy import *

config = PyleniumConfig()
driver = threading.local()
driver.x = None


def start(url: str) -> PyleniumDriver:
    if isinstance(driver.x, PyleniumDriver):
        return driver.x.goto(url)
    print('Hey, you have a thread local driver duh!')
    driver.x = PyleniumDriver(PyleniumConfig(), ChromeBrowserStrategy())
    return driver.x.goto(url)
