from __future__ import annotations

from pylenium.commands.command import Command


class GetTagCommand(Command):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def execute(self) -> str:
        return self.element.tag_name()
