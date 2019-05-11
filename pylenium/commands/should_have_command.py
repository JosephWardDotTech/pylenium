from __future__ import annotations

import typing
from typing import Union, List

from pylenium.commands.command import Command
from pylenium.conditions.conditions import Have, ShouldHave

if typing.TYPE_CHECKING:
    from pylenium.core.pylenium import PyElement, PyleniumDriver


class ShouldHaveCommand(Command):
    def __init__(self, driver: PyleniumDriver, element: PyElement, conditions: Union[List[ShouldHave], Have]):
        super().__init__(driver, element)
        self.conditions = [conditions] if conditions is not list else conditions

    def execute(self):
        super().execute()
        for condition in self.conditions:
            condition.confirm(self.element)
        return self.element

