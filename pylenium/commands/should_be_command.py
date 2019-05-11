from typing import Union, List
from pylenium.commands.command import Command
from pylenium.conditions.conditions import ShouldBe


class ShouldBeCommand(Command):
    def __init__(self, driver, element, conditions: Union[List[ShouldBe], ShouldBe]):
        super().__init__(driver, element)
        self.conditions = [conditions] if conditions is not list else conditions

    def execute(self):
        super().execute()
        for condition in self.conditions:
            condition.confirm(self.element)
        return self.element
