import logging
import threading

import pytest

from configuration.config import PyleniumConfig
from core.pylenium import terminate, start

log = logging.getLogger("pylenium")


@pytest.fixture(scope="function", autouse=True)
def manage_test(request):
    PyleniumConfig().base_url = "http://localhost:8000/tests/server/static_content/"
    start(request.node.get_closest_marker("IT").kwargs["page"])
    yield
    terminate()

