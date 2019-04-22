import threading


class CreateDriverCommand:

    @staticmethod
    def create_driver(config,
                 factory,
                 proxy,
                 listeners):
        if not config.reopen_browser:
            raise ValueError('No web driver is bound to the current thread: {} and we cannot launch a new one'
                             'because pylenium_reopen_browser is False'.format(threading.get_ident()))

        pylenium_proxy_server = None
        browser_proxy = proxy

        if config.proxy_enabled:
            # build out the pylenium proxy capabilities!, but not yet!
            pass

        driver = factory.create_webdriver(config, browser_proxy)


class CreateDriverResult:
    def __init__(self,
                 driver,
                 proxy):
        self.driver = driver
        self.proxy = proxy
