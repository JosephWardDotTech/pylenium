from core.pylenium import start


class IntegrationTest:

    @staticmethod
    def open_file(file_name: str):
        start('http://localhost:8000/static_content/' + file_name)
