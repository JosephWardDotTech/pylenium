from __future__ import annotations

import os
from enum import Enum

from selenium.webdriver import DesiredCapabilities

# Pyleniums possible web element lookup strategy (by default)
from pylenium.utility.meta import Singleton


class FileDownloadMode(Enum):
    HTTP_GET = ("http_get",)
    PROXY = ("proxy",)


class Selector(Enum):
    CSS = "CSS"
    XPATH = "XPATH"
    ID = "ID"


# Pyleniums possible browser (by default)
class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


# Pyleniums page loading strategy (by default)
# This is basically how quickly Pylenium will attempt to proceed on page loads and click follow up actions
class PageLoadStrategy(Enum):
    NORMAL = "normal"
    FAST = "fast"
    EAGER = "eager"


class PyleniumConfig(metaclass=Singleton):

    _browser = os.getenv('pylenium_browser', BrowserType.CHROME)
    _headless = os.getenv('pylenium_headless', False)
    _remote = os.getenv('pylenium_remote', False)
    _browser_size = os.getenv('pylenium_browser_size', '1920x1080')
    _browser_version = os.getenv('pylenium_browser_version', None)
    _browser_position = os.getenv('pylenium_browser_position', None)
    _browser_maximized = os.getenv('pylenium_maximized', True)
    _wdm_enabled = os.getenv('pylenium_wdm_enabled', True)
    _browser_binary = os.getenv('pylenium_browser_binary', '')
    _page_load_strategy = os.getenv('pylenium_page_load_strategy', PageLoadStrategy.NORMAL)
    _desired_capabilities = DesiredCapabilities()
    _base_url = os.getenv('pylenium_base_url', 'http://localhost:8080/')
    _explicit_wait_timeout = os.getenv('pylenium_wait_timeout', 15)
    _polling_interval = os.getenv('pylenium_polling_interval', 200)
    _capture_screenshots = os.getenv('pylenium_screenshot', True)
    _capture_page_source = os.getenv('pylenium_pagesource', True)
    _click_with_javascript = os.getenv('pylenium_js_click', False)
    _javascript_sendkeys = os.getenv('pylenium_js_sendkeys', False)
    _selector_default = Selector.CSS
    _proxy_enabled = os.getenv('pylenium_proxy_on', False)
    _file_download = os.getenv('pylenium_file_download', FileDownloadMode.HTTP_GET)
    _reopen_browser = os.getenv('pylenium_reopen_browser', True)

    @property
    def reopen_browser(self) -> bool:
        return self._reopen_browser

    @reopen_browser.setter
    def reopen_browser(self, value: bool):
        self._reopen_browser = value

    @property
    def proxy_enabled(self) -> bool:
        return self._proxy_enabled

    @proxy_enabled.setter
    def proxy_enabled(self, value: bool):
        self._proxy_enabled = value

    @property
    def file_download(self) -> FileDownloadMode:
        return self._file_download

    @file_download.setter
    def file_download(self, value: FileDownloadMode):
        self._file_download = value

    @property
    def browser(self) -> BrowserType:
        return self._browser

    @browser.setter
    def browser(self, value: BrowserType):
        self._browser = value

    @property
    def headless(self) -> bool:
        return self._headless

    @headless.setter
    def headless(self, value: bool):
        self._headless = value

    @property
    def remote(self) -> bool:
        return self._remote

    @remote.setter
    def remote(self, value: bool):
        self._remote = value

    @property
    def browser_size(self) -> str:
        return self._browser_size

    @browser_size.setter
    def browser_size(self, value: str):
        self._browser_size = value

    @property
    def browser_version(self) -> str:
        return self._browser_version

    @browser_version.setter
    def browser_version(self, value: str):
        self._browser_version = value

    @property
    def browser_position(self) -> str:
        return self._browser_position

    @browser_position.setter
    def browser_position(self, value: str):
        self._browser_position = value

    @property
    def browser_maximized(self) -> bool:
        return self._browser_maximized

    @browser_maximized.setter
    def browser_maximized(self, value: bool):
        self._browser_maximized = value

    @property
    def wdm_enabled(self) -> bool:
        return self._wdm_enabled

    @wdm_enabled.setter
    def wdm_enabled(self, value: bool):
        self._wdm_enabled = value

    @property
    def browser_binary(self) -> str:
        return self._browser_binary

    @browser_binary.setter
    def browser_binary(self, value: str):
        self._browser_binary = value

    @property
    def page_load_strategy(self) -> PageLoadStrategy:
        return self._page_load_strategy

    @page_load_strategy.setter
    def page_load_strategy(self, value: PageLoadStrategy):
        self._page_load_strategy = value

    @property
    def desired_capabilities(self) -> DesiredCapabilities:
        return self._desired_capabilities

    @desired_capabilities.setter
    def desired_capabilities(self, value: DesiredCapabilities):
        self._desired_capabilities = value

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str):
        self._base_url = value

    @property
    def explicit_wait_timeout(self) -> int:
        return self._explicit_wait_timeout

    @explicit_wait_timeout.setter
    def explicit_wait_timeout(self, value: int):
        self._explicit_wait_timeout = value

    @property
    def polling_interval(self) -> int:
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, value: int):
        self._polling_interval = value

    @property
    def capture_screenshots(self) -> bool:
        return self._capture_screenshots

    @capture_screenshots.setter
    def capture_screenshots(self, value: bool):
        self._capture_screenshots = value

    @property
    def capture_page_source(self) -> bool:
        return self._capture_page_source

    @capture_page_source.setter
    def capture_page_source(self, value: bool):
        self._capture_page_source = value

    @property
    def click_with_javascript(self) -> bool:
        return self._click_with_javascript

    @click_with_javascript.setter
    def click_with_javascript(self, value: bool):
        self._click_with_javascript = value

    @property
    def javascript_sendkeys(self) -> bool:
        return self._javascript_sendkeys

    @javascript_sendkeys.setter
    def javascript_sendkeys(self, value: bool):
        self._javascript_sendkeys = value
