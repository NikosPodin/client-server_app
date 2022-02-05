"""Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента:
сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""


import argparse
import json
import re
from socket import *
import time

DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '127.0.0.1'
MAX_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'


def client_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("-a", type=str, default=DEFAULT_IP_ADDRESS, help='Listening IP')
    args_parser.add_argument("-p", type=int, default=DEFAULT_PORT, help='port')
    args = args_parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    if args.a != '' and re.match(ip_re_tpl, args.a) is None:
        print('Wrong IP address')
        exit(1)
    if not 1024 <= args.p <= 65535:
        print('Please enter the port between 1024-65535')
        exit(1)
    return args.a, args.p


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    ip_address, port = client_args()
    try:
        server_socket.bind((ip_address, port))
    except OSError:
        print(f'Address {ip_address} or port {port} already in use')
        exit(1)
    server_socket.listen(5)
    print(f'Server started on port {port}')

    while True:
        client, address = server_socket.accept()
        print(f"Connection request received from {address}")

        data = client.recv(MAX_PACKAGE_LENGTH)
        client_message = json.loads(data.decode(ENCODING))
        print(f'Message received: {client_message}')

        server_message = ''
        if client_message['action'] == 'presence':
            server_message = {
                "response": 200,
                "time": time.time(),
                "alert": 'OK'
            }

        data = json.dumps(server_message).encode(ENCODING)
        client.send(data)

        client.close()


if __name__ == '__main__':
    main()
