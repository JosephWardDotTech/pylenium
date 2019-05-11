from __future__ import annotations

import time
from abc import abstractmethod, ABC

from selenium.common.exceptions import NoSuchElementException

from pylenium.exceptions.errors import PyAssertionError
from pylenium.exceptions.exceptions import UIAssertionException


class PyCondition(ABC):
    @abstractmethod
    def evaluate(self, py_element):
        pass


class Text(PyCondition):
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, element):
        try:
            assert element.wrapped_element.text == self.expected
        except AssertionError:
            raise UIAssertionException(
                "Element should of had text: {} but it was actually: {}".format(
                    self.expected, element.wrapped_element.text
                )
            )

        return element


class NonExistent(PyCondition):
    def __init__(self):
        pass

    def evaluate(self, py_element):
        try:
            time.sleep(0.1)
            py_element.find()
            raise PyAssertionError("Expected element to be non existent but it was found in the DOM")
        except NoSuchElementException:
            pass  # do nothing, this is good!


class Attribute(PyCondition):
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, proxy):
        try:
            proxy.wrapped_element.get_attribute(self.expected) is not None
        except AssertionError:
            raise UIAssertionException(
                "Expected element have the attribute: {} but it did not".format(
                    self.expected
                )
            )
