import pytest

from pylenium.core.pylenium import PyElement, ID
from tests.integration.base_integration_test import BaseIntegrationTest


@pytest.mark.IT(page="element_dissappears_on_click.html")
class TestPyleniumElement(BaseIntegrationTest):

    @pytest.mark.element
    def test_driver_returns_pyelement(self):
        element = ID('remove')
        element.click()
        assert isinstance(element, PyElement)
