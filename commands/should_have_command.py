from typing import Union, List

from commands.command import Command
from conditions.condition import PyCondition


class ShouldHaveCommand(Command):
    def __init__(self, py_element, conditions: Union[List[PyCondition], PyCondition]):
        super().__init__(py_element)
        self.conditions = conditions

    def execute(self) -> str:
        return self.py_element.wrapped_element.text
