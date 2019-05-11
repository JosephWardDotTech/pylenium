from __future__ import annotations

import typing

from pylenium.commands.command import Command
from pylenium.conditions.condition import PyCondition

if typing.TYPE_CHECKING:
    from pylenium.core.pylenium import PyElement, PyleniumDriver


class ShouldHaveCommand(Command):
    def __init__(self, driver: PyleniumDriver, element: PyElement,
                 conditions: typing.Union[typing.List[PyCondition], PyCondition]):
        super().__init__(driver, element)
        self.conditions = conditions

    def execute(self):
        super().execute()
        if type(self.conditions) is not list:
            self.conditions.evaluate(self.element)
        else:
            for condition in self.conditions:
                condition.evaluate(self.element)
        return self.element
