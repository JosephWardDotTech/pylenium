import pytest

from config.config import PyleniumConfig
from core.pylenium import start, terminate


@pytest.fixture(scope='function', autouse=True)
def manage_test(request):
    PyleniumConfig().base_url = 'http://localhost:8000/tests/server/static_content/'
    if 'page_objects' not in request.keywords:
        _open_file(request.node.get_closest_marker('IT').kwargs['page'])
    yield
    terminate()


def _open_file(name: str):
    start(name)
