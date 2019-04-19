import pytest


@pytest.fixture(scope='function', autouse=True)
def auto_close(request):
    def auto_close_browser():
        from common.pylenium import terminate
        terminate()

    request.addfinalizer(auto_close_browser)
