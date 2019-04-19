from __future__ import annotations
import threading
from typing import List, Union

from selenium.webdriver.common.by import By

from config.config import PyleniumConfig
from core.web_elements import PyElement
from drivers.pylenium_driver import PyleniumDriver
from page_objects.page_object import PyPage

# global config object
config = PyleniumConfig()


def start(entry_point: Union[str, PyPage]) -> PyleniumDriver:
    return PyleniumDriver().maximize().goto(entry_point)


def terminate() -> None:
    PyleniumDriver().quit()


def get_driver() -> PyleniumDriver:
    return PyleniumDriver()


def find(by: By, selector: str) -> PyElement:
    return PyleniumDriver().find(by, selector)


def find_all(by: By, selector: str) -> List[PyElement]:
    return PyleniumDriver().find_all((by, selector))
