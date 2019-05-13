from __future__ import annotations
import abc
import logging
import time
from pylenium.core.web_element_source import WebElementSource
log = logging.getLogger("pylenium")


class Command(metaclass=abc.ABCMeta):
    def __init__(self, element_source: WebElementSource):
        self.element_source = element_source

    def execute(self):
        self._wait_for_page_ready_state()
        time.sleep(0.1)

    def _wait_for_page_ready_state(self):
        log.info('Waiting for page source to be stable for up to: {} seconds'.format(self.element_source.explicit_wait_timeout))
        log.info('Detecting JQuery and waiting for ajax if applicable')
        self.waiter.until(lambda driver: self.driver.execute_javascript("return document.readyState") == "complete")
