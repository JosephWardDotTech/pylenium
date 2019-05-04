from pylenium.commands import Command


class GetTextCommand(Command):
    def __init__(self, driver, element):
        super().__init__(driver, element)

    def execute(self) -> str:
        self.wait_for_element()
        self.wait_for_page_to_be_ready()
        return self.element.wrapped_element.text
