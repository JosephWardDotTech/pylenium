import logging
import threading
import time

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


class CloseDriverCommand:
    def __init__(self,
                 driver,
                 proxy):
        self.driver = driver
        self.proxy = proxy

    def run(self):
        thread_id = threading.get_ident()
        if self.driver is not None:
            log.info('Closing webdriver: {} -> {}'.format(threading, self.driver))
            if self.proxy is not None:
                log.info('Closing pylenium proxy: {} -> server {}'.format(thread_id, self.proxy))

            start = time.time()
            t = threading.Thread(target=CloseBrowser(), args=self.driver, self.proxy, daemon=True)
            t.start()


class CloseBrowser(Runnable):
    def __init__(self,
                 driver,
                 proxy):
        self.driver = driver
        self.proxy = proxy


