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


class PyElementProxy:
    __soft_asserts = {'should',
                      'should_be',
                      'should_have'
                      'should_not',
                      'should_not_have',
                      'should_not_be'
                      'wait_until'
                      'wait_while'}

    def __init__(self,
                 web_element_source: WebElementSource):
        self.web_element_source = web_element_source


class WebElementSource:
    pass


class ElementFinder:
    def __init__(self,
                 driver,
                 locator):
        self.driver = driver
        self.locator = locator

    @staticmethod
    def wrap(driver, locator):
        # return proxy!
        pass
