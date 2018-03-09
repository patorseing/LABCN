# !/usr/bin/python

import SimpleHTTPServer
import SocketServer

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print "I received a GET request"
        self.wfile.write("LOVE U ALL")


PORT = 3605

httpd = SocketServer.TCPServer(('', PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()
