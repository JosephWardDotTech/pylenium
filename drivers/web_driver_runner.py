from __future__ import annotations

# facade module for accessing web driver instance for threads
from drivers.containers import WebDriverThreadLocalContainer

web_driver_container = WebDriverThreadLocalContainer()


def add_listener(listener):
    web_driver_container.add_listener(listener)
