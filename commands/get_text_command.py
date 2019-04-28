from commands.command import Command


class GetTextCommand(Command):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def execute(self) -> str:
        return self.element.wrapped_element.text
