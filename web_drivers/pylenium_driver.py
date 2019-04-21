from __future__ import annotations

import logging
import threading
from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from configuration.config import PyleniumConfig
from core.elements import PyElement
from core.locators import PyLocator
from exceptions.exceptions import PyPageException
from pages.page_object import PyPage
from proxy.proxy import ElementFinder
from web_drivers.driver_strategy import ChromeBrowserStrategy, FirefoxBrowserStrategy

log = logging.getLogger("pylenium")
config = PyleniumConfig()
threaded_driver = threading.local()


class PyleniumDriver:
    def __init__(self):
        if not hasattr(threaded_driver, "driver"):
            log.info(
                "Thread: {} has no driver, instantiating a new driver for use...".format(
                    threading.get_ident()
                )
            )
            self._driver = self._get_browser_strategy().instantiate()
            threaded_driver.driver = self._driver
        else:
            self._driver = threaded_driver.driver

    @property
    def driver(self) -> webdriver:
        return self._driver

    @driver.setter
    def driver(self, value):
        raise Exception(
            "Pylenium manages the driver(s), do not attempt to change the driver reference"
        )

    def goto(self, entry_point: Union[str, PyPage]) -> Union[PyleniumDriver, PyPage]:
        url = (
            PyleniumConfig().base_url + entry_point
            if isinstance(entry_point, str)
            else entry_point.url
        )
        if not url:
            raise PyPageException(
                "The url was empty, did your page object specify the self.url parameter?"
            )
        else:
            self.driver.get(url)
            if isinstance(entry_point, PyPage):
                return entry_point
        return self

    def maximize(self) -> PyleniumDriver:
        self.driver.maximize_window()
        return self

    def quit(self):
        log.info("Quit called, terminating the browser")
        self.driver.quit()
        del threaded_driver.driver

    def url(self) -> str:
        return self.driver.current_url

    def find(self, locator: PyLocator) -> PyElement:
        return ElementFinder.wrap(self, locator)

    def X(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.XPATH, identifier))

    def ID(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.ID, identifier))

    def CSS(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.CSS_SELECTOR, identifier))

    def PLT(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.PARTIAL_LINK_TEXT, identifier))

    def LT(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.LINK_TEXT, identifier))

    def NAME(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.NAME, identifier))

    def TAG_NAME(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.TAG_NAME, identifier))

    def CLASS(self, identifier: str) -> PyElement:
        return self.find(PyLocator(By.CLASS_NAME, identifier))

    @staticmethod
    def _get_browser_strategy():
        if config.browser.value == "chrome":
            log.info("Creating a chrome browser instance")
            return ChromeBrowserStrategy()
        elif config.browser.value == "firefox":
            return FirefoxBrowserStrategy()
