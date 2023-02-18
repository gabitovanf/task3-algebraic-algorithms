class MatrixInvalidException(Exception):
    """
    Matrix passed is invalid
    """
    def __init__(self):
        self.message = "Matrix passed is invalid"

    def __str__(self) -> str:
        return self.message
