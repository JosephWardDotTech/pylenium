import threading

from core.pylenium import start


class TestSomething:

    def test_threads(self):
        t1 = threading.Thread(target=start, args=('http://www.google.com',))
        t2 = threading.Thread(target=start, args=('http://www.google.com',))
        t3 = threading.Thread(target=start, args=('http://www.google.com',))
        t4 = threading.Thread(target=start, args=('http://www.google.com',))
        t5 = threading.Thread(target=start, args=('http://www.google.com',))
        t6 = threading.Thread(target=start, args=('http://www.google.com',))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
