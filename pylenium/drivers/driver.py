from __future__ import annotations

import logging
import threading
from enum import Enum
import typing

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from pylenium.configuration.config import PyleniumConfig, FileDownloadMode
from pylenium.core.bys import *
from pylenium.drivers.commands import CreateDriverCommand, CloseDriverCommand
from pylenium.drivers.factories import WebDriverFactory
from pylenium.exceptions.exceptions import PyleniumProxyException

if typing.TYPE_CHECKING:
    from pylenium.core.pylenium import PyElement


log = logging.getLogger("pylenium")


class BasicAuth:
    @staticmethod
    def append_basic_auth_to_url(
            url: str, domain: str, login: str, password: str
    ) -> str:
        if domain:
            domain += "%5C"
        if login:
            login += ":"
        if password:
            password += "@"
        index = url.index("://") + 3

        return (
            domain + login + password + url
            if index < 3
            else url[: index - 3] + "://" + domain + login + password + url[:index]
        )


class AuthenticationType(Enum):
    BASIC = "basic"


class PyleniumDriver:
    def __init__(
            self, config, users_proxy=None, driver=None, listener: typing.Optional[AbstractEventListener] = None
    ):
        self.navigator = Navigator()
        self.config = config
        self.proxy = users_proxy
        self.listener = listener
        self.driver = driver or LazyDriver(self.config, self.proxy, self.listener)

    def start(self, url: str):
        self.navigator.open(self, url)

    def get_and_check_driver(self):
        return self.driver.get_and_check_webdriver()

    def url(self) -> str:
        return self.driver.web_driver.current_url

    def quit(self):
        self.driver.web_driver.quit()
        self.driver.web_driver = None

    def close(self):
        self.driver.close()

    def execute_javascript(self, script: str, *args):
        return self.driver.web_driver.execute_script(script, args)

    def find_element(self, by) -> PyElement:
        element = self.driver.web_driver.find_element(by)
        return element

    def X(self, identifier: str):
        return self.find_element(identity(identifier))

    def ID(self, identifier: str):
        return self.find_element(identity(identifier))

    def CSS(self, identifier: str):
        return self.find_element(css(identifier))

    def PLT(self, identifier: str):
        return self.find_element(partial_link_text(identifier))

    def LT(self, identifier: str):
        return self.find_element(link_text(identifier))

    def NAME(self, identifier: str):
        return self.find_element(name(identifier))

    def TAG_NAME(self, identifier: str):
        return self.find_element(tag(identifier))

    def CLASS(self, identifier: str):
        return self.find_element(clazz(identifier))

    def get_current_url(self) -> str:
        return self.driver.web_driver.current_url


class LazyDriver:
    def __init__(
            self,
            config,
            user_proxy,
            listener,
            factory: WebDriverFactory = None,
            browser_health_checker: BrowserHealthChecker = None,
    ):
        self.config: PyleniumConfig = config
        self.proxy = user_proxy
        self.listener = listener
        self.factory = factory or WebDriverFactory()
        self.browser_health_checker = browser_health_checker or BrowserHealthChecker()
        self.web_driver = None
        self.closed = False

    def get_and_check_webdriver(self):
        if (
                self.web_driver is not None
                and self.config.reopen_browser
                and not self.browser_health_checker.is_browser_open(self.web_driver)
        ):
            log.info("Web driver has been closed, Lets recreate it")
            self.close()
            self.create_driver()
        elif self.web_driver is None:
            log.info(
                "No web driver is bound to the current thread: {} - lets create one".format(
                    threading.get_ident()
                )
            )
            self.create_driver()
        return self.get_web_driver()

    def get_web_driver(self):
        if self.closed or self.web_driver is None:
            raise ValueError(
                "Web driver has been closed, you need to call start() to open another browser"
            )
        else:
            return self.web_driver

    def close(self):
        if not self.config.reopen_browser:
            CloseDriverCommand(self.web_driver, self.proxy).run()
            self.web_driver = None
            self.proxy = None
            self.closed = True

    def create_driver(self):
        result = CreateDriverCommand().create_driver(
            self.config, self.factory, self.proxy, self.listener
        )
        self.web_driver = result.driver
        self.proxy = result.proxy
        self.closed = False


class Navigator:
    __basic_auth: BasicAuth = BasicAuth()

    def open(self, driver, url):
        self.navigate_to(driver, url, AuthenticationType.BASIC, "", "", "")

    def navigate_to(
            self,
            driver: PyleniumDriver,
            url: str,
            auth: AuthenticationType,
            domain: str,
            login: str,
            password: str,
    ):
        self.check_proxy_is_enabled(driver.config)
        url = self.absolute_url(driver.config, url)
        url = self.append_basic_auth_if_necessary(
            driver.config, url, auth, domain, login, password
        )

        web_driver = driver.get_and_check_driver()
        self.before_navigate_to(
            driver.config, driver.proxy, auth, domain, login, password
        )
        web_driver.get(url)

    def before_navigate_to(self, config, proxy, auth, domain, login, password):
        if config.proxy_enabled:
            self.check_that_proxy_is_started(proxy)
            self.before_navigate_to_with_proxy(proxy, auth, domain, login, password)
        else:
            self.before_navigate_to_without_proxy(auth, domain, login, password)

    def check_that_proxy_is_started(self):
        pass

    def before_navigate_to_with_proxy(self, proxy, auth, domain, login, password):
        if self._has_auth(domain, login, password):
            # BasicAuthRequestFilter(proxy).set_auth(auth, Credentials(login, password))
            pass
        else:
            # BasicAuthRequestFilter(proxy).remove_auth()
            pass

    def before_navigate_to_without_proxy(self, auth, domain, login, password):
        if self._has_auth(domain, login, password) and auth != AuthenticationType.BASIC:
            raise PyleniumProxyException(
                "Cannot use: {} authentication without a proxy server".format(auth)
            )

    @staticmethod
    def check_proxy_is_enabled(config: PyleniumConfig):
        if not config.file_download == FileDownloadMode.PROXY and config.proxy_enabled:
            raise PyleniumProxyException(
                "You are attempting to download files using a proxy but no"
                "proxy was specified, download mode is: Proxy but proxy enablement is"
                "false."
            )

    def absolute_url(self, config: PyleniumConfig, url: str):
        return url if self._is_absolute_url(url) else config.base_url + url

    @staticmethod
    def _is_absolute_url(relative_or_absolute_url: str) -> bool:
        return relative_or_absolute_url.lower().startswith(("http", "https", "file:"))

    def append_basic_auth_if_necessary(
            self,
            config: PyleniumConfig,
            url: str,
            auth: AuthenticationType,
            domain: str,
            login: str,
            password: str,
    ):
        return (
            self.__basic_auth.append_basic_auth_to_url(url, domain, login, password)
            if self._pass_basic_auth_through_url(config, auth, domain, login, password)
            else url
        )

    def _pass_basic_auth_through_url(
            self,
            config: PyleniumConfig,
            auth: AuthenticationType,
            domain: str,
            login: str,
            password: str,
    ):
        return (
                self._has_auth(domain, login, password)
                and not config.proxy_enabled
                and auth == AuthenticationType.BASIC
        )

    @staticmethod
    def _has_auth(domain, login, password):
        return domain != "" or login != "" or password != ""


class BrowserHealthChecker:
    @staticmethod
    def is_browser_open(driver: webdriver) -> bool:
        try:
            driver.get_title()
            return True
        except WebDriverException as ex:
            log.info("Driver window, session or window was not found!")
            return False
