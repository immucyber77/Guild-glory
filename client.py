import socket
import threading

class FF_CLIENT:
    def __init__(self, uid, password):
        self.uid = uid
        self.password = password
        self.sock = None

    def connect(self, token, ip, port, name, key, iv):
        print(f"[+] Connecting to {ip}:{port}")
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((ip, int(port)))
            self.sock.send(bytes.fromhex(token))
            print("[+] Token sent successfully")
        except Exception as e:
            print(f"[!] Error connecting or sending token: {e}")

    def start(self):
        if not self.sock:
            print("[!] Socket not connected.")
            return

        print("[+] Client started. Listening for server data...")

        def receive():
            try:
                while True:
                    data = self.sock.recv(4096)
                    if not data:
                        break
                    print(f"[Server] {data.hex()}")
            except Exception as e:
                print(f"[!] Receive error: {e}")

        thread = threading.Thread(target=receive)
        thread.daemon = True
        thread.start()