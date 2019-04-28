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
        self.wait_for_element()
        self.wait_for_page_to_be_ready()
        if type(self.conditions) is not list:
            self.conditions.evaluate(self.element)
        else:
            for condition in self.conditions:
                condition.evaluate(self.element)
        return self.element
