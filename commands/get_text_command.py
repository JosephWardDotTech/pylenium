from commands.command import Command


class GetTextCommand(Command):
    def __init__(self, element):
        super().__init__(element)

    def execute(self) -> str:
        return self.py_element.wrapped_element.text
