from pylenium.core.pylenium import *


class TestOpen(object):
    pass


assert start('https://www.bbc.co.uk') \
    .goto('https://github.com') \
    .goto('https://www.thesun.co.uk') \
    .url() is 'https://www.thesun.co.uk'
