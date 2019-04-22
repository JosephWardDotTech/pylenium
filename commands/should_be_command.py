import typing

from commands.command import Command
from conditions.condition import PyCondition


class ShouldBe(Command):
    def __init__(
            self, proxy, conditions: typing.Union[typing.List[PyCondition], PyCondition]
    ):
        super().__init__(proxy)
        self.conditions = conditions

    def execute(self):
        if type(self.conditions) is not list:
            self.conditions.evaluate(self.py_element)
        else:
            for condition in self.conditions:
                condition.evaluate(self.py_element)
        return self.py_element
