import logging
import threading

import pytest

from configuration.config import PyleniumConfig
from core.pylenium import start, terminate
from web_drivers.driver import PyleniumDriver

log = logging.getLogger('pylenium')


@pytest.fixture(scope="function", autouse=True)
def manage_test(request):
    PyleniumConfig().base_url = "http://localhost:8000/tests/server/static_content/"
    local = threading.local()
    local.driver = PyleniumDriver(PyleniumConfig(), None, None)
    if "page_objects" not in request.keywords:
        _open_file(request.node.get_closest_marker("IT").kwargs["page"])
    yield
    terminate()


def _open_file(name: str):
    start(name)
