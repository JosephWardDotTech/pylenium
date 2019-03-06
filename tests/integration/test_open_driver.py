from pylenium.core.pylenium import *


class TestOpen(object):

    def test_driver_open(self):
        start('https://www.bbc.co.uk') \
            .goto('https://github.com') \
            .goto('https://www.thesun.co.uk') \
            .quit()
