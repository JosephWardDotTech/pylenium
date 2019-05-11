from selenium.common.exceptions import NoSuchElementException

from pylenium.conditions.conditions import ShouldHave, ShouldBe
from pylenium.core.pylenium import PyElement
from pylenium.exceptions.errors import PyAssertionError


class NonExistent(ShouldBe):

    def __init__(self):
        super().__init__()

    def confirm(self, element: PyElement):
        try:
            element.find()
            raise PyAssertionError("Expected element to be non existent but it was found in the DOM")
        except NoSuchElementException:
            pass  # do nothing, this is good!

