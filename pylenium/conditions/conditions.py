from abc import abstractmethod, ABC


# The base pylenium condition, if the condition does not match the expected, e.g a Has is False or a HasNot is True
# then pylenium should raise a PyleniumAssertionError with helpful information
class PyCondition(ABC):

    def __init__(self, is_not_condition):
        self.is_not_condition = is_not_condition

    @abstractmethod
    def confirm(self, element):
        pass


class Be(PyCondition):

    def __init__(self, is_not_condition):
        super().__init__(is_not_condition)

    @abstractmethod
    def confirm(self, element):
        pass


class Have(PyCondition):

    def __init__(self, is_not_condition, expected):
        super().__init__(is_not_condition)
        self.expected = expected

    @abstractmethod
    def confirm(self, element):
        pass


class ShouldBe(Be):

    def __init__(self):
        super().__init__(True)

    @abstractmethod
    def confirm(self, element):
        pass


class ShouldNotBe(Be):

    def __init__(self):
        super().__init__(False)

    @abstractmethod
    def confirm(self, element):
        pass


class ShouldHave(Have):

    def __init__(self, expected):
        super().__init__(True, expected)

    @abstractmethod
    def confirm(self, element):
        pass


class ShouldNotHave(Have):

    def __init__(self, expected):
        super().__init__(False, expected)

    @abstractmethod
    def confirm(self, element):
        pass
