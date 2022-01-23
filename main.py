"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:
.
Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
'''
import socket
obj_sock = socket.socket()
# bytes ->
obj_sock.sendto(var, ())
#close
клиент 1) 2)
'''
import yaml

data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
        'items_quantity': 4,
        'items_ptice': {'computer': '200€-1000₫',
                        'keyboard': '5₽-50₽',
                        'mouse': '4₩-7₩',
                        'printer': '100₴-300₴'},
        }

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True) # вот про allow_unicod не увидел в задании и десять минут рыл стековерфлоу

with open('file.yaml', encoding='utf-8') as f_n:
    new_f_n = yaml.safe_load(f_n)

if (new_f_n == data):
    print('Всё совпадает')
else: print('Ничего не совпадает млин!')

print(new_f_n)