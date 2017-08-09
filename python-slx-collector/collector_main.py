"""
Copyright 2017 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import asyncore
import logging
import logging.config
import os
import yaml
import socket
from timeit import default_timer as timer

from collector_handler import CollectorHandler

#logging.basicConfig(level=logging.DEBUG, 
#  format='%(asctime)-15s:%(levelname)8s:[%(threadName)-15s::%(name)-20s:%(funcName)s(%(lineno)d)] %(message)s'
#  )

def setup_logging(
    default_path='log.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    #print('%s value is \'%s\'' % (env_key, value))
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        #print('Using %s config' % path)
        logging.config.dictConfig(config)
    else:
        #print('Using default config')
        logging.basicConfig(level=default_level)

setup_logging() 

logger = logging.getLogger('CollectorServer')

class CollectorServer(asyncore.dispatcher):

  def __init__(self, address, json_dir=None):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.bind(address)
    self.address = self.socket.getsockname()
    self.json_dir = json_dir
    self.listen(1)
    return

  def handle_accept(self):
    # Called when a client connects to our socket
    client = self.accept()
    logger.debug('client -> %s', client[1])
    CollectorHandler(sock=client[0], json_dir=self.json_dir)
    return

  def handle_close(self):
    logger.debug('closing...')
    self.close()
    return

def runAsServer(args):
#  logger.info("Running as server %s " % args)
  host = ''
  if args.host != None: host = args.host
  logger.info("Starting server with \"%s:%d\"" % (host, args.port))
  address = (host, args.port)
  server = CollectorServer(address, args.json)

  asyncore.loop()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Helps running Collector client/server')
    subparsers = parser.add_subparsers(dest='type')
    subparsers.required = True


    # create the parser for the "server" command
    server_parser = subparsers.add_parser('server', help='Runs in server mode ')
    server_parser.add_argument('--host', required=False, help='Hostname to be used; if not specified binds to all')
    server_parser.add_argument('--port', required=True, type=int, help='Port number to be used')
    server_parser.add_argument('--json', required=False, help='Produce json output in specified directory')
    server_parser.set_defaults(func=runAsServer)

    args = parser.parse_args()
    
    #print('Args: %s' % args)
    if (args.type == None):
        parser.print_help()
        sys.exit(-1)


    start = timer()
    args.func(args)
    end = timer()
    print('Run in "%s" mode took %8.3f seconds (elapsed+sleep)' %  (args.type, (end-start)))
