from __future__ import annotations
from abc import abstractmethod, ABC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
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
