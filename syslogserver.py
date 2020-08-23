"""
* JBoss, Home of Professional Open Source.
* Copyright 2020 Red Hat, Inc., and individual contributors
* as indicated by the @author tags.
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http: // www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"""

import logging
import time
import threading
import socketserver

"""
* Syslog Server in Python that is able to receive UDP & TCP based syslog
* entries on a specified port and save them to a file
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class syslogServer:
	
	""" Create new instance
        @param host : the IP address of the host
        @param tcp_port : the port to open tcp socket connection on
		@param udp_port : the port to open udp socket connection on
        @param log_file : the port to open tcp socket connection on    
	"""
	
	def __init__(self,host='127.0.0.1',tcp_port=514, udp_port=1514, log_file='audit.log'):
		self.log_file = log_file
		self.host = host
		self.tcp_port = tcp_port
		self.udp_port = udp_port
		logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=self.log_file, filemode='a')

	class SyslogUDPHandler(socketserver.BaseRequestHandler):

		def handle(self):
			data = bytes.decode(self.request[0].strip(), encoding="utf-8")
			socket = self.request[1]
			print( "%s : " % self.client_address[0], str(data.encode("utf-8")))
			logging.info(str(data.encode("utf-8")))

	class SyslogTCPHandler(socketserver.BaseRequestHandler):

		End = '\n'
		def join_data(self, total_data):
			final_data = ''.join(total_data)
			for data in final_data.split(self.End):
				print( "%s : " % self.client_address[0], str(data))
				logging.info(str(data))

		def handle(self):
			total_data = []
			while True:
				data = self.request.recv(8192)
				data = data.decode("utf-8")
				if(len(data)>=1):
					print(data[62:])
					logging.info(data[62:])

	def start(self):
		try:
			# UDP server
			udpServer = socketserver.UDPServer((self.host, self.udp_port), self.SyslogUDPHandler)
			udpThread = threading.Thread(target=udpServer.serve_forever)
			udpThread.daemon = True
			udpThread.start()
			
			# TCP server
			tcpServer = socketserver.TCPServer((self.host, self.tcp_port), self.SyslogTCPHandler)
			tcpThread = threading.Thread(target=tcpServer.serve_forever)
			tcpThread.daemon = True
			tcpThread.start()
			while True:
				time.sleep(1)

		except (IOError, SystemExit):
			raise
		
		except KeyboardInterrupt:
			udpServer.shutdown()
			udpServer.server_close()
			tcpServer.shutdown()
			tcpServer.server_close()
			print ("Crtl+C Pressed. Shutting down.")
