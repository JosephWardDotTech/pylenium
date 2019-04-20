import logging
log = logging.getLogger('pylenium')


# refreshes the underlying web element to prevent staleness etc
def anti_staleness(f):
    def wrapper(*args):
        log.info('Re-finding the web element')
        return f(*args)
    return wrapper


def ready_state(f):
    def wrapper(*args):
        # js, stability, ajax etc!
        log.info('Stabilizing the page')
        return f(*args)
    return wrapper
