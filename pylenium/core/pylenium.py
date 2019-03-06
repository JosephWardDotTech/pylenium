from pylenium.config.config import PyleniumConfig


# Our main entry point for Pylenium
class Pylenium(object):
    def __init__(self):
        self.config = PyleniumConfig()
