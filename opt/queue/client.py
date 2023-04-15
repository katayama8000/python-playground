import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5557")

while True:
    msg = socket.recv()
    print("recv: " + msg.decode('utf-8'))