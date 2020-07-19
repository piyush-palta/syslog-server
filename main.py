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

from syslogserver import syslogServer
import sys

"""
* Executes Syslog Server
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

# syslogServer(host, tcp_port, udp_port, log_file)
# object initialized with default param 

host = '127.0.0.1'
tcp_port = 1525
udp_port = 1514
log_file = 'audit.log'

if len(sys.argv)==5 :
    host = sys.argv[1]
    tcp_port = int(sys.argv[2])
    udp_port = int(sys.argv[3])
    log_file = sys.argv[4]

elif len(sys.argv)==4 :
    host = sys.argv[1]
    tcp_port = int(sys.argv[2])
    udp_port = int(sys.argv[3])

elif len(sys.argv)==3 :
    host = sys.argv[1]
    port = int(sys.argv[2])

elif len(sys.argv)==2 :
    host = sys.argv[1]

server = syslogServer(host,tcp_port, udp_port, log_file)      
server.start()
