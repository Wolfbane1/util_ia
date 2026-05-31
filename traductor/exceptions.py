"""
Custom exception module for Document Translation Agent.

Provides custom exceptions for handling translation errors,
unsupported formats, and API errors.
"""


class TranslationException(Exception):
    """
    Base exception class for all translation-related errors.

    This exception serves as the primary exception class for the
    Document Translation Agent. All other translation exceptions
    inherit from this class.

    Attributes:
        message (str): A descriptive error message.
        errors (str): Additional error details if available.
        messagio (str): Default error message prefix.
    """

    def __init__(self, message, errors="", messagio="Error during translation"):
        super().__init__(f"{messagio} - {message}", errors)
        self.message = message
        self.errors = errors


class TranslationUnsupportedFormatError(TranslationException):
    """
    Exception raised when an unsupported file format is encountered.

    This exception inherits from TranslationException and is raised
    when a file format is not supported by the translation engine.

    Attributes:
        format (str): The unsupported file format that caused the error.
    """

    def __init__(self, message="", errors="", format=None, messagio="Unsupported file format"):
        if format:
            message = f"Format '{format}' is not supported. Supported formats: PDF, DOCX, TXT"
        super().__init__(message, errors, messagio)
        self.format = format


class TranslationAPIError(TranslationException):
    """
    Exception raised when a translation API error occurs.

    This exception inherits from TranslationException and is raised
    when there are errors communicating with the Ollama API or
    when the API returns error status codes (401, 429, 500).

    Attributes:
        status_code (int): The HTTP status code returned by the API.
    """

    def __init__(self, message="", errors="", status_code=None, messagio="Translation API error"):
        if status_code:
            message = f"API returned status code {status_code}"
        super().__init__(message, errors, messagio)
        self.status_code = status_code
