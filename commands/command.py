from __future__ import annotations

import abc
import logging
import typing
from typing import Union

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from core.pylenium_wait import PyleniumWait

if typing.TYPE_CHECKING:
    from core.pylenium import PyElement, config, PyleniumDriver

log = logging.getLogger("pylenium")


class Command(metaclass=abc.ABCMeta):
    def __init__(self, driver: PyleniumDriver, element: PyElement):
        self.driver: PyleniumDriver = driver
        self.element: PyElement = element
        self.waiter: WebDriverWait = PyleniumWait(driver=self.driver,
                                                  timeout=config.explicit_wait_timeout,
                                                  poll_frequency=config.polling_timeout,
                                                  ignored_exceptions=StaleElementReferenceException)

    @abc.abstractmethod
    def execute(self) -> Union[str, PyElement, bool, int]:
        pass

    def wait_for_element(self) -> PyElement:
        self.element.wrapped_element = self.waiter.until(expected_conditions.presence_of_element_located(
            self.element.locator))
        return self.element

    def wait_for_page_to_be_ready(self):
        pass
