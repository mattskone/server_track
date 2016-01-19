"""An asynchronous, RESTful web server."""

import tornado.gen
import tornado.ioloop
import tornado.web

import log


class ServerHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, server_name):
        self.write(log.get_server_log(server_name))

    @tornado.gen.coroutine
    def post(self, server_name):
        log.add_server_log(server_name, self.request.body)
        self.set_status(201)
        self.write(self.request.body)


def make_app():
    return tornado.web.Application([
        (r'/server/(\w+)', ServerHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

