import abc
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from configuration.config import Browser_type

log = logging.getLogger('pylenium')


class BrowserResizer:

    @staticmethod
    def adjust_size(config, driver):
        if config.browser_size and not config.browser_maximized:
            log.info('Setting browser screen size to: {}'.format(config.browser_size))
            coordinates = config.browser_size.split('x')
            width = int(coordinates[0])
            height = int(coordinates[1])
            driver.set_window_size(width, height)
        elif config.browser_maximized:
            driver.maximize_window()
        return driver

    @staticmethod
    def adjust_position(config, driver):
        if config.browser_position:
            log.info('Setting browser position to: {}'.format(config.browser_position))
            coordinates = config.browser_position.split('x')
            width = int(coordinates[0])
            height = int(coordinates[1])
            driver.set_window_position(width, height)
        return driver


class AbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, config, proxy):
        pass

    @abc.abstractmethod
    def supports(self, config, browser) -> bool:
        pass


class ChromeFactory(AbstractFactory):
    def create(self, config, proxy):
        return webdriver.Chrome(ChromeDriverManager().install())

    def supports(self, config, browser) -> bool:
        return browser.is_chrome()


class WebDriverFactory:
    _supported_factories = [ChromeFactory()]
    _browser_resizer = BrowserResizer()

    def create_driver(self, config, proxy):
        log.info('Browser: {}'.format(config.browser))
        log.info('Browser version: {}'.format(config.browser_version))
        log.info('Remote: {}'.format(config.remote))
        log.info('Browser size: {}'.format(config.browser_size))
        log.info('Start Maximized: {}'.format(config.browser_maximized))

        # build browser
        browser = Browser(config.browser, config.headless)
        # do web driver manager stuff
        if config.wdm_enabled and not config.remote:
            #  todo -> pythons wdm is tightly coupled to driver instantiation?
            log.info('Still to setup the wdm capabilities!')
            pass

        # stream factories to build supported driver
        actual_driver = next(filter(lambda x: x.supports(config, browser), self._supported_factories)).create(config,
                                                                                                              browser)

        # set sizing of browser
        actual_driver = self._browser_resizer.adjust_size(config, actual_driver)
        actual_driver = self._browser_resizer.adjust_position(config, actual_driver)

        # log some info

        return actual_driver


class Browser:
    def __init__(self,
                 name: str,
                 headless: bool):
        self.name = name
        self.headless = headless

    def is_headless(self) -> bool:
        return self.is_phantom_js() or self.is_html_unit() or self.headless

    def is_chrome(self) -> bool:
        if isinstance(self.name, Browser_type):
            return self.name.value.lower().startswith('chrome')
        return self.name.lower().startswith('chrome')

    def is_firefox(self) -> bool:
        return self.name.lower().startswith('firefox')

    def is_legacy_firefox(self) -> bool:
        return self.name.lower().startswith('legacy_firefox')

    def is_ie(self) -> bool:
        return self.name.lower().startswith('ie')

    def is_edge(self) -> bool:
        return self.name.lower().startswith('edge')

    def is_safari(self) -> bool:
        return self.name.lower().startswith('safari')

    def is_html_unit(self) -> bool:
        return self.name.lower().startswith('htmlunit')

    def is_phantom_js(self) -> bool:
        return self.name.lower().startswith('phantom_js')

    def is_jbrowser(self) -> bool:
        return self.name.lower().startswith('jbrowser')

    def is_opera(self) -> bool:
        return self.name.lower().startswith('opera')

    def supports_modal_dialogs(self) -> bool:
        return not self.is_safari() and not self.is_phantom_js()
