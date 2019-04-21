from __future__ import annotations

from abc import abstractmethod, ABC


class PyCondition(ABC):
    @abstractmethod
    def evaluate(self, py_element):
        pass


class text(PyCondition):  # NOSONAR
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, py_element):
        assert py_element.text == self.expected
        return py_element


class attribute(PyCondition):  # NOSONAR
    def __init__(self, expected: str):
        self.expected = expected

    def evaluate(self, py_element):
        pass
