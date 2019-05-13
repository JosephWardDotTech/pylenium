from __future__ import annotations

import abc
import logging
import time
import typing

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pylenium.configuration.config import PyleniumConfig
from pylenium.core.pylenium_wait import PyleniumWait

if typing.TYPE_CHECKING:
    from pylenium.core.pylenium import PyElement, PyleniumDriver

log = logging.getLogger("pylenium")


class Command(metaclass=abc.ABCMeta):
    def __init__(self, driver: PyleniumDriver, element: PyElement):
        self.driver: PyleniumDriver = driver
        self.element: PyElement = element
        self.config = PyleniumConfig()
        self.waiter: WebDriverWait = PyleniumWait(driver=self.driver.driver.web_driver,
                                                  timeout=self.config.explicit_wait_timeout,
                                                  poll_frequency=self.config.polling_interval,
                                                  ignored_exceptions=StaleElementReferenceException)

    def execute(self):
        self._wait_for_page_ready_state()
        self._wait_for_element()
        time.sleep(0.1)

    def _wait_for_element(self) -> PyElement:
        log.info('Resolving the web element for stability')
        log.info('By is: {}'.format(self.element.locator.by))
        log.info('Selector is: {}'.format(self.element.locator.selector))
        self.element = self.waiter.until(expected_conditions.presence_of_element_located(
            (self.element.locator.by, self.element.locator.selector)))
        return self.element

    def _wait_for_page_ready_state(self):
        log.info('Waiting for page source to be stable for up to: {} seconds'.format(self.config.explicit_wait_timeout))
        log.info('Detecting JQuery and waiting for ajax if applicable')
        self.waiter.until(lambda driver: self.driver.execute_javascript("return document.readyState") == "complete")

