import logging
import threading

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

log = logging.getLogger("pylenium")


class CreateDriverCommand:
    @staticmethod
    def create_driver(config, factory, proxy, listener):
        if not config.reopen_browser:
            raise ValueError(
                "No web driver is bound to the current thread: {} and we cannot launch a new one"
                "because pylenium_reopen_browser is False".format(threading.get_ident())
            )

        pylenium_proxy_server = None
        browser_proxy = proxy

        if config.proxy_enabled:
            # build out the pylenium proxy capabilities!, but not yet!
            pass

        driver = factory.build_driver(config, browser_proxy)
        log.info(
            "Creating web driver in current thread: {}".format(threading.get_ident())
        )
        driver = CreateDriverCommand.add_listeners(driver, listener)
        return CreateDriverResult(driver, pylenium_proxy_server)

    @staticmethod
    def add_listeners(driver, listener):
        if not listener:
            return driver
        return EventFiringWebDriver(driver, listener)


class CreateDriverResult:
    def __init__(self, driver, proxy):
        self.driver = driver
        self.proxy = proxy
