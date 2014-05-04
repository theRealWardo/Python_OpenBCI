"""A sample client for the OpenBCI UDP server."""

import cPickle as pickle
import open_bci
import socket


class UDPClient(object):

  def __init__(self, ip, port):
    self.ip = ip
    self.port = port
    self.client = socket.socket(
        socket.AF_INET, # Internet
        socket.SOCK_DGRAM)
    self.client.bind((ip, port))

  def start_listening(self, callback=None):
    while True:
      data, addr = self.client.recvfrom(1024)
      sample = pickle.loads(data)
      print sample.channels


client = UDPClient('127.0.0.1', 8888)
client.start_listening()
