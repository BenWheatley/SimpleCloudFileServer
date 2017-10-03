#!/usr/bin/python2.7

import time
import BaseHTTPServer
import json

HOST_NAME = "localhost"
PORT_NUMBER = 8000 # Magic number. Can't bind under 1024 on normal user accounts; port 80 is the normal HTTP port

class SimpleCloudFileServer(BaseHTTPServer.BaseHTTPRequestHandler):
	fileData = {}
	
	def sendHeader(self, response=200, contentType="application/json"):
		self.send_response(response)
		self.send_header("Content-type", contentType)
		self.end_headers()
	
	def do_HEAD(self):
		self.sendHeader()
	
	def do_GET(self):
		filename = self.path[1:]
		
		if (filename=="index.json"):
			self.sendHeader()
			self.wfile.write(json.dumps(self.fileData.keys()))
			
		elif filename not in self.fileData:
			self.sendHeader(response=404)
			
		else:
			# While this claims the content being returned is image/jpeg, the upload handler doesn't actually enforce that
			self.sendHeader(response=200, contentType="image/jpeg")
			self.wfile.write(self.fileData[filename])
	
	def do_POST(self):
		self.sendHeader()
		newFileName = str(self.fileData.__len__()) # Old syntax because macOS uses old version of python
		contentLength = int(self.headers.getheader('content-length'))
		newFileData = self.rfile.read(contentLength) # can't just .read() because that will hang until the socket closes
		
		self.fileData[newFileName] = newFileData
		
		result = {"new_file_name": newFileName}
		self.wfile.write(json.dumps(result))

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
