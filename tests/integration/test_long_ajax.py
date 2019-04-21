from __future__ import annotations

import pytest

from conditions.condition import text
from core.pylenium import *


@pytest.mark.IT(page="long_ajax_request.html")
@pytest.mark.ajax
class TestLongAjaxLoading:
    def test_chained_text_retrieval(self):
        X("//button").click()
        X("//span[@id='result-2']").should_have(text('r2'))
