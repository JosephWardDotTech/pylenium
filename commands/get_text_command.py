from commands.command import Command


class GetTextCommand(Command):
    def __init__(self, pyelement):
        super().__init__(pyelement)

    def execute(self) -> str:
        return self.py_element.element.text
