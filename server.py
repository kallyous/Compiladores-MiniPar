import socket
import threading

def handle_client(client_socket):
    try:
        expression = client_socket.recv(1024).decode('utf-8')
        # print(f"Received expression: {expression}")
        try:
            result = eval(expression)
        except Exception as e:
            result = f"Error: {e}"
        client_socket.send(str(result).encode('utf-8'))
        # print(f"Sent result: {result}")
    finally:
        client_socket.close()

def start_server(host='0.0.0.0', port=50007):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[*] Listening on {host}:{port}")
        s.bind((host, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            # print(f"[*] Accepted connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(conn,))
            client_handler.start()


if __name__ == '__main__':
    start_server()