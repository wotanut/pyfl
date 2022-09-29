class PYFL_Error(Exception):
    """Base class for all PYFL errors."""
    def __init__(self, message):
        self.message = message

class invalid_api_key(PYFL_Error):
    """Raised when the API key is invalid."""
    def __init__(self, message):
        self.message = message

class invalid_endpoint(PYFL_Error):
    """Raised when the endpoint is invalid."""
    def __init__(self, message):
        self.message = message

class invalid_parameter(PYFL_Error):
    """Raised when the parameter is invalid."""
    def __init__(self, message):
        self.message = message

class invalid_response(PYFL_Error):
    """Raised when the response is invalid."""
    def __init__(self, message):
        self.message = message