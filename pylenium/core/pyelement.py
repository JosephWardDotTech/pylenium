from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class PyElement(WebElement):

    def __init__(self, parent, id_):
        super().__init__(parent, id_)

    def find(self):
        pass

    def find_all(self):
        pass
