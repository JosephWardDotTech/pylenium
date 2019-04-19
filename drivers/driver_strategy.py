from __future__ import annotations

from abc import abstractmethod, ABC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import PyleniumConfig

config = PyleniumConfig()


class AbstractBrowserStrategy(ABC):

    # Prepare web driver manager if applicable and instantiate a thread local driver
    @abstractmethod
    def instantiate(self):
        pass


class ChromeBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        chrome_options = None
        if config.headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
        return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


class FirefoxBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        return webdriver.Firefox(GeckoDriverManager().install())


class RemoteWebDriverBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        pass
