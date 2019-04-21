from __future__ import annotations

import abc
import typing
import logging

from commands.get_tag_command import GetTagCommand
from commands.get_text_command import GetTextCommand
from conditions.condition import PyCondition
from core.locators import PyLocator
log = logging.getLogger("pylenium")


# refreshes the underlying web element to prevent staleness etc
def anti_staleness(f):
    def wrapper(*args):
        log.info("Lazy loading or refreshing of web elements!")
        args[0].wrapped_element = PyElement(
            args[0].driver.driver.find_element(
                args[0].locator.by, args[0].locator.selector
            )
        )
        return f(*args)

    return wrapper


def ready_state(f):
    def wrapper(*args):
        # js, stability, ajax etc!
        log.info("Stabilizing the page")
        return f(*args)

    return wrapper


class ElementInterface(metaclass=abc.ABCMeta):
    """
    common interface between our pyelement and the pyelement proxy so that the proxy can be used
    anywhere where pyelement is used
    """

    @abc.abstractmethod
    def tag_name(self) -> str:
        pass

    @abc.abstractmethod
    def text(self) -> str:
        pass

    @abc.abstractmethod
    def should_have(
            self, conditions: typing.Union[PyCondition, typing.List[PyCondition]]
    ) -> PyElement:
        pass


class PyElementProxy(ElementInterface):
    __soft_asserts = {
        "should",
        "should_be",
        "should_have" "should_not",
        "should_not_have",
        "should_not_be" "wait_until" "wait_while",
    }

    def __init__(self, driver, locator: PyLocator):
        self.driver = driver
        self.locator: PyLocator = locator
        self.wrapped_element: PyElement = None

    @ready_state
    @anti_staleness
    def tag_name(self) -> str:
        return self.wrapped_element.tag_name()

    @ready_state
    @anti_staleness
    def text(self) -> str:
        breakpoint()
        return self.wrapped_element.text()

    @ready_state
    @anti_staleness
    def should_have(self, conditions) -> PyElement:
        return self.wrapped_element.should_have(conditions)


class ElementFinder:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @staticmethod
    def wrap(driver, locator):
        return PyElementProxy(driver, locator)


class PyElement(ElementInterface):
    def __init__(self, wrapped_element):
        self.wrapped_element = wrapped_element

    def tag_name(self) -> str:
        return GetTagCommand(self).execute()

    def text(self) -> str:
        return GetTextCommand(self).execute()

    def should_have(self, conditions: typing.Union[PyCondition, typing.List[PyCondition]]) -> PyElement:
        return Should
