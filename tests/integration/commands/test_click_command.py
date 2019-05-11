import pytest

from pylenium.conditions.be_conditions import NonExistent
from pylenium.core.pylenium import ID


@pytest.mark.IT(page="element_dissappears_on_click.html")
class TestClickCommand:

    @pytest.mark.current
    def test_cannot_click_disappeared_element(self):
        btn = ID("remove")
        btn.click()
        btn.should_be(NonExistent())
