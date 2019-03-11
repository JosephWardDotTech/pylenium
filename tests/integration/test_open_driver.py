from pylenium.core.pylenium import *


class TestOpen(object):

    # Page Objects and business logic sold separately!
    def test_my_login(self):
        start('https://www.google.co.uk')
        find(By.NAME, 'q').set_value("Cheese!")
        find(By.CSS_SELECTOR, '#submit').click()
        find(By.CSS_SELECTOR, '#password').should_have(Text("Hello, Simon!"))
        terminate()
