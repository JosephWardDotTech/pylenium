from __future__ import annotations

from config.config import PyleniumConfig


class PyPage:
    def __init__(self, relative_url: str = ''):
        self.config = PyleniumConfig()
        self.url = self.config.base_url + relative_url

    @property
    def url(self) -> str:
        return self.url

    @url.setter
    def url(self, value) -> PyPage:
        self.url = value
        return self

