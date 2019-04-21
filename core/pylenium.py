from __future__ import annotations

import logging
import os
import time
import typing

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver, webelement

from commands.click_command import ClickCommand
from commands.get_tag_command import GetTagCommand
from commands.get_text_command import GetTextCommand
from commands.should_have_command import ShouldHaveCommand
from conditions.condition import PyCondition
from configuration.config import PyleniumConfig
from core.locators import PyLocator
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


def find(locator: PyLocator) -> PyElementWrapper:
    return driver().find(locator)


def ID(selector: str) -> PyElementWrapper:
    return find(PyLocator(By.ID, selector))


def X(selector: str) -> PyElementWrapper:
    return find(PyLocator(By.XPATH, selector))


# refreshes the underlying web element to prevent staleness etc
def anti_staleness(f):
    def wrapper(*args):
        log.info("refresh reference to the underlying webelement to prevent staleness")
        args[0].driver = driver()
        args[0].wrapped_element = args[0].driver.driver.find_element(args[0].locator.by, args[0].locator.selector)
        return f(*args)
    return wrapper


def ready_state(f):
    def wrapper(*args):
        start = time.time()
        log.info('Waiting for page readystate')
        while time.time() < start + config.explicit_wait_timeout:
            if args[0].driver.execute_javascript('return document.readyState') == 'complete':
                break
        else:
            log.error('page was not ready in time...')
        start = time.time()
        log.info('Waiting for jquery')
        while time.time() < start + config.explicit_wait_timeout:
            if not args[0].driver.execute_javascript('return !!window.jQuery && window.jQuery.active == 0'):
                break
        else:
            log.error('Jquery was not finished in time')
        return f(*args)
    return wrapper


class PyElementWrapper:
    __soft_asserts = {
        "should",
        "should_be",
        "should_have" "should_not",
        "should_not_have",
        "should_not_be" "wait_until" "wait_while",
    }

    def __init__(self, locator):
        self.locator = locator
        self.driver = driver()
        self.wrapped_element: webelement = None

    @ready_state
    @anti_staleness
    def tag_name(self) -> str:
        return GetTagCommand(self).execute()

    @ready_state
    @anti_staleness
    def text(self) -> str:
        return GetTextCommand(self).execute()

    @ready_state
    @anti_staleness
    def should_have(self, conditions: typing.Union[PyCondition, typing.List[PyCondition]]) -> PyElementWrapper:
        return ShouldHaveCommand(self, conditions).execute()

    @ready_state
    @anti_staleness
    def click(self):
        return ClickCommand(self).execute()
