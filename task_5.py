"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
print('Задание 5 \n','-'*20)
import subprocess
import chardet

def site_ping(url):
    ping = subprocess.Popen(['ping', url], stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        print(f'site {url},', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

site_ping('yandex.ru')
site_ping('youtube.com')
