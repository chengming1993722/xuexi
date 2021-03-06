from tornado import httpserver,ioloop,options,web
from tornado.options import define,options

define('port',default=8000,help='run on the given port',type=int)
class IndexHandler(web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting','Hello')
        self.write(greeting+',friendly user!')

if __name__ == '__main__':
    options.parse_command_line()
    app = web.Application(handlers=[(r"/", IndexHandler)])
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()
