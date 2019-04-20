from __future__ import annotations

import pytest
from core.locators import *
from core.pylenium import find, terminate
from tests.integration.integration_test import IntegrationTest


@pytest.mark.IT
class TestRetrieveText(IntegrationTest):

    @pytest.fixture(scope='function', autouse=True)
    def manage_test(self, request):
        IntegrationTest.open_file('basic_text.html')
        yield
        terminate()

    def test_basic_text_retrieval(self):
        text = find(ID('heyworld')).text()
        assert text == 'Hello Wurld!'
