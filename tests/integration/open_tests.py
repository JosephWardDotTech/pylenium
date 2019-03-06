from pylenium.core.pylenium import *


class TestOpen(object):
    pass


driver = start()
driver.maximize()
driver.goto('https://www.google.co.uk')
driver.quit()
