from __future__ import annotations

from selenium.webdriver.remote import webelement
import logging
log = logging.getLogger('pylenium')


# refreshes the underlying web element to prevent staleness etc
def refresh(f):
    def wrapper(*args):
        log.info('Refinding the webelement')
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

    def find(self) -> webelement:
        from core.pylenium import get_wrapped_driver
        return get_wrapped_driver().find_element(self.locator.by, self.locator.selector)







