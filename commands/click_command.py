from typing import Union

from commands.command import Command
from core.elements import PyElement


class Click(Command):
    def __init__(self, py_element):
        super().__init__(py_element)

    def execute(self) -> Union[str, PyElement, bool, int]:
        self.py_element.element.click()
        return self.py_element
