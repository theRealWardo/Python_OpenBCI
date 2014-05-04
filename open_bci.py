"""Core OpenBCI objects for handling connections and samples from the board.
"""

import serial


class OpenBCIBoard(object):
  """Handle a connection to an OpenBCI board.

  Args:
    port: The port to connect to.
    baud: The baud of the serial connection.
  """

  def __init__(self, port, baud):
    self.ser = serial.Serial(port, baud)
    self.dump_registry_data()
    self.streaming = False

  def dump_registry_data(self):
    """Dump all the debug data until we get to a line with something
    about streaming data.
    """
    line = ''
    while 'begin streaming data' not in line:
      line = self.ser.readline()

  def start_streaming(self, callback):
    """Start handling streaming data from the board. Call a provided callback
    for every single sample that is processed.

    Args:
      callback: A callback function that will receive a single argument of the
          OpenBCISample object captured.
    """
    if not self.streaming:
      # Send an 'x' to the board to tell it to start streaming us text.
      self.ser.write('x')
      # Dump the first line that says "Arduino: Starting..."
      self.ser.readline()
    while True:
      data = self.ser.readline()
      sample = OpenBCISample(data)
      callback(sample)


class OpenBCISample(object):
  """Object encapulsating a single sample from the OpenBCI board."""

  def __init__(self, data):
    parts = data.rstrip().split(', ')
    self.id = parts[0]
    self.channels = []
    for c in xrange(1, len(parts) - 2):
      self.channels.append(int(parts[c]))
    # This is fucking bullshit but I have to strip the comma from the last
    # sample because the board is returning a comma... wat?
    self.channels.append(int(parts[len(parts) - 1][:-1])) 
