from __future__ import annotations
from commands.command import Command
import typing
if typing.TYPE_CHECKING:
    from core.elements import PyElement


class GetTagCommand(Command):
    def __init__(self, py_element: PyElement):
        super().__init__(py_element)

    def execute(self) -> str:
        return self.py_element.element.tag_name()
