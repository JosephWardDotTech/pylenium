from __future__ import annotations

import logging
from typing import List, Union

from commands.get_tag_command import GetTagCommand
from commands.get_text_command import GetTextCommand
from conditions.condition import PyCondition
from core.pylenium import driver
from proxy.proxy import Subject

log = logging.getLogger("pylenium")


class PyElement(Subject):
    def __init__(self, locator):
        self.locator = locator
        self.driver = driver()
        self.wrapped_element = None

    def tag_name(self) -> str:
        return GetTagCommand(self.driver, self).execute()

    def text(self) -> str:
        return GetTextCommand(self.driver, self).execute()

    def should_have(self, conditions: Union[PyCondition, List[PyCondition]]) -> PyElement:
        return self
