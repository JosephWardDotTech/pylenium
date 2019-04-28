import typing
from typing import Union

from commands.command import Command
from conditions.condition import PyCondition

if typing.TYPE_CHECKING:
    from core.pylenium import PyElement


class ShouldHaveCommand(Command):
    def __init__(
            self,
            driver,
            element,
            conditions: typing.Union[typing.List[PyCondition], PyCondition]
    ):
        super().__init__(self, driver, element)
        self.conditions = conditions

    def execute(self) -> Union[str, PyElement, bool, int]:
        if type(self.conditions) is not list:
            self.conditions.evaluate(self.element)
        else:
            for condition in self.conditions:
                condition.evaluate(self.element)
        return self.element
