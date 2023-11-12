import socket
import json
from operations import Operations

class RCPServer:

    # インスタンス化する際に、ソケットをバインドして待機状態にする
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def start(self) -> None:
        try:
            while True:
                print("Waiting for request...")
                conn, client = self.server_socket.accept()
                print(f"Connected to client {client}")

                self.handle_request(conn)

                conn.close()

        except KeyboardInterrupt:
            print("\nServer stopped.")
            self.server_socket.close()

    def handle_request(self, conn: socket.socket):
        try:
            data = conn.recv(1024)
            req = json.loads(data.decode("utf-8"))

            method = req.get("method")
            params = req.get("params")
            client_id = req.get("id")

            # Operationsがmethodを持っているかどうか判定する
            # hasattr()は、第一引数にオブジェクトをとるが、Pythonではクラスもオブジェクトとして扱う
            if hasattr(Operations, method):
                result = getattr(Operations, method)(*params)
                result_type = str(type(result))
            else:
                result = f"Method '{method}' not found."

            res = json.dumps({
                    "result": result,
                    "result_type": result_type,
                    "id": client_id
                })
            conn.send(res.encode("utf-8"))

        except Exception as e:
            print(f"Error: {e}")
            raise


if __name__ == "__main__":
    server = RCPServer("localhost", 5000)
    server.start()
