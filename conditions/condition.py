from __future__ import annotations

from abc import abstractmethod, ABC

from exceptions.exceptions import UIAssertionException


class PyCondition(ABC):
    @abstractmethod
    def evaluate(self, py_element):
        pass


class text(PyCondition):  # NOSONAR
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, py_element):
        try:
            assert py_element.wrapped_element.text == self.expected
        except AssertionError:
            raise UIAssertionException('Element should of had text: {} but it was actually: {}'.format(
                self.expected,
                py_element.wrapped_element.text,
            ))

        return py_element


class attribute(PyCondition):  # NOSONAR
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, py_element):
        pass
