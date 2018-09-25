"""Main bottle app.
Contains all of the sub-applications, as well as some global routes for HTTP errors.
"""

import json
import logging

import bottle
from webargs.bottleparser import parser as arg_parser

from perseus.constants.messages import ErrorMessages, LogMessages
from perseus.routes import main_routes
from perseus.util import web


logger = logging.getLogger(__name__)
# suppress the following logs so we don't get blasted with 3rd party debug messages...
SUPPRESS_LOGS = ['boto', 'botocore', 'boto3']
for log_name in SUPPRESS_LOGS:
    logging.getLogger(log_name).setLevel(logging.ERROR)


class PerseusApp(object):
    """The main application that is to be served for the service"""

    # mapping of HTTP status codes to relevant error messages
    STATUS_CODE_TO_MESSAGES = {
        400: ErrorMessages.APIErrors.BAD_REQUEST,
        401: ErrorMessages.APIErrors.NOT_AUTHORIZED,
        403: ErrorMessages.APIErrors.FORBIDDEN,
        404: ErrorMessages.APIErrors.NOT_FOUND,
        405: ErrorMessages.APIErrors.METHOD_NOT_ALLOWED,
        409: ErrorMessages.APIErrors.CONFLICT,
        422: ErrorMessages.APIErrors.INVALID_REQUEST_PARAMS,
        500: ErrorMessages.APIErrors.SERVER_ERROR,
        501: ErrorMessages.APIErrors.NOT_IMPLEMENTED_YET
    }

    def __init__(self, config):
        self.config = config
        self.port = config.get('port', 8028)
        # set logging options from config
        logging.basicConfig(
            format=config.get('log_format', '%(asctime)s %(levelname)s: %(message)s'),
            level=config.get('log_level', logging.INFO)
        )

        self.app = bottle.Bottle()

        routes_app = main_routes.App()

        self.app.merge(routes_app)

        self.app.route(path='/perseus/v1/heartbeat', callback=self.heartbeat)

        self.route_for_errors()
        logger.info(LogMessages.APP_INITIALIZING)

    def heartbeat(self):
        """A simple health check endpoint"""

        return {}

    def route_for_errors(self):
        """Method creates all the routes for custom error handling on the app.
        All errors are returns as JSON responses with an error field.
        """
        self.app.default_error_handler = self.custom_error  # override bottle default error handler

        @arg_parser.error_handler
        def arg_parse_error(err):
            """Handler for webargs errors.
            Called when request arguments cannot be validated, and raises an exception with the message details.
            """
            status_code = 400
            messages = getattr(err, 'messages', None)

            web.response_error(status_code=status_code, details=messages)

    def custom_error(self, error_exc):
        """Custom error handler for all exceptions encountered."""

        status_code = error_exc.status_code
        # try to get the error message from the status code mapping. otherwise, used the exception body
        error_message = PerseusApp.STATUS_CODE_TO_MESSAGES.get(status_code, error_exc.body)
        if not error_message:  # if there is no message mapping, and HTTPError.body is empty, use status
            error_message = error_exc.status
        ret_val = dict(
            error=error_message
        )
        if error_exc.message:  # add details if an exception message is present
            ret_val['details'] = error_exc.message
        if 400 != status_code:
            logger.info(LogMessages.RETURNING_NON_200_OR_400.format(error_message))
        return web.response_json(
            data=ret_val,
            status=status_code
        )

    @staticmethod
    def from_config(fn):
        with open(fn) as fp:
            config = json.load(fp)
        return PerseusApp(config)
