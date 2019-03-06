from abc import abstractmethod, ABC


class AbstractBrowserStrategy(ABC):

    # Prepare web driver manager if applicable and instantiate a thread local driver
    @abstractmethod
    def instantiate(self):
        pass


class ChromeBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        pass


class FirefoxBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        pass


class RemoteWebDriverBrowserStrategy(AbstractBrowserStrategy):

    def instantiate(self):
        pass


class PyleniumDriver(object):
    def __init__(self,
                 driver_strategy: AbstractBrowserStrategy = ChromeBrowserStrategy()):
        self.driver_strategy = driver_strategy
