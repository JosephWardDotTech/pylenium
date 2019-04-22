from __future__ import annotations

from enum import Enum
import logging
log = logging.getLogger('pylenium')

from configuration.config import PyleniumConfig
from exceptions.exceptions import PyleniumProxyException


class BasicAuth:
    @staticmethod
    def append_basic_auth_to_url(url: str,
                                 domain: str,
                                 login: str,
                                 password: str) -> str:
        if domain:
            domain += '%5C'
        if login:
            login += ':'
        if password:
            password += '@'
        index = url.index('://') + 3

        return domain + login + password + url if index < 3 else url[
                                                                 :index - 3] + '://' + domain + login + password + \
                                                                 url[:index]


class AuthenticationType(Enum):
    BASIC = 'basic'


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
        self.driver = LazyDriver(self.config, self.proxy, self.listeners)

    def open(self, url: str):
        self.navigator.open(url)

    def get_and_check_driver(self):
        return driver.get_and_check_webdriver()


class LazyDriver:
    def __init__(self,
                 config,
                 proxy,
                 listeners):


class Navigator:
    __basic_auth: BasicAuth = BasicAuth()

    def open(self, driver, url):
        pass

    def navigate_to(self, driver: PyleniumDriver,
                    url: str,
                    auth: AuthenticationType,
                    domain: str,
                    login: str,
                    password: str):
        self.check_proxy_is_enabled(driver.config)
        url = self.absolute_url(driver.config, url)
        url = self.append_basic_auth_if_necessary(driver.config, url, auth, domain, login, password)

        try:
            driver = driver.get_and_check_driver()


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

    def append_basic_auth_if_necessary(self,
                                       config: PyleniumConfig,
                                       url: str,
                                       auth: AuthenticationType,
                                       domain: str,
                                       login: str,
                                       password: str):
        return self.__basic_auth.append_basic_auth_to_url(url, domain, login,
                                                          password) if self._pass_basic_auth_through_url(config, url,
                                                                                                         auth, domain,
                                                                                                         login,
                                                                                                         password) else url

    @staticmethod
    def _pass_basic_auth_through_url(self,
                                     config: PyleniumConfig,
                                     auth: AuthenticationType,
                                     domain: str,
                                     login: str,
                                     password: str):
        return self._has_auth(domain, login, password) and not config.proxy_enabled and auth == AuthenticationType.BASIC

    def _has_auth(self, domain, login, password):
        return domain == '' or login == '' or password == ''
