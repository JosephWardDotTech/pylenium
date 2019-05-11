from __future__ import annotations

import pytest

from pylenium.conditions.condition import Text
from pylenium.core.pylenium import ID


@pytest.mark.IT(page="basic_text.html")
class TestRetrieveText:
    def test_chained_text_retrieval(self):
        ID("basic_text").should_have(Text("Hello World")).should_have(
            Text("Hello World")
        )
