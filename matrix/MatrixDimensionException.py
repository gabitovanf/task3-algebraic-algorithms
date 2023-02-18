class MatrixDimensionException(Exception):
    """
    Matrices' dimesions passed are not suitable for the operation
    """
    def __init__(self):
        self.message = "Matrices' dimesions passed are not suitable for the operation"

    def __str__(self) -> str:
        return self.message
