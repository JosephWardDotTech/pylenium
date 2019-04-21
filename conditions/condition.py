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

    def evaluate(self, proxy):
        try:
            assert proxy.wrapped_element.text == self.expected
        except AssertionError:
            raise UIAssertionException('Element should of had text: {} but it was actually: {}'.format(
                self.expected,
                proxy.wrapped_element.text,
            ))

        return proxy


class attribute(PyCondition):  # NOSONAR
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, proxy):
        try:
            assert proxy.wrapped_element.get_attribute(self.expected) is not None
        except AssertionError:
            raise UIAssertionException('Expected element have the attribute: {} but it did not'.format(
                self.expected
            ))
