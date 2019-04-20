from __future__ import annotations

import logging
from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from config.config import PyleniumConfig
from core.elements import PyElement
from core.locators import PyLocator
from drivers.pylenium_driver import PyleniumDriver
from page_objects.page_object import PyPage

log = logging.getLogger("pylenium")
log.setLevel(logging.INFO)

# ascii:
with open("resources/ascii.txt") as art:
    for line in art:
        print(line)

# global config object
config = PyleniumConfig()


def start(entry_point: Union[str, PyPage]) -> Union[PyleniumDriver, PyPage]:
    return PyleniumDriver().maximize().goto(entry_point)


def terminate() -> None:
    PyleniumDriver().quit()


def get_driver() -> PyleniumDriver:
    return PyleniumDriver()


def get_wrapped_driver() -> webdriver:
    return PyleniumDriver().driver


def find(locator: PyLocator) -> PyElement:
    return PyleniumDriver().find(locator)


def ID(selector: str) -> PyElement:
    return find(PyLocator(By.ID, selector))
