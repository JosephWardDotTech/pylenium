from __future__ import annotations
from selenium.webdriver.remote.webelement import WebElement

from pylenium.conditions.py_conditions import PyCondition


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
