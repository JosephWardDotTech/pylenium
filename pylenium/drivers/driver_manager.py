from __future__ import annotations

from typing import List

from selenium.webdriver.common.by import By

from pylenium.config.config import PyleniumConfig
from pylenium.core.pyelement import PyElement
from pylenium.drivers.driver_strategy import *


class PyleniumDriver(object):
    def __init__(self,
                 config: PyleniumConfig,
                 driver_strategy: AbstractBrowserStrategy = ChromeBrowserStrategy()):
        self._config = config
        self.driver_strategy = driver_strategy
        self._driver = self.driver_strategy.instantiate()

    @property
    def driver(self) -> webdriver:
        return self._driver

    @driver.setter
    def driver(self, value):
        self._driver = value
        if self._config.browser_maximized:
            self.maximize()

    def goto(self, url: str) -> PyleniumDriver:
        self.driver.get(url)
        return self

    def maximize(self) -> PyleniumDriver:
        self.driver.maximize_window()
        return self

    def quit(self):
        self.driver.quit()

    def url(self) -> str:
        return self.driver.current_url

    def find(self, by: By) -> PyElement:
        return self.driver.find_element(by)

    def find_all(self, by: By) -> List[PyElement]:
        return self.driver.find_elements(by)
