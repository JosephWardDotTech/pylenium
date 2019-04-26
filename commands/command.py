from __future__ import annotations

import abc
import logging
import typing
from typing import Union

if typing.TYPE_CHECKING:
    from core.pylenium import PyElement

log = logging.getLogger("pylenium")


class Command(metaclass=abc.ABCMeta):
    def __init__(self, py_element: PyElement):
        self.py_element = py_element

    @abc.abstractmethod
    def execute(self) -> Union[str, PyElement, bool, int]:
        pass
