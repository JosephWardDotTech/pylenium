from __future__ import annotations


class PyPage:
    def __init__(self, url: str = ''):
        self._url = url

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value) -> PyPage:
        self._url = value
        return self

