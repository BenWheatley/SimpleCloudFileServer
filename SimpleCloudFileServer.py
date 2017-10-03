#!/usr/bin/python

import time
import BaseHTTPServer
import json

HOST_NAME = "localhost"
PORT_NUMBER = 8000 # Magic number. Can't bind under 1024 on normal user accounts; port 80 is the normal HTTP port

class SimpleCloudFileServer(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write("hi")

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), SimpleCloudFileServer)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
