from __future__ import annotations

import time
import typing

from selenium.common.exceptions import StaleElementReferenceException

from pylenium.commands.command import Command

if typing.TYPE_CHECKING:
    from pylenium.core.pylenium import PyleniumDriver, PyElement


class ClickCommand(Command):
    def __init__(self,
                 driver: PyleniumDriver,
                 element: PyElement):
        super().__init__(driver, element)

    def execute(self) -> None:
        super().execute()
        self._click_it()

    def _click_it(self):
        starting = time.time()
        while time.time() < starting + self.config.explicit_wait_timeout:
            try:
                if self.element.is_displayed() and self.element.is_enabled():
                    self.element.click()
                    return
            except StaleElementReferenceException:
                pass  # do nothing, keep re-finding using our locator until its clickable and not stale
