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


def start(entry_point):
    return driver().maximize().goto(entry_point)


def terminate() -> None:
    driver().quit()


def driver() -> PyleniumDriver:
    log.info('Fetching the driver')
    return PyleniumDriver()


def get_wrapped_driver() -> webdriver:
    return driver().driver


def find(locator: PyLocator) -> PyElementProxy:
    return driver().find(locator)


def ID(selector: str) -> PyElementProxy:
    return find(PyLocator(By.ID, selector))


def X(selector: str) -> PyElementProxy:
    return find(PyLocator(By.XPATH, selector))
