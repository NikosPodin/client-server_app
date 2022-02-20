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

from def_var import DEFAULT_PORT, ENCODING

# Функция для приема данных от сервера
def receive_data(_sock):
    try:
        data = _sock.recv(1024)  # Принять не более 1024 байтов данных
        data_decode = json.loads(data.decode('utf-8'))
        if data_decode['response'] in (100, 101, 102, 200, 201, 202):
            print('Код возврата:', data_decode['response'], data_decode['alert'])
    except json.decoder.JSONDecodeError:
        print('Сообщение сервера не распознано')

# Функция для соединения с сервером. Отправялет presence-сообщение
def get_socket(msg, host, port):
    try:
        _sock = socket(AF_INET, SOCK_STREAM)  # сокет TCP
        _sock.connect((host, port))

        send_data(msg, _sock)
        receive_data(_sock)
        _sock.close()

    except ConnectionRefusedError as err:
        print("Ошибка создания сокета: {}".format(err))

# Утилита кодирования и отправки сообщения принимает словарь и отправляет его
def send_data(msg, data):
    print(f'Отправка сообщения {msg}')
    data.send(msg)

def client_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=str, help='Address') #address
    parser.add_argument("-p", nargs='?', type=int, default=DEFAULT_PORT, help='Server port') #port
    args = parser.parse_args()
    ip_re_tpl = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    if re.match(ip_re_tpl, args.address) is None:
        print('Wrong IP address')
        exit(1)
    if not 1024 <= args.port <= 65535:
        print('Please enter the port between 1024-65535')
        exit(1)
    # return args.address, args.port
    return args


def main():
    # server = create_server()
    # client_socket = socket(AF_INET, SOCK_STREAM)
    # server_address, server_port = client_args()
    # try:
    #     client_socket.connect(client_args())
    # except ConnectionError:
    #     print('Error')
    #     exit(1)

    client_message = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": "Nikos",
            "status": "Your enter!"
        }
    }

    args = client_args()
    host = args.addr
    port = args.port

    data = json.dumps(client_message).encode(ENCODING)
    # server_address.send(data)
    get_socket(data, host, port)

    # data = server_address.recv(MAX_PACKAGE_LENGTH)
    # message = json.loads(data.decode(ENCODING))
    #
    # print(f'Server response code: {message:["response"]}')
    # print(f'Server message: {message["alert"]}')
    #
    # server_address.close()


if __name__ == '__main__':
    main()
