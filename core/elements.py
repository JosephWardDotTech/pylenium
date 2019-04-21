from __future__ import annotations

import logging
from typing import List, Union

from selenium.webdriver.remote.webelement import WebElement

from commands.get_tag_command import GetTagCommand
from commands.get_text_command import GetTextCommand
from conditions.condition import PyCondition
from proxy.proxy import Subject

log = logging.getLogger("pylenium")


class PyElement(WebElement, Subject):
    def __init__(self, locator, parent, id_):
        super().__init__(parent, id_)
        self.locator = locator

    def tag_name(self) -> str:
        return GetTagCommand(self).execute()

    def text(self) -> str:
        return GetTextCommand(self).execute()

    def should_have(self, conditions: Union[PyCondition, List[PyCondition]]
    ) -> PyElement:
        return self
