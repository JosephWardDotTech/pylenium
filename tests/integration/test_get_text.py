from __future__ import annotations

import pytest

from core.pylenium import *


@pytest.mark.IT(page="basic_text.html")
class TestRetrieveText:
    def test_basic_text_retrieval(self):
        ID("basic_text").should_have(text("hello world"))
