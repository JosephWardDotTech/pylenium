from __future__ import annotations
from abc import abstractmethod, ABC
from selenium.webdriver.remote.webelement import WebElement


class PyElement(WebElement):

    def __init__(self, parent, id_):
        super().__init__(parent, id_)

    def find(self):
        pass

    def find_all(self):
        pass

    def set_value(self, value: str) -> PyElement:
        super().send_keys(value)
        return self

    def should_have(self, condition: PyCondition) -> PyElement:
        condition.evaluate(self)
        return self

    def click(self) -> None:
        super().click()


class PyCondition(ABC):

    @abstractmethod
    def evaluate(self, py_element: PyElement) -> PyElement:
        pass


class Text(PyCondition):
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, py_element: PyElement) -> PyElement:
        assert py_element.text == self.expected
        return py_element

