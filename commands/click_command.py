from commands.command import Command


class ClickCommand(Command):
    def __init__(self, element):
        super().__init__(element)

    def execute(self) -> None:
        return self.py_element.wrapped_element.click()
