from pylenium.conditions.conditions import ShouldHave


class Text(ShouldHave):

    def __init__(self, element):
        super().__init__(element)

    def confirm(self):
        pass


class ExactText(ShouldHave):

    def __init__(self, element):
        super().__init__(element)

    def confirm(self):
        pass


class Attribute(ShouldHave):

    def __init__(self, element):
        super().__init__(element)

    def confirm(self):
        pass


class Value(ShouldHave):

    def __init__(self, element):
        super().__init__(element)

    def confirm(self):
        pass
