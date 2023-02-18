class MatrixInvalidParametersException(Exception):
    """
    Parameters passed to Matrix() are invalid:
    one need to pass rowsList or dimensions: rows and cols
    """
    def __init__(self):
        self.message = "Need to pass rowsList or dimensions: rows and cols"

    def __str__(self) -> str:
        return self.message
