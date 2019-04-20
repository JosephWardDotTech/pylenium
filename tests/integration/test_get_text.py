from __future__ import annotations

import pytest

from core.locators import ID
from core.pylenium import find


@pytest.mark.IT(page='basic_text.html')
class TestRetrieveText:

    def test_basic_text_retrieval(self):
        text = find(ID('heyworld')).text()
        assert text == 'Hello Wurld!'
