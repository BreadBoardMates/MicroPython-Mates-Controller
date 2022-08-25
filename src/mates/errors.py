class MatesError():
    """
    An enumerated class representing all possible error states of the
    Python Mates Serial controller.

    Attributes
    ----------
    MATES_ERROR_NONE: int
        - indicates no error state.

    MATES_ERROR_COMMAND_FAILED: int
        - indicates requested command failed.

    MATES_ERROR_COMMAND_TIMEOUT: int
        - indicates requested command timed out without a response.

    MATES_ERROR_RESPONSE_TIMEOUT: int
        - indicates response requested from controller timed out.
    
    MATES_ERROR_NOT_INITIALIZED: int
        - The library hasn't been initialized yet
    
    MATES_ERROR_SYNC_TIMEOUT: int
        - The synchronization attempt reached specified timeout

    MATES_ERROR_SYNC_ERROR: int
        - Invalid active page or no reply received after sync
    """
    MATES_ERROR_NONE = 0
    MATES_ERROR_COMMAND_FAILED = 1
    MATES_ERROR_COMMAND_TIMEOUT = 2
    MATES_ERROR_RESPONSE_TIMEOUT = 3
    MATES_ERROR_NOT_INITIALIZED = 4
    MATES_ERROR_SYNC_TIMEOUT = 5
    MATES_ERROR_SYNC_ERROR = 6