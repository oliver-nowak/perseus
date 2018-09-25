"""Main entry point.
Parses command line arguments and serves the main app (TMOABApp) with the given config.
"""

import optparse

import bottle

from perseus.app import PerseusApp


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-c', '--conf', help='JSON config file')
    opts, args = parser.parse_args()
    service = PerseusApp.from_config(opts.conf)
    bottle.run(service.app, host='0.0.0.0', port=service.port)
