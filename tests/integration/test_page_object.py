import pytest

from core.pylenium import start
from tests.test_pages.page_objects import ExamplePageObject


@pytest.mark.IT(page="basic_text.html")
@pytest.mark.page_objects
class TestPageObject:
    _basic_page = ExamplePageObject()

    @pytest.mark.debug
    def test_simple_page_object_launching(self):
        assert start(self._basic_page).retrieve_the_text() == "Hello World"
