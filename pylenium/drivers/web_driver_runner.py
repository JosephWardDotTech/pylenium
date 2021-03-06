from __future__ import annotations

# facade module for accessing web driver instance for threads
from pylenium.drivers.containers import WebDriverThreadLocalContainer

web_driver_container = WebDriverThreadLocalContainer()


def add_listener(listener):
    web_driver_container.add_listener(listener)


def start(url: str):
    web_driver_container.get_pylenium_driver().start(url)
