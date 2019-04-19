from __future__ import annotations

from selenium.webdriver.remote.webelement import WebElement


class PyElement(WebElement):

    def __init__(self, parent, id_):
        super().__init__(parent, id_)

    def set_value(self, value: str) -> PyElement:
        super().send_keys(value)
        return self

    def should_have(self, pylenium_condition) -> PyElement:
        pylenium_condition.evaluate(self)
        return self

    def click(self) -> None:
        super().click()

