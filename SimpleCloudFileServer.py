#!/usr/bin/python

import time
import BaseHTTPServer
import json

HOST_NAME = "localhost"
PORT_NUMBER = 8000 # Magic number. Can't bind under 1024 on normal user accounts; port 80 is the normal HTTP port

class SimpleCloudFileServer(BaseHTTPServer.BaseHTTPRequestHandler):
	def sendHeader(self, response=200, contentType="application/json"):
		self.send_response(response)
		self.send_header("Content-type", contentType)
		self.end_headers()
	
	def do_HEAD(self):
		self.sendHeader()
	
	def do_GET(self):
		self.sendHeader()
		self.wfile.write("hi")

def printServerMessage(customMessage):
	print customMessage, "(Time: %s, Host: %s, port: %s)" % (time.asctime(), HOST_NAME, PORT_NUMBER)
	
if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), SimpleCloudFileServer)
	
	printServerMessage("Server startup")
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	printServerMessage("Server stop")
