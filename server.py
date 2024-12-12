import socket

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Сервер запущено...")

    # Привʼязуємо сервер до адреси та порту
    server_address = ('', 6116)
    server_socket.bind(server_address)

    # Очікування зʼєднань
    server_socket.listen(5)
    print("Очікуємо зʼєднання...")

    client_socket, client_address = server_socket.accept()
    print("Клієнт підключився:", client_address)

    while True:
        data = client_socket.recv(1024)
        if data:
            print(f"Отримано: {data.decode()}")
            message = "Привіт, Клієнт!"
            client_socket.send(message.encode())
        else:
            break
finally:
    print("Завершення роботи сервера.")
    server_socket.close()
