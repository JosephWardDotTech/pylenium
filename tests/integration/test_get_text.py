from __future__ import annotations

import pytest

from conditions.condition import text
from core.pylenium import *


@pytest.mark.IT(page="basic_text.html")
class TestRetrieveText:
    def test_basic_text_retrieval(self):
        element = ID("basic_text")
        a = 25
