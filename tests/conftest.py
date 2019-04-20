import pytest

from core.pylenium import start, terminate


@pytest.fixture(scope='function', autouse=True)
def manage_test(request):
    url = 'http://localhost:8000/tests/server/static_content/{}'
    _open_file(url.format(request.node.get_closest_marker('IT').kwargs['page']))
    yield
    terminate()


def _open_file(name: str):
    start(name)
