from __future__ import annotations

from selenium.webdriver.remote import webelement


# refreshes the underlying web element to prevent staleness etc
def refresh(f):
    def wrapper(*args):
        breakpoint()
        args[0].element = args[0].find()
        return f(*args)
    return wrapper


def stability(f):
    def wrapper(*args):
        # js, stability, ajax etc!
        return f(*args)
    return wrapper


class PyElement:

    def __init__(self, locator):
        self.locator = locator
        self.element: webelement = None

    @refresh
    def tag_name(self) -> str:
        return self.element.tag_name()

    def find(self) -> webelement:
        from core.pylenium import get_wrapped_driver
        return get_wrapped_driver().find_element(self.locator.by, self.locator.selector)







