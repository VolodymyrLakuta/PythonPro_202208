class My_exceptions (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return f"{self.message}"

