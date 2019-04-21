import threading

import pytest

from configuration.config import PyleniumConfig
from core.pylenium import start, terminate


@pytest.fixture(scope="function", autouse=True)
def manage_test(request):
    print('THIS THREAD IS: {}'.format(threading.current_thread().ident))
    PyleniumConfig().base_url = "http://localhost:8000/tests/server/static_content/"
    if "page_objects" not in request.keywords:
        _open_file(request.node.get_closest_marker("IT").kwargs["page"])
    yield
    terminate()


def _open_file(name: str):
    start(name)
