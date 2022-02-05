'''Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
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
'''


from socket import *
import argparse
import json
import re
import time

DEFAULT_PORT = 7777
DEFAULT_IP_ADDRESS = '127.0.0.1'
MAX_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'


def client_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', type=str, help='Address')
    parser.add_argument("port", nargs='?', type=int, default=DEFAULT_PORT, help='Server port')
    args = parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    if re.match(ip_re_tpl, args.address) is None:
        print('Wrong IP address')
        exit(1)
    if not 1024 <= args.port <= 65535:
        print('Please enter the port between 1024-65535')
        exit(1)
    return args.address, args.port


def main():
    # server = create_server()
    client_socket = socket(AF_INET, SOCK_STREAM)
    server_address, server_port = client_args()
    try:
        server_address.connect(server_address, server_port)
    except ConnectionError:
        print('Error')
        exit(1)

    client_message = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": "Nikos",
            "status": "Your enter!"
        }
    }

    data = json.dumps(client_message).encode(ENCODING)
    server_address.send(data)

    data = server_address.recv(MAX_PACKAGE_LENGTH)
    message = json.loads(data.decode(ENCODING))

    print(f'Server response code: {message:["response"]}')
    print(f'Server message: {message["alert"]}')

    server_address.close()


if __name__ == '__main__':
    main()
