import pytest

from core.pylenium import start
from tests.test_pages.page_objects import ITPageObject


@pytest.mark.IT(page='basic_text.html')
class TestPageObject:

    _basic_page = ITPageObject()

    def test_simple_page_object_launching(self):
        assert start(self._basic_page)
