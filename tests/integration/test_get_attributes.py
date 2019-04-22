from __future__ import annotations

import pytest

from conditions.condition import attribute
from core.pylenium import *


@pytest.mark.IT(page="attributes.html")
class TestRetrieveAttribute:
    def test_chained_text_retrieval(self):
        ID("attributes").should_have(attribute('random-attribute'))

    def test_something(self):
        a = 25
