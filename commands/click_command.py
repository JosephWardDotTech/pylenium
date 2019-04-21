from commands.command import Command


class ClickCommand(Command):
    def __init__(self, py_element):
        super().__init__(py_element)

    def execute(self):
        return self.py_element.wrapped_element.click()
