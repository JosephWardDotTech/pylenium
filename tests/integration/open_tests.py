from pylenium.core.pylenium import *


class TestOpen(object):
    pass


driver = start('https://www.google.co.uk') \
    .maximize() \

driver2 = start('https://www.bbc.co.uk') \
    .goto('https://github.com') \
    .goto('https://www.thesun.co.uk') \
    .quit()
