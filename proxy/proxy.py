from __future__ import annotations
import abc
import typing


from conditions.condition import PyCondition
from core.locators import PyLocator
from utility.decorators import anti_staleness, ready_state

if typing.TYPE_CHECKING:
    from core.elements import PyElement


class Subject(metaclass=abc.ABCMeta):
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
    def should_have(self, conditions: typing.Union[PyCondition, typing.List[PyCondition]]) -> PyElement:
        pass


class PyElementProxy(Subject):
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

