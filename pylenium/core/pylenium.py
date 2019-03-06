from pylenium.config.config import PyleniumConfig
from pylenium.drivers.driver_manager import PyleniumDriver
from pylenium.drivers.driver_strategy import *

config = PyleniumConfig()


def start() -> PyleniumDriver:
    return PyleniumDriver(PyleniumConfig(), ChromeBrowserStrategy())






