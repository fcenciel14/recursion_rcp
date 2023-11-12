import socket
import json
import math
from typing import List

def add(a, b):
    return a + b

def floor(x: float):
    return math.floor(x)

def nroot(n: int, x: int):
    return math.pow(x, 1 / n)

def reverse(s: str):
    s_reversed_list = list(reversed(s))
    s_reversed = ''.join(s_reversed_list)
    return s_reversed

def validAnagram(str1: str, str2: str):
    hashmap1 = generateHashmap(str1)
    hashmap2 = generateHashmap(str2)

    sorted_hashmap1 = sorted(hashmap1.items())
    sorted_hashmap2 = sorted(hashmap2.items())

    return sorted_hashmap1 == sorted_hashmap2

def generateHashmap(s: str):
    hashmap = {}

    for char in s:
        if char in hashmap:
            hashmap[char] = hashmap[char] + 1
        else:
            hashmap[char] = 1

    return hashmap

def sort(strArr: List[str]):
    return sorted(strArr)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5000))
sock.listen(1)

while True:
    print("Waiting for request...")
    conn, addr = sock.accept()
    print(f"Connected to client {addr}")

    data = conn.recv(1024)
    req = json.loads(data.decode("utf-8"))

    method = req.get("method")
    params = req.get("params")

    if method == "add":
        result = add(*params)
    elif method == "floor":
        result = floor(*params)
    elif method == "nroot":
        result = nroot(*params)
    elif method == "reverse":
        result = reverse(*params)
    elif method == "validAnagram":
        result = validAnagram(*params)
    elif method == "sort":
        result = sort(*params)

    # result = methods[method](*params)

    res = json.dumps({"result": result})
    conn.send(res.encode("utf-8"))
    conn.close()
