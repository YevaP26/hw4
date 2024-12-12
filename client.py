import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('127.0.0.1', 6116)
client_socket.connect(server_address)

try:
    message = "Привіт, Сервер!"
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    if data:
        print(f"Отримано від сервера: {data.decode()}")
finally:
    print("Закриття клієнтського зʼєднання.")
    client_socket.close()
