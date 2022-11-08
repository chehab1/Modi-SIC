

class LabelNotFound(Exception):
    """Exception raised when label not found"""
    def __init__(self , message):
        self.message = message
        print(self.message)
        super().__init__(self.message)