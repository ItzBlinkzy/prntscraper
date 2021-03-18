class PrntScraperError(Exception):
    """Base class for other exceptions"""
    pass


class NoImageFolderError(PrntScraperError):
    """Raised when there is no ./image folder located in module import directory"""
    def __init__(self):
        self.message = "\x1b[0;31;40m" "There is no ./images folder in this directory, please create this folder." "\x1b[0m"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ValueTooSmallError(PrntScraperError):
    """Raised when value is too small"""
    def __init__(self, value):
        self.value = value
        self.message = "\x1b[0;31;40m" f"{self.value} is too small" "\x1b[0m"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ValueTooLargeError(PrntScraperError):
    """Raised when value is too large"""
    def __init__(self, value):
        self.value = value
        self.message = "\x1b[0;31;40m" f"{self.value} is too large." "\x1b[0m"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class NotAnIntegerError(PrntScraperError):
    """Raised when value entered is not an integer"""
    def __init__(self, value):
        self.value = value
        self.message = "\x1b[0;31;40m" f"{self.value} is not an integer" "\x1b[0m"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class AlphabeticCharsOnlyError(PrntScraperError):
    """Raised when values are not alphabetic"""
    def __init__(self, value):
        self.value = value
        self.message = "\x1b[0;31;40m" f"{self.value} is not an alphabetic string" "\x1b[0m"
        super().__init__(self.message)

    def __str__(self):
        return self.message
