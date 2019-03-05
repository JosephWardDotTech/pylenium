from __future__ import annotations
import os

from selenium.webdriver import DesiredCapabilities
from enum import Enum


# Pyleniums possible web element lookup strategy (by default)
class Selector(Enum):
    CSS = 'CSS'
    XPATH = 'XPATH'
    ID = 'ID'


# Pyleniums possible browser (by default)
class Browser(Enum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'


# Pyleniums page loading strategy (by default)
# This is basically how quickly Pylenium will attempt to proceed on page loads and click follow up actions
class PageLoadStrategy(Enum):
    NORMAL = 'normal'
    FAST = 'fast'
    EAGER = 'eager'


class PyleniumConfig(object):
    __browser = os.getenv('pylenium.browser', Browser.CHROME)
    __headless = os.getenv('pylenium.headless', False)
    __remote = os.getenv('pylenium.remote', False)
    __browser_size = os.getenv('pylenium.browser_size', '1366x768')
    __browser_version = os.getenv('pylenium.browser_version', None)
    __browser_position = os.getenv('pylenium.browser_position', None)
    __browser_maximized = os.getenv('pylenium.maximized', True)
    __wdm_enabled = os.getenv('pylenium.wdm_enabled', True)
    __browser_binary = os.getenv('pylenium.browser_binary', '')
    __page_load_strategy = os.getenv('pylenium.page_load_strategy', PageLoadStrategy.NORMAL)
    __desired_capabilities = DesiredCapabilities()
    __base_url = os.getenv('pylenium.base_url', 'http://localhost:8080')
    __explicit_wait_timeout = os.getenv('pylenium.wait_timeout', 15000)
    __polling_timeout = os.getenv('pylenium.polling_timeout', 200)
    __capture_screenshot = os.getenv('pylenium.screenshot', True)
    __capture_pagesource = os.getenv('pylenium.pagesource', True)
    __javascript_clicking = os.getenv('pylenium.js_click', False)
    __javascript_sendkeys = os.getenv('pylenium.js_sendkeys', False)
    __selector_default = Selector.CSS

    @property
    def browser(self) -> Browser:
        return self.__browser

    @browser.setter
    def browser(self, value: Browser) -> PyleniumConfig:
        self.__browser = value
        return self

    @property
    def headless(self) -> bool:
        return self.__headless

    @headless.setter
    def headless(self, value: bool) -> PyleniumConfig:
        self.__headless = value
        return self

    @property
    def remote(self) -> bool:
        return self.__remote

    @remote.setter
    def remote(self, value: bool) -> PyleniumConfig:
        self.__remote = value
        return self

    @property
    def browser_size(self) -> str:
        return self.__browser_size

    @browser_size.setter
    def browser_size(self, value: str) -> PyleniumConfig:
        self.__browser_size = value
        return self

    @property
    def browser_version(self) -> str:
        return self.__browser_version

    @browser_version.setter
    def browser_version(self, value: str) -> PyleniumConfig:
        self.__browser_version = value
        return self

    @property
    def browser_position(self) -> str:
        return self.__browser_position

    @browser_position.setter
    def browser_position(self, value: str) -> PyleniumConfig:
        self.__browser_position = value
        return self

    @property
    def browser_maximized(self) -> bool:
        return self.__browser_maximized

    @browser_maximized.setter
    def browser_maximized(self, value: bool) -> PyleniumConfig:
        self.__browser_maximized = value
        return self

    @property
    def wdm_enabled(self) -> bool:
        return self.__wdm_enabled

    @wdm_enabled.setter
    def wdm_enabled(self, value: bool) -> PyleniumConfig:
        self.__wdm_enabled = value
        return self

    @property
    def browser_binary(self) -> str:
        return self.__browser_binary

    @browser_binary.setter
    def browser_binary(self, value: str) -> PyleniumConfig:
        self.__browser_binary = value
        return self

    @property
    def page_load_strategy(self) -> str:
        return self.__page_load_strategy

    @page_load_strategy.setter
    def page_load_strategy(self, value: PageLoadStrategy) -> PyleniumConfig:
        self.__page_load_strategy = value
        return self

    @property
    def desired_capabilities(self) -> DesiredCapabilities:
        return self.__desired_capabilities

    @desired_capabilities.setter
    def desired_capabilities(self, value: DesiredCapabilities):
        self.__desired_capabilities = value
        return self

    @property
    def base_url(self) -> str:
        return self.__base_url

    @base_url.setter
    def base_url(self, value: str) -> PyleniumConfig:
        self.__base_url = value
        return self

    @property
    def explicit_wait_timeout(self) -> int:
        return self.__explicit_wait_timeout

    @explicit_wait_timeout.setter
    def explicit_wait_timeout(self, value: int) -> PyleniumConfig:
        self.__explicit_wait_timeout = value
        return self

    @property
    def polling_timeout(self) -> int:
        return self.__polling_timeout

    @polling_timeout.setter
    def polling_timeout(self, value: int) -> PyleniumConfig:
        self.__polling_timeout = value
        return self

    @property
    def capture_screenshot(self) -> bool:
        return self.__capture_screenshot

    @capture_screenshot.setter
    def capture_screenshot(self, value: bool) -> PyleniumConfig
        self.__capture_screenshot = value
        return self

    @property
    def capture_pagesource(self) -> bool:
        return self.__capture_pagesource

    @capture_pagesource.setter
    def capture_pagesource(self, value: bool) -> PyleniumConfig:
        self.__capture_pagesource = value
        return self

    @property
    def javascript_clicking(self) -> bool:
        return self.__javascript_clicking

    @javascript_clicking.setter
    def javascript_clicking(self, value: bool) -> PyleniumConfig
        self.__javascript_clicking = value
        return self

    @property
    def javascript_sendkeys(self) -> bool:
        return self.__javascript_sendkeys

    @javascript_sendkeys.setter
    def javascript_sendkeys(self, value: bool) -> PyleniumConfig:
        self.__javascript_sendkeys = value
        return self
