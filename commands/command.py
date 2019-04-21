from __future__ import annotations

import abc
import logging
import typing
from typing import Union

from common.decorators import anti_staleness, ready_state

if typing.TYPE_CHECKING:
    from core.elements import PyElement

log = logging.getLogger("pylenium")


class Command(metaclass=abc.ABCMeta):
    def __init__(self, driver, py_element: PyElement):
        self.driver = driver
        self.py_element = py_element

    @abc.abstractmethod
    @anti_staleness
    @ready_state
    def execute(self) -> Union[str, PyElement, bool, int]:
        pass
