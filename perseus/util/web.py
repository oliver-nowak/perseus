"""Web related utility functions"""

import json

import bottle


def response_json(data, status=200):
    """Turn a Python object into a JSON response with a relevant HTTP status code."""

    return bottle.HTTPResponse(
        status=status,
        body=json.dumps(data),
        content_type='application/json'
    )

def response_error(status_code, details=None):
    """Return an error response.
    Raises an HTTPError so that we go through our custom error handler. The exception message is used as a vehicle for
    delivering more specific details in the API response.
    """
    exc = bottle.HTTPError(status=status_code)
    if details:  # add the message for the exception.
        exc.message = details
    raise exc