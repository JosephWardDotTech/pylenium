from pylenium.core.pylenium import start, terminate


class TestOpen(object):

    def test_redirection(self):
        github_url = 'https://github.com/'
        expected_url = start('https://www.bbc.co.uk') \
            .goto(github_url) \
            .url()
        assert expected_url == github_url
        terminate()
