from pylenium.commands.command import Command


class GetTextCommand(Command):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def execute(self) -> str:
        self._wait_for_page_ready_state()
        return self.element.text
