"""A server that handles a connection with an OpenBCI board and serves that
data over both a UDP socket server and a WebSocket server.

Requires:
  - pyserial
  - asyncio
  - websockets
"""

import cPickle as pickle
import open_bci
import socket


class UDPServer(object):

  def __init__(self, ip, port):
    self.ip = ip
    self.port = port
    self.server = socket.socket(
        socket.AF_INET, # Internet
        socket.SOCK_DGRAM)

  def send_data(self, data):
    self.server.sendto(data, (self.ip, self.port))

  def handle_sample(self, sample):
    self.send_data(pickle.dumps(sample))


obci = open_bci.OpenBCIBoard('/dev/tty.usbmodem1411', 115200)
sock_server = UDPServer('127.0.0.1', 8888)
obci.start_streaming(sock_server.handle_sample)
