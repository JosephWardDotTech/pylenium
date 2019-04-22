import logging
log = logging.getLogger('pylenium')


class AbstractFactory:
    pass


class ChromeFactory(AbstractFactory):
    pass


class WebDriverFactory:

    __supported_factories = [ChromeFactory()]

    @staticmethod
    def create_driver(config, proxy):
        log.info('Browser: {}'.format(config.browser))
        log.info('Browser version: {}'.format(config.browser_version))
        log.info('Remote: {}'.format(config.remote))
        log.info('Browser size: {}'.format(config.browser_size))
        log.info('Start Maximized: {}'.format(config.start_maximized))

        # build browser

        # do web driver manager stuff

        # stream factories to build supported driver

        # set sizing of browser


        # log some info


class Browser:
    def __init__(self,
                 name: str,
                 headless: bool):
        self.name = name
        self.headless = headless

    def is_headless(self) -> bool:
        return self.is_phantom_js() or self.is_html_unit() or self.headless

    def is_chrome(self) -> bool:
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
