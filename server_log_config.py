"""Кофнфиг клиентского логгера"""

import os
import logging
from def_var import LOGGING_LEVEL
from logging.handlers import TimedRotatingFileHandler

# создаём формировщик логов (formatter):
log_Formatter = logging.Formatter('%(acstime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path(__file__))
PATH = os.path.split(PATH)[0]
PATH = os.path.join(PATH, 'Server.log')

# создаём потоки вывода логов
file_handler = logging.TimedRotatingFileHandler(
    PATH, encoding='utf-8', interval=1, when='midnight')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_Formatter)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('Server')
LOGGER.setLevel(LOGGING_LEVEL)
LOGGER.addHandler(file_handler)

if __name__ == '__main__':
    LOGGER.debug('Это дебаг')
    LOGGER.info('Информационное сообщение')
    LOGGER.error('Вышла ошибка')
    LOGGER.critical('Ещё чуточку и будет экран смерти!')