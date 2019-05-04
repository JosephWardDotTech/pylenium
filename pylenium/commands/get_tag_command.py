from __future__ import annotations

from pylenium.commands import Command


class GetTagCommand(Command):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def execute(self) -> str:
        return self.element.wrapped_element.tag_name()
