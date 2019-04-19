from __future__ import annotations

from abc import abstractmethod, ABC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class AbstractBrowserStrategy(ABC):

    # Prepare web driver manager if applicable and instantiate a thread local driver
    @abstractmethod
    def instantiate(self):
        pass


class ChromeBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(ChromeDriverManager().install())


class FirefoxBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        return webdriver.Firefox(GeckoDriverManager().install())


class RemoteWebDriverBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        pass
