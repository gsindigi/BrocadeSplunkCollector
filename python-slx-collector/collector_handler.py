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

import asynchat
import datetime
import json
import struct
import tempfile
import logging
import os

from google.protobuf import text_format
from google.protobuf import json_format
from protos.brocade_collector_pb2 import CollectorResponse as CollectorResponse

class CollectorHandler(asynchat.async_chat):

  def __init__(self, sock, json_dir=None):
    self.received_data = []
    self.l = logging.getLogger('CollectorHandler')
    asynchat.async_chat.__init__(self, sock)
    self.process_data = self._read_length
    if json_dir != None:
      self.json_file = tempfile.NamedTemporaryFile(bufsize=0,dir=json_dir,suffix='.json')
      self.l.info('Dumping to file %s', self.json_file)
    else:
      self.json_file = None
    self.set_terminator(4)
    return

  def collect_incoming_data(self, data):
    """Read an incoming message from the client and put it into our outgoing queue."""
    self.l.debug('data -> (%d bytes):"%s"', len(data), data)
    self.received_data.append(data)

  def found_terminator(self):
    """The end of a command or message has been seen."""
    self.l.debug('found_terminator()')
    self.process_data()

  def _read_length(self):
    """We have the length, read it """
    msg_length = struct.unpack('!I', self.received_data[0])[0]
    self.l.debug('msg_length = %d', msg_length)
    self.set_terminator(msg_length)
    self.process_data = self._read_message
    self.received_data = []

  def _read_message(self):
    """We have the message, read it """
    msg = ''.join(self.received_data)
    self.l.debug('msg = %s', msg)
    try:
      cr = CollectorResponse()
      cr.ParseFromString(msg)
      s_resp = text_format.MessageToString(cr, as_one_line=True)
      self.l.debug('Received Response: %s' % s_resp)
      if self.json_file != None:
        json_str = json_format.MessageToJson(cr, including_default_value_fields=True)
        json_obj = json.loads(json_str)
        json_obj['utctime'] = str(datetime.datetime.utcnow())
        json.dump(json_obj, self.json_file)
        self.json_file.write('\n')
        #self.json_file.write('%s\n'%(json_format.MessageToJson(cr, including_default_value_fields=True)))
        print(json.dumps(json_obj))
    except Exception as e:
      self.l.exception('Failed to convert CollectorResponse')  
    self.set_terminator(4)
    self.process_data = self._read_length
    self.received_data = []


