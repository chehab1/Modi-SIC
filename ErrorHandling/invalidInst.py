class InvalidInst(Exception):
    """Exception raised when label not found"""
    def __init__(self, inst):
        self.message = 'Instruction  ' + inst + ' is invalid'
        super().__init__(self.message)