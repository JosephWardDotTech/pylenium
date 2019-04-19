from __future__ import annotations

import threading
from typing import Union, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from config.config import PyleniumConfig
from core.elements import PyElement
from drivers.driver_strategy import ChromeBrowserStrategy, FirefoxBrowserStrategy
from page_objects.page_object import PyPage

config = PyleniumConfig()
threaded_driver = threading.local()


class PyleniumDriver:
    def __init__(self):
        if not hasattr(threaded_driver, 'driver'):
            print('This thread has no driver, lets make a new one!')
            self._driver = self._get_browser_strategy().instantiate()
            threaded_driver.driver = self._driver
        else:
            self._driver = threaded_driver.driver

    @property
    def driver(self) -> webdriver:
        return self._driver

    @driver.setter
    def driver(self, value):
        raise Exception('Pylenium manages the driver(s), do not attempt to change the driver reference')

    def goto(self, entry_point: Union[str, PyPage]) -> PyleniumDriver:
        self.driver.get(entry_point)
        return self

    def maximize(self) -> PyleniumDriver:
        self.driver.maximize_window()
        return self

    def quit(self):
        self.driver.quit()
        del threaded_driver.driver

    def url(self) -> str:
        return self.driver.current_url

    def find(self, by: By, selector: str) -> PyElement:
        return self.driver.find_element(by.lookup())

    def find_all(self, by) -> List[PyElement]:
        return self.driver.find_elements(by.lookup())

    def exec_js(self, command: str) -> PyleniumDriver:
        return self

    @staticmethod
    def _get_browser_strategy():
        if config.browser.value == 'chrome':
            return ChromeBrowserStrategy()
        elif config.browser.value == 'firefox':
            return FirefoxBrowserStrategy()
