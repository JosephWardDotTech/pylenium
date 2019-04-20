from __future__ import annotations
import typing
from typing import Union
from common.decorators import anti_staleness, ready_state
import logging
import abc
from core.pylenium import get_driver

if typing.TYPE_CHECKING:
    from core.elements import PyElement

log = logging.getLogger('pylenium')


class Command(metaclass=abc.ABCMeta):
    def __init__(self, py_element: PyElement):
        self.driver = get_driver()
        self.py_element = py_element

    @abc.abstractmethod
    @anti_staleness
    @ready_state
    def execute(self) -> Union[str, PyElement, bool, int]:
        pass
