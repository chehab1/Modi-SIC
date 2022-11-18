
class LabelNotFound(Exception):
    """Exception raised when label not found"""
    def __init__(self, val, temp):
        self.message = 'Value ' + val + ' Not Found in Labels in the instruction ' + temp
        super().__init__(self.message)
