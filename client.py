import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5000))
print("Connected to server")

req = json.dumps({"method": "add", "params": [1, 2]})
req = json.dumps({"method": "floor", "params": [3.222]})
req = json.dumps({"method": "nroot", "params": [3, 8]})
req = json.dumps({"method": "reverse", "params": ["hello"]})
req = json.dumps({"method": "validAnagram", "params": ["hello", "ollhe"]})
# req = json.dumps({"method": "sort", "params": [["b", "c", "a", "z", "k"]]})
sock.send(req.encode("utf-8"))

data = sock.recv(1024)
res = json.loads(data.decode("utf-8"))
print(res['result'])
