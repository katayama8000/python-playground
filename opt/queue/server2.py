import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5557")

id = 0
while True:
    id += 1
    socket.send(("sub2:" + str(id)).encode('utf-8'))
    print("send: " + str(id))
    time.sleep(1)