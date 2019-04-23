import logging
import subprocess
import sys
import time

import pytest

from configuration.config import PyleniumConfig
from core.pylenium import terminate, start

log = logging.getLogger("pylenium")


@pytest.fixture(scope='session', autouse=True)
def web_server_for_integration_tests():
    import http.server
    subprocess.Popen('python -m http.server -d ./tests/server/static_content')
    time.sleep(5)
    yield


@pytest.fixture(scope="function", autouse=True)
def manage_test(request):
    PyleniumConfig().base_url = "http://localhost:8000/"
    start(request.node.get_closest_marker("IT").kwargs["page"])
    yield
    terminate()

