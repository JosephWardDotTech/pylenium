from __future__ import annotations

import logging

from selenium.webdriver.remote import webelement

log = logging.getLogger('pylenium')


# refreshes the underlying web element to prevent staleness etc
def refresh(f):
    def wrapper(*args):
        log.info('Re-finding the web element')
        args[0].element = args[0].find()
        return f(*args)

    return wrapper


def page_stability(f):
    def wrapper(*args):
        # js, stability, ajax etc!
        log.info('Stabilizing the page')
        return f(*args)

    return wrapper


class PyElement:

    def __init__(self, locator):
        self.locator = locator
        self.element: webelement = None

    @refresh
    @page_stability
    def tag_name(self) -> str:
        return self.element.tag_name()

    @page_stability
    @refresh
    def text(self) -> str:
        return self.element.text

    @page_stability
    @refresh
    def set_text(self, value) -> PyElement:
        return self.element.send_keys(value)

    def find(self) -> webelement:
        from core.pylenium import get_wrapped_driver
        return get_wrapped_driver().find_element(self.locator.by, self.locator.selector)
