from __future__ import annotations
from core.pylenium import ID
from page_objects.page_object import PyPage


class ExamplePageObject(PyPage):
    _page_field = ID('basic_text')

    def retrieve_the_text(self) -> str:
        return self._page_field.text()

    def set_the_text(self, value: str) -> ExamplePageObject:
        self._page_field.set_text(value)
        return self
