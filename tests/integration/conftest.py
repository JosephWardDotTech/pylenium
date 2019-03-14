import pytest


@pytest.fixture(scope='function', autouse=True)
def auto_close(request):
    def auto_close_browser():
        from pylenium.core.pylenium.pylenium import terminate
        terminate()

    request.addfinalizer(auto_close_browser)



