from core.locators import ID
from core.pylenium import find, start
from page_objects.page_object import PyPage


class ITPageObject(PyPage):

    page_field = find(ID('basic_text'))

    def __init__(self):
        super().__init__('basic_text.html')

    def retrieve_the_text(self) -> str:
        return self.page_field.text()



