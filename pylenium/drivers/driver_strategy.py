from __future__ import annotations
from abc import abstractmethod, ABC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pylenium.config.config import PyleniumConfig
from selenium import webdriver


class AbstractBrowserStrategy(ABC):

    # Prepare web driver manager if applicable and instantiate a thread local driver
    @abstractmethod
    def instantiate(self):
        pass


class ChromeBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        return webdriver.Chrome(ChromeDriverManager().install())


class FirefoxBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        return webdriver.Firefox(GeckoDriverManager().install())


class RemoteWebDriverBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        pass


class PyleniumDriver(object):
    def __init__(self,
                 config: PyleniumConfig,
                 driver_strategy: AbstractBrowserStrategy = ChromeBrowserStrategy()):
        self.driver_strategy = driver_strategy
        self._driver: webdriver = self.driver_strategy.instantiate()

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
