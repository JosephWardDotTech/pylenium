from commands.command import Command


class ClickCommand(Command):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def execute(self) -> None:
        return self.element.wrapped_element.click()
