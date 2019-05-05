import logging
import threading
import time
from typing import Dict

from pylenium.configuration.config import PyleniumConfig
from pylenium.drivers.driver import PyleniumDriver
from pylenium.utility.meta import Singleton

log = logging.getLogger('pylenium')


class WebDriverThreadLocalContainer(metaclass=Singleton):
    _listeners = []
    _all_web_driver_threads = []
    _thread_web_driver = {}
    clean_up_thread_started = threading.local()
    clean_up_thread_started.x = False

    def add_listener(self, listener):
        self._listeners.append(listener)

    def set_web_driver(self, driver, proxy=None):
        thread_id = threading.get_ident()
        previous = self._thread_web_driver.get(thread_id, None)
        if previous is not None:
            previous.close()

        self._thread_web_driver[thread_id] = driver

    def get_pylenium_driver(self):
        if threading.get_ident() not in self._thread_web_driver:
            self._thread_web_driver[threading.get_ident()] = self.mark_for_auto_close(threading.current_thread(),
                                                                                      PyleniumDriver(PyleniumConfig(), None))
            return self._thread_web_driver[threading.get_ident()]
        else:
            return self._thread_web_driver[threading.get_ident()]

    def get_and_check_webdriver(self):
        return self.get_pylenium_driver().get_and_check_webdriver()

    def get_webdriver(self):
        return self.get_pylenium_driver().get_webdriver()

    def get_proxy_server(self):
        return self.get_pylenium_driver().get_proxy()

    def mark_for_auto_close(self, thread, driver):
        self._all_web_driver_threads.append(thread)
        if not self.clean_up_thread_started.x:
            UnusedWebDriverCleanupThread(self._all_web_driver_threads, self._thread_web_driver).start()
        self.clean_up_thread_started.x = True
        return driver


class UnusedWebDriverCleanupThread(threading.Thread):
    def __init__(self, driver_threads, thread_driver):
        super().__init__(daemon=True, name='[WebDriver Exterminator]')
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
        log.info('Thread is is: {}'.format(threading.get_ident()))
        self.driver_threads = [t for t in self.driver_threads if not t.ident == threading.current_thread().ident]
        driver = self.thread_driver.pop(threading.get_ident(), None)
        if driver is None:
            log.info('No web driver found for thread: {} - nothing to close'.format(threading.get_ident()))
        else:
            driver.close()
