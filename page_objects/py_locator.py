from abc import ABC, abstractmethod

# Shorthand pylenium locators
# X = XPATH
# CSS = CSS_SELECTOR
# LT = Link_Text
# PTL = Partial_Link_Text
# Class = Class
# Name = Class_Name
# Tag = Tag_Name
from selenium.webdriver.common.by import By

from common.pylenium import get_driver
from common.web_elements import PyElement


class PyLocator(ABC):
    def __init__(self, by: By, selector: str):
        self.by = by
        self.selector = selector

    @abstractmethod
    def lookup(self) -> PyElement:
        pass


class X(PyLocator):  # NOSONAR
    def __init__(self, selector: str):
        super().__init__(By.XPATH, selector)

    def lookup(self):
        return get_driver().find()


class CSS(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass


class LT(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass


class PTL(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass


class Class(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass


class Name(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass


class Tag(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass
