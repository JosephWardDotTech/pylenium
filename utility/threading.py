import threading

from drivers.pylenium_driver import PyleniumDriver


class DriverContainers:
    def __init__(self):
        self.threaded_drivers = {}

    def get_thread_driver(self) -> PyleniumDriver:
        if threading.get_ident() in self.threaded_drivers:
            return self.threaded_drivers[threading.get_ident()]
        else:
            self.threaded_drivers[threading.get_ident()] = PyleniumDriver()
            return self.threaded_drivers[threading.get_ident()]
