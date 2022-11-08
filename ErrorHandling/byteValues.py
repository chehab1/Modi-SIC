class invalidByteValue(Exception):
    """raised when Invalid Byte Value"""
    def __init__(self, LCounter, message):
        self.LCounter = LCounter
        self.message = message + LCounter
        print(self.message)
        super().__init__(self.message)

