from __future__ import annotations

import abc
import logging
import time
import typing
from typing import Union

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from configuration.config import PyleniumConfig
from core.pylenium_wait import PyleniumWait

if typing.TYPE_CHECKING:
    from core.pylenium import PyElement, PyleniumDriver

log = logging.getLogger("pylenium")


class Command(metaclass=abc.ABCMeta):
    def __init__(self, driver: PyleniumDriver, element: PyElement):
        self.driver: PyleniumDriver = driver
        self.element: PyElement = element
        self.config = PyleniumConfig()
        self.waiter: WebDriverWait = PyleniumWait(driver=self.driver.driver.web_driver,
                                                  timeout=self.config.explicit_wait_timeout,
                                                  poll_frequency=self.config.polling_timeout,
                                                  ignored_exceptions=StaleElementReferenceException)

    @abc.abstractmethod
    def execute(self) -> Union[str, PyElement, bool, int]:
        pass

    def wait_for_element(self) -> PyElement:
        log.info('Resolving the web element for stability')
        self.element.wrapped_element = self.waiter.until(expected_conditions.presence_of_element_located(
            (self.element.locator.by, self.element.locator.selector)))
        return self.element

    def wait_for_page_to_be_ready(self):
        log.info('Waiting for page source to be stable')
        self.waiter.until(lambda driver: self.driver.execute_javascript("return document.readyState") == 0)
        log.info('Detecting JQuery and waiting for ajax if applicable')
        self.waiter.until(lambda driver: self.driver.execute_javascript("return jQuery.active == 0"))
