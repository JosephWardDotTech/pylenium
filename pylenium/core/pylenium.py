from __future__ import annotations

import logging
import os
import typing

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

import pylenium.drivers.web_driver_runner as runner
from pylenium.commands.click_command import ClickCommand
from pylenium.commands.get_tag_command import GetTagCommand
from pylenium.commands.get_text_command import GetTextCommand
from pylenium.commands.should_have_command import ShouldHaveCommand
from pylenium.conditions.condition import PyCondition
from pylenium.configuration.config import PyleniumConfig
from pylenium.core.locators import PyLocator
from pylenium.drivers.driver import PyleniumDriver

log = logging.getLogger("pylenium")
log.setLevel(logging.INFO)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ascii:
with open(os.path.join(ROOT_DIR, "resources", "ascii.txt")) as art:
    for line in art:
        print(line)

config = PyleniumConfig()


def get_config() -> PyleniumConfig:
    return config


def start(entry_point):
    """
    Entry point for testing, this is the window into pylenium and will instantiate a new thread local driver
    if necessary, if a driver is already assigned to the executing thread, it will return such driver
    :param entry_point: The url to load to begin testing: default -> 'localhost:8080'
    :return: thread-local scoped driver as per your configurations
    """
    return get_pylenium_driver().start(entry_point)


def go(entry_point):
    """
    Interchangeable with start()
    """
    return start(entry_point)


def open(entry_point):
    """
    Interchangeable with start()
    """
    return start(entry_point)


def terminate() -> None:
    get_pylenium_driver().quit()


def get_pylenium_driver() -> PyleniumDriver:
    return runner.web_driver_container.get_pylenium_driver()


def find(locator: PyLocator) -> PyElement:
    return get_pylenium_driver().find(locator)


def ID(selector: str) -> PyElement:
    return get_pylenium_driver().find(PyLocator(By.ID, selector))


def X(selector: str) -> PyElement:
    return find(PyLocator(By.XPATH, selector))


class PyElement:
    __soft_asserts = {
        "should",
        "should_be",
        "should_have",
        "should_not",
        "should_not_have",
        "should_not_be",
        "wait_until",
        "wait_while"
    }

    def __init__(self, locator):
        self.locator = locator
        self.wrapped_element: webelement = None

    def tag_name(self) -> str:
        return GetTagCommand(get_pylenium_driver(), self).execute()

    def text(self) -> str:
        return GetTextCommand(get_pylenium_driver(), self).execute()

    def should_have(self, conditions: typing.Union[PyCondition, typing.List[PyCondition]]) -> PyElement:
        return ShouldHaveCommand(get_pylenium_driver(), self, conditions).execute()

    def click(self):
        return ClickCommand(get_pylenium_driver(), self).execute()
