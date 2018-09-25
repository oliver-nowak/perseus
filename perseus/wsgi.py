import sys

from perseus import app


perseus = app.PerseusApp.from_config(sys.argv[1])
application = perseus.app
