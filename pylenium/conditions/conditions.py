from abc import abstractmethod, ABC

from pylenium.core.pylenium import get_pylenium_driver


# The base pylenium condition, if the condition does not match the expected, e.g a Has is False or a HasNot is True
# then pylenium should raise a PyleniumAssertionError with helpful information
class PyCondition(ABC):

    def __init__(self, element, is_not_condition):
        self.driver = get_pylenium_driver()
        self.element = element
        self.is_not_condition = is_not_condition

    @abstractmethod
    def confirm(self):
        pass


class Be(PyCondition):

    def __init__(self, element, is_not_condition):
        super().__init__(element, is_not_condition)

    @abstractmethod
    def confirm(self):
        pass


class Have(PyCondition):

    def __init__(self, element, is_not_condition):
        super().__init__(element, is_not_condition)
        self.is_not_condition = is_not_condition

    @abstractmethod
    def confirm(self):
        pass


class ShouldBe(Be):

    def __init__(self, element):
        super().__init__(element, True)

    @abstractmethod
    def confirm(self):
        pass


class ShouldNotBe(Be):

    def __init__(self, element):
        super().__init__(element, False)

    @abstractmethod
    def confirm(self):
        pass


class ShouldHave(Have):

    def __init__(self, element):
        super().__init__(element, True)

    @abstractmethod
    def confirm(self):
        pass


class ShouldNotHave(Have):

    def __init__(self, element):
        super().__init__(element, False)

    @abstractmethod
    def confirm(self):
        pass
