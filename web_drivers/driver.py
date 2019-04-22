from __future__ import annotations
from enum import Enum

from configuration.config import PyleniumConfig
from exceptions.exceptions import PyleniumProxyException


class AuthenticationType(Enum):
    pass


class FileDownloadMode(Enum):
    HTTP_GET = 'http_get',
    PROXY = 'proxy',


class PyleniumDriver:
    def __init__(self,
                 config,
                 users_proxy,
                 driver_listeners):
        self.navigator = Navigator()
        self.config = config
        self.proxy = users_proxy
        self.listeners = driver_listeners

    def open(self, url: str):
        self.navigator.open(url)


class Navigator:

    def open(self, driver, url):
        pass

    def navigate_to(self, driver: PyleniumDriver,
                    url: str, auth: AuthenticationType,
                    domain: str,
                    login: str,
                    password: str):
        self.check_proxy_is_enabled(driver.con)

    @staticmethod
    def check_proxy_is_enabled(config: PyleniumConfig):
        if not config.file_download == FileDownloadMode.PROXY and config.proxy_enabled:
            raise PyleniumProxyException('You are attempting to download files using a proxy but no'
                                         'proxy was specified, download mode is: Proxy but proxy enablement is'
                                         'false.')

    def absolute_url(self, config: PyleniumConfig, url: str):
        return url if self._is_absolute_url(url) else config.base_url + url

    @staticmethod
    def _is_absolute_url(relative_or_absolute_url: str) -> bool:
        return relative_or_absolute_url.lower().startswith(('http', 'https', 'file:'))



class BasicAuth:
    pass





