import socket
import threading
import base64
from ssl_utils import wrap_socket

CONTROL_PORT = 9090
DATA_PORT = 9091
HOST = '0.0.0.0'

# Simulating decryption (base64)
def simulate_decryption(enc_msg):
    return base64.b64decode(enc_msg).decode()

def handle_client(conn, addr):
    try:
        print(f"Connection attempt from {addr}")
        ssl_conn = wrap_socket(conn, is_server=True)
        
        data = ssl_conn.recv(1024)
        encrypted_data = data.decode()

        # Encrypted message
        print(f"[SERVER] Received encrypted: {encrypted_data}")

        # Decrypt and display
        try:
            decrypted_data = simulate_decryption(encrypted_data.encode())
            print(f"[SERVER] Decrypted: {decrypted_data}")
        except Exception as e:
            print(f"[SERVER] Error decrypting message: {e}")
            decrypted_data = "[Decryption failed]"

        ssl_conn.send(b"Message received securely.")
        ssl_conn.close()
    except Exception as e:
        print(f"[SERVER] Error accepting connection: {e}")

def start_server(port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, port))
    server_sock.listen(5)
    print(f"[{'CONTROL' if port == CONTROL_PORT else 'DATA'}] Listening on port {port}")
    while True:
        conn, addr = server_sock.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

threading.Thread(target=start_server, args=(CONTROL_PORT,), daemon=True).start()
threading.Thread(target=start_server, args=(DATA_PORT,), daemon=True).start()

# Keeping main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("[SERVER] Shutting down.")
