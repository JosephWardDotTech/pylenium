from pylenium.conditions.conditions import ShouldHave
from pylenium.core.pylenium import PyElement
from pylenium.exceptions.errors import PyAssertionError


class Text(ShouldHave):

    def __init__(self, expected: str):
        super().__init__(expected)

    def confirm(self, element: PyElement):
        actual_text = element.text
        if actual_text != self.expected:
            raise PyAssertionError(f"Expected element to contain text: '{self.expected}' "
                                   f"but the elements text was: '{actual_text}'")


class ExactText(ShouldHave):

    def __init__(self, expected):
        super().__init__(expected)

    def confirm(self, element):
        pass


class Attribute(ShouldHave):

    def __init__(self, expected: str):
        super().__init__(expected)

    def confirm(self, element: PyElement):
        if element.get_attribute(self.expected) is None:
            raise PyAssertionError(f"Expected element to have: {self.expected} attribute, but it did not")


class Value(ShouldHave):

    def __init__(self, expected):
        super().__init__(expected)

    def confirm(self, element):
        pass
