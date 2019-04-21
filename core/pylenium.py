from __future__ import annotations

import logging
import os
import threading
from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from configuration.config import PyleniumConfig
from core.locators import PyLocator
from pages.page_object import PyPage
from proxy.proxy import PyElementProxy
from web_drivers.pylenium_driver import PyleniumDriver

log = logging.getLogger("pylenium")
log.setLevel(logging.INFO)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ascii:
with open(os.path.join(ROOT_DIR, "resources", "ascii.txt")) as art:
    for line in art:
        print(line)

# global configuration object
config = PyleniumConfig()
t_drivers = threading.local()


def start(entry_point: Union[str, PyPage]) -> Union[PyleniumDriver, PyPage]:
    return driver().maximize().goto(entry_point)


def terminate() -> None:
    t_drivers.threaded_driver.quit()
    breakpoint()


def driver() -> PyleniumDriver:
    if hasattr(t_drivers, 'threaded_driver'):
        return t_drivers.threaded_driver
    else:
        t_drivers.threaded_driver = PyleniumDriver()
        return t_drivers.threaded_driver


def get_wrapped_driver() -> webdriver:
    return driver().driver


def find(locator: PyLocator) -> PyElementProxy:
    return driver().find(locator)


def ID(selector: str) -> PyElementProxy:
    return find(PyLocator(By.ID, selector))


def X(selector: str) -> PyElementProxy:
    return find(PyLocator(By.XPATH, selector))
