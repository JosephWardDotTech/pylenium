from __future__ import annotations

import pytest

from pylenium.conditions.have_conditions import Attribute
from pylenium.core.pylenium import ID


@pytest.mark.IT(page="attributes.html")
class TestRetrieveAttribute:
    def test_chained_text_retrieval(self):
        ID("attributes").should_have(Attribute("random-attribute"))
