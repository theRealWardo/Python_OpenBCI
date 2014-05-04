from ws4py.client.threadedclient import WebSocketClient

class DummyClient(WebSocketClient):

  def closed(self, code, reason=None):
    print "Closed down", code, reason

  def received_message(self, m):
    print m
    if len(m) == 175:
      self.close(reason='Bye bye')

if __name__ == '__main__':
  try:
    ws = DummyClient(
        'ws://localhost:8880/socket.io/1/websocket/k_HTzF4ybAnZE9DX_SYy',
        protocols=['http-only', 'chat'])
    ws.connect()
    ws.run_forever()
  except KeyboardInterrupt:
    ws.close()
