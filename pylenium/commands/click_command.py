from __future__ import annotations
import typing
from pylenium.commands import Command

if typing.TYPE_CHECKING:
    from pylenium.core.pylenium import PyleniumDriver, PyElement


class ClickCommand(Command):
    def __init__(self,
                 driver: PyleniumDriver,
                 element: PyElement):
        super().__init__(driver, element)

    def execute(self) -> None:
        self.wait_for_element()
        self.wait_for_page_to_be_ready()
        return self.element.wrapped_element.click()
