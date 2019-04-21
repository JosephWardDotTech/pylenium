from __future__ import annotations

import logging
from typing import List, Union

from selenium.webdriver.remote.webelement import WebElement

from commands.get_tag_command import GetTagCommand
from commands.get_text_command import GetTextCommand
from conditions.condition import PyCondition

log = logging.getLogger("pylenium")


class PyElement(WebElement):
    def __init__(self, locator, parent, id_):
        super().__init__(parent, id_)
        self.locator = locator

    def tag_name(self) -> str:
        return GetTagCommand(self).execute()

    def text(self) -> str:
        return GetTextCommand(self).execute()

    def should_have(
            self, conditions: Union[PyCondition, List[PyCondition]]
    ) -> PyElement:
        return self


class PyElementProxy:
    __soft_asserts = {
        "should",
        "should_be",
        "should_have" "should_not",
        "should_not_have",
        "should_not_be" "wait_until" "wait_while",
    }

    def __init__(self, web_element_source: WebElementSource):
        self.web_element_source = web_element_source


class WebElementSource:
    pass


class ElementFinder:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @staticmethod
    def wrap(driver, locator):
        # return proxy!
        pass
