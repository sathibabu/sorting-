#!/usr/bin/env python
import string,cgi,time
from os import curdir, sep
import urllib2 
import BaseHTTPServer
import CGIHTTPServer
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 


def main():
	try:
		server = BaseHTTPServer.HTTPServer
		handler = CGIHTTPServer.CGIHTTPRequestHandler
		server_address = ("", 8000)
		handler.cgi_directories = ["/"]

		httpd = server(server_address, handler)
		httpd.serve_forever()
	except KeyboardInterrupt:
		httpd.socket.close()	

if __name__ == '__main__':
    main()