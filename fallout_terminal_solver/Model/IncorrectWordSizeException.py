class IncorrectWordSizeException(Exception):
    def __init__(self, message):

        super(IncorrectWordSizeException, self).__init__(message)