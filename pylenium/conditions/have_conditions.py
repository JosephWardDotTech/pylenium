from pylenium.conditions.conditions import ShouldHave


class Text(ShouldHave):

    def __init__(self, expected: str):
        super().__init__(expected)

    def confirm(self, element):
        pass


class ExactText(ShouldHave):

    def __init__(self, expected):
        super().__init__(expected)

    def confirm(self, element):
        pass


class Attribute(ShouldHave):

    def __init__(self, expected):
        super().__init__(expected)

    def confirm(self, element):
        pass


class Value(ShouldHave):

    def __init__(self, expected):
        super().__init__(expected)

    def confirm(self, element):
        pass
