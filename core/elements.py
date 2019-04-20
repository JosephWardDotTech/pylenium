from __future__ import annotations

import logging

from commands.get_tag_command import GetTagCommand
from commands.get_text_command import GetTextCommand

log = logging.getLogger("pylenium")


class PyElement:
    def __init__(self, locator):
        self.locator = locator
        self.element = None

    def tag_name(self) -> str:
        return GetTagCommand(self).execute()

    def text(self) -> str:
        return GetTextCommand(self).execute()
