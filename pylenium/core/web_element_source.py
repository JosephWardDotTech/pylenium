from pylenium.configuration.config import PyleniumConfig
from pylenium.core.pylenium import PyElement


class WebElementSource:
    def __init__(self, element: PyElement):
        self.element = element
        self.driver = element.parent
        self.config = PyleniumConfig()
