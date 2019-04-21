from __future__ import annotations
import abc
import typing


from conditions.condition import PyCondition
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

    def __init__(self, driver, py_element: PyElement):
        self._driver = driver
        self._real_subject = py_element

    def tag_name(self) -> str:
        return self._real_subject.tag_name()

    def text(self) -> str:
        return self._real_subject.text()

    def should_have(self, conditions) -> PyElement:
        return self._real_subject.should_have(conditions)


class ElementFinder:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @staticmethod
    def wrap(driver, locator):
        return PyElementProxy(driver, locator)

