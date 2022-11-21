class InvalidInst(Exception):
    """Exception raised when label not found"""
    def __init__(self, inst , index):
        self.message = 'Instruction  ' + inst + ' is invalid in line -> ' + index
        super().__init__(self.message)