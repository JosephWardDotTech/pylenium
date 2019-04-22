import threading

from web_drivers.driver import PyleniumDriver


class WebDriverThreadLocalContainer:
    _listeners = []
    _driver_threads = {}
    _drivers = {}

    def add_listener(self, listener):
        self._listeners.append(listener)

    def set_web_driver(self, driver, proxy=None):
        thread_id = threading.get_ident()
        previous = self._drivers.get(thread_id, None)
        if previous is not None:
            previous.close()

        self._drivers[thread_id] = PyleniumDriver(driver, proxy)


    def get_pylenium_driver(self):
        pass

    def get_and_check_webdriver(self):
        return self.get_pylenium_driver().get_and_check_webdriver()

    def get_webdriver(self):
        return self.get_pylenium_driver().get_webdriver()

    def get_proxy_server(self):
        return self.get_pylenium_driver().get_proxy()
