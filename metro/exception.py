class Metro_Exception(Exception):
    def __init__(self, type, description):
        self.type = type
        self.description = description

    def __str__(self):
        return f'{self.type}Error: {self.description}'