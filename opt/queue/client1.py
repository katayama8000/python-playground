import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5557")

while True:
    msg = socket.recv()
    print("recv: " + msg.decode('utf-8'))

# Pull/Push
# Pull/Pushは、Push側からPull側にデータを送信する
# 送信側は、Push側、受信側はPull側と呼ぶ

# Pub/Sub
# Pub/Subは、Pub側からSub側にデータを送信する
# 送信側は、Pub側、受信側はSub側と呼ぶ

# Pull/PushとPub/Subの違い
# Pull/Pushは、1対1の通信
# Pub/Subは、1対多の通信

