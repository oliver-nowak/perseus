"""
The app that serves the endpoints
"""

import logging
import bottle


from perseus.util import web

logger = logging.getLogger(__name__)


def App():
    app = bottle.Bottle()

    @app.get('/perseus/v1/health')
    def get_health():
        return web.response_json("OK")

    @app.get('/perseus/v1/pegasus/<horse_id>')
    def get_pegasus(horse_id):
        return {'url': '/perseus/v1/pegasus/{}'.format(horse_id), 'message': 'OK'}

    @app.put('/perseus/v1/monsters/<monster_id>/status/<status_id>')
    def assign_monster_status(monster_id, status_id):
        return {'url': '/perseus/v1/monsters/{}/status/{}'.format(monster_id, status_id), 'message': 'OK'}

    @app.post('/perseus/v1/treasure/<treasure_name>')
    def create_treasure(treasure_name):
        return {'url': '/perseus/v1/treasure/{}'.format(treasure_name), 'message': 'OK'}

    return app
