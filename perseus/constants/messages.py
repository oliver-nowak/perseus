"""A file containing the user facing messages in the system."""


class ErrorMessages(object):
    """Error related user messages."""

    class APIErrors(object):
        """Error messages for the API's custom error handler."""

        NOT_FOUND = "Not found."
        SERVER_ERROR = "Internal server error."
        METHOD_NOT_ALLOWED = "Method not allowed."
        NOT_AUTHORIZED = "Authentication failed."
        FORBIDDEN = "You do not have permissions to perform this action."
        INVALID_REQUEST_PARAMS = "Invalid request parameters."
        BAD_REQUEST = "Bad request."
        CONFLICT = "Conflict."
        NOT_IMPLEMENTED_YET = "This endpoint has not been implemented yet."
        DB_ERROR = "Failed committing to the database."


class LogMessages(object):
    """Messages for logging"""
    APP_INITIALIZING = "Application is done initializing"
    RETURNING_NON_200_OR_400 = "API returning non 200/400: {}"
    DB_ERROR = "Error committing to database after request execution."
