import logging

from core.elements import PyElement

log = logging.getLogger("pylenium")


# refreshes the underlying web element to prevent staleness etc
def anti_staleness(f):
    def wrapper(*args):
        log.info("Lazy loading or refreshing of webelements!")
        args[0].wrapped_element = PyElement(
            args[0].driver.driver.find_element(
                args[0].locator.by, args[0].locator.selector
            )
        )
        return f(*args)

    return wrapper


def ready_state(f):
    def wrapper(*args):
        # js, stability, ajax etc!
        log.info("Stabilizing the page")
        return f(*args)

    return wrapper
