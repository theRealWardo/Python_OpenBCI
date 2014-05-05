Python and Node.js with OpenBCI
==============

![alt tag](https://raw.github.com/theRealWardo/Python_OpenBCI/master/architecture.png)

- **open_bci.py** manages the connection between the OpenBCI board and Python
- **udp_server.py** exposes the data over UDP
- **socket_server.js** a Node.js server that retransmits the data over a Web Socket
- **htdocs/index.html** a hack to display data using D3.js

Running the Server
--------------

- Plugin the board
- `python udp_server.py --json`
- Optionally use `python udp_client.py --json` to verify data is coming through
- Make sure you have socket.io (or run `npm install socket.io`)
- Run `node socket_server.js`
- Visit [http://localhost:8880](http://localhost:8880) to see your brain waves
- Optionally use `python socket_client.py` to view the Web Socket data coming back into Python (requires socketio-client)


Dependency List
--------------

Python UDP demos require:
- pyserial

Node sample requires:
- socket.io

Python Web Socket requires:
- socketio-client
