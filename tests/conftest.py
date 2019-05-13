import logging
import os
import subprocess
import time

import pytest

from pylenium.core.pylenium import terminate, get_config, start

log = logging.getLogger("pylenium")


@pytest.fixture(scope='session', autouse=True)
def web_server_for_integration_tests(request):
    if os.environ.get('PYLENIUM_TRAVIS'):
        log.info('Travis detected, Integration server is started automatically')
        return
    else:
        http_server = subprocess.Popen('python -m http.server', shell=True)
        time.sleep(2.5)  # let the http server 'ready-up'
        request.addfinalizer(http_server.kill)
    return


@pytest.fixture(scope="function", autouse=True)
def manage_test(request):
    request.addfinalizer(terminate)
    get_config().base_url = "http://localhost:8000/tests/server/static_content/"
    start(request.node.get_closest_marker("IT").kwargs["page"])
