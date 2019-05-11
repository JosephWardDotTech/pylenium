from __future__ import annotations

from pylenium.conditions.condition import Text
from pylenium.core.pylenium import ID
from pylenium.utility.decorators import loadable


@loadable(page="/login.php")
class ExampleLoginPage:
    _page_field = ID("basic_text")

    def retrieve_the_text(self) -> str:
        return self._page_field.text()

    def set_the_text(self, value: str) -> ExampleLoginPage:
        self._page_field.set_text(value)
        self._page_field.should_have(Text(value))
        return self
