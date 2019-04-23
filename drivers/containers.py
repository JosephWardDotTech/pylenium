import threading
import time
from typing import Dict

from configuration.config import PyleniumConfig
from drivers.driver import PyleniumDriver
from utility.meta import Singleton
import logging

log = logging.getLogger('pylenium')


class WebDriverThreadLocalContainer(metaclass=Singleton):
    _listeners = []
    _driver_threads = []
    _drivers = {}
    clean_up_thread_started = False

    def add_listener(self, listener):
        self._listeners.append(listener)

    def set_web_driver(self, driver, proxy=None):
        thread_id = threading.get_ident()
        previous = self._drivers.get(thread_id, None)
        if previous is not None:
            previous.close()

        self._drivers[thread_id] = driver

    def get_pylenium_driver(self):
        if threading.get_ident() not in self._drivers:
            self._drivers[threading.get_ident()] = self.mark_for_auto_close(threading.current_thread(),
                                                                            PyleniumDriver(PyleniumConfig(), None))
            return self._drivers[threading.get_ident()]
        else:
            return self._drivers[threading.get_ident()]

    def get_and_check_webdriver(self):
        return self.get_pylenium_driver().get_and_check_webdriver()

    def get_webdriver(self):
        return self.get_pylenium_driver().get_webdriver()

    def get_proxy_server(self):
        return self.get_pylenium_driver().get_proxy()

    def mark_for_auto_close(self, thread, driver):
        self._driver_threads.append(thread)
        UnusedWebDriverCleanupThread(self._driver_threads, self._drivers).start()
        self.clean_up_thread_started = True
        return driver


class UnusedWebDriverCleanupThread(threading.Thread):
    def __init__(self, driver_threads, thread_driver):
        super().__init__(daemon=True, name='Web driver Killer Thread')
        self.driver_threads = driver_threads
        self.thread_driver: Dict = thread_driver

    def run(self):
        while True:
            self.close_unused_drivers()
            time.sleep(100)

    def close_unused_drivers(self):
        for thread in self.driver_threads:
            if thread.isAlive():
                log.info('Thread: {} is dead, Lets close the Pylenium driver: {}'
                         .format(threading.get_ident(),
                                 self.thread_driver.get(threading.get_ident())))
                self.close_web_driver()

    def close_web_driver(self):
        self.driver_threads.remove(threading.get_ident())
        driver = self.thread_driver.pop(threading.get_ident())
        if driver is None:
            log.info('No web driver found for thread: {} - nothing to close'.format(threading.get_ident()))
        else:
            driver.close()
