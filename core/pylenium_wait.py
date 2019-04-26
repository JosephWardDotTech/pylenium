from selenium.webdriver.support.wait import WebDriverWait


class PyleniumWait(WebDriverWait):

    def __init__(self, driver, timeout, poll_frequency, ignored_exceptions):
        super().__init__(driver, timeout, poll_frequency, ignored_exceptions)
