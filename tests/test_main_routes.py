from perseus.app import PerseusApp

from webtest import TestApp

service = PerseusApp.from_config('./config/perseus.conf')


class TestRoutes(object):

    def test_heartbeat_route_returns_200(self):
        test_app = TestApp(service.app)
        resp = test_app.get('/perseus/v1/heartbeat')
        assert resp.status == '200 OK'
        assert resp.status_int == 200

    def test_healthcheck_route_returns_200(self):
        test_app = TestApp(service.app)
        resp = test_app.get('/perseus/v1/health')
        assert resp.status_int == 200

    def test_get_pegasus_returns_200(self):
        test_app = TestApp(service.app)
        resp = test_app.get('/perseus/v1/pegasus/1337')
        assert resp.status == '200 OK'
        assert resp.status_int == 200
        assert resp.json == {'url': '/perseus/v1/pegasus/1337', 'message': 'OK'}

    def test_get_monster_status_returns_200(self):
        test_app = TestApp(service.app)
        resp = test_app.put('/perseus/v1/monsters/gorgon/status/1')
        assert resp.status == '200 OK'
        assert resp.status_int == 200
        assert resp.json == {'url': '/perseus/v1/monsters/gorgon/status/1', 'message': 'OK'}

    def test_get_treasure_returns_200(self):
        test_app = TestApp(service.app)
        resp = test_app.post('/perseus/v1/treasure/vorpalsword')
        assert resp.status == '200 OK'
        assert resp.status_int == 200
        assert resp.json == {'url': '/perseus/v1/treasure/vorpalsword', 'message': 'OK'}

