from __future__ import annotations

import sys
from typing import List, Union
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from config.config import PyleniumConfig
from core.elements import PyElement
from drivers.pylenium_driver import PyleniumDriver
from page_objects.page_object import PyPage

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger('pylenium')
log.setLevel(logging.INFO)


# global config object
config = PyleniumConfig()


def start(entry_point: Union[str, PyPage]) -> PyleniumDriver:
    return PyleniumDriver().maximize().goto(entry_point)


def terminate() -> None:
    PyleniumDriver().quit()


def get_driver() -> PyleniumDriver:
    return PyleniumDriver()


def get_wrapped_driver() -> webdriver:
    return PyleniumDriver().driver


def find(by: By, selector: str) -> PyElement:
    return PyleniumDriver().find(by, selector)


def find_all(by: By, selector: str) -> List[PyElement]:
    return PyleniumDriver().find_all((by, selector))
