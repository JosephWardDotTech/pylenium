import logging
import os
import subprocess

import pytest

from configuration.config import PyleniumConfig
from core.pylenium import terminate, start

log = logging.getLogger("pylenium")


@pytest.fixture(scope='session', autouse=True)
def web_server_for_integration_tests(request):
    if os.environ.get('PYLENIUM_TRAVIS'):
        log.info('Travis detected, travis can manage the integration server!')
        return
    http_server = subprocess.Popen('python -m http.server -d ./tests/server/static_content/')
    request.addfinalizer(http_server.kill)
    return


@pytest.fixture(scope="function", autouse=True)
def manage_test(request):
    request.addfinalizer(terminate)
    PyleniumConfig().base_url = "http://localhost:8000/"
    start(request.node.get_closest_marker("IT").kwargs["page"])
