from __future__ import annotations

import pytest

from conditions.condition import text
from core.pylenium import *


@pytest.mark.IT(page="basic_text.html")
@pytest.mark.debug
class TestRetrieveText:
    def test_chained_text_retrieval(self):
        ID("basic_text").should_have(text('Hello World')).should_have(text('Hello World'))

