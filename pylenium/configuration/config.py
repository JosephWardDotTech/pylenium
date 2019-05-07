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
class Browser_type(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"


# Pyleniums page loading strategy (by default)
# This is basically how quickly Pylenium will attempt to proceed on page loads and click follow up actions
class PageLoadStrategy(Enum):
    NORMAL = "normal"
    FAST = "fast"
    EAGER = "eager"


class PyleniumConfig(metaclass=Singleton):

    _browser = os.getenv('pylenium_browser', Browser_type.CHROME)
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
    _capture_pagesource = os.getenv('pylenium_pagesource', True)
    _click_with_javascript = os.getenv('pylenium_js_click', False)
    _selector_default = Selector.CSS
    _proxy_enabled = os.getenv('pylenium_proxy_on', False)
    _file_download = os.getenv('pylenium_file_download', FileDownloadMode.HTTP_GET)
    _reopen_browser = os.getenv('pylenium_reopen_browser', True)
