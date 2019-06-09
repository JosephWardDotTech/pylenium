import pytest
from assertpy import assert_that

from pylenium.core.pylenium import PyElement, ID
from tests.integration.base_integration_test import BaseIntegrationTest


@pytest.mark.IT(page="element_dissappears_on_click.html")
class TestPyleniumElement(BaseIntegrationTest):

    @pytest.mark.element
    def test_driver_returns_pyelement(self):
        element = ID('remove')
        element.click()
        assert_that(element).is_instance_of(PyElement)
