from commands.command import Command


class GetTextCommand(Command):
    def __init__(self, py_element):
        super().__init__(py_element)

    def execute(self) -> str:
        return self.py_element.element.text
