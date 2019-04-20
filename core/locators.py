from abc import ABC
from selenium.webdriver.common.by import By


class PyLocator(ABC):
    def __init__(self, by: By, selector: str):
        self.by = by
        self.selector = selector


class X(PyLocator):  # NOSONAR

    def __init__(self, selector: str):
        super().__init__(By.XPATH, selector)


class CSS(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.CSS_SELECTOR, selector)


class LT(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.LINK_TEXT, selector)


class PTL(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.PARTIAL_LINK_TEXT, selector)


class Class(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.CLASS_NAME, selector)


class Name(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.NAME, selector)


class Tag(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.TAG_NAME, selector)


class ID(PyLocator):
    def __init__(self, selector: str):
        super().__init__(By.ID, selector)
