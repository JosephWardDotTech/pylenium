from abc import ABC, abstractmethod
# Shorthand pylenium locators
# X = XPATH
# CSS = CSS_SELECTOR
# LT = Link_Text
# PTL = Partial_Link_Text
# Class = Class
# Name = Class_Name
# Tag = Tag_Name


class PyLocator(ABC):
    def __init__(self, selector: str):
        self.selector = selector

    @abstractmethod
    def lookup(self):
        pass


class X(PyLocator):
    def __init__(self, selector: str):
        super().__init__(selector)

    def lookup(self):
        pass


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
