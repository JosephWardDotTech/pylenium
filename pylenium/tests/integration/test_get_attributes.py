from __future__ import annotations

import pytest

from pylenium.conditions.condition import attribute
from pylenium.core.pylenium import ID


@pytest.mark.IT(page="attributes.html")
class TestRetrieveAttribute:
    def test_chained_text_retrieval(self):
        ID("attributes").should_have(attribute("random-attribute"))
