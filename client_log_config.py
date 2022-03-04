import logging
import os
from def_var import LOGGING_LEVEL
from logging.handlers import TimedRotatingFileHandler

PATH = os.path.dirname(__file__)
PATH = os.path.split(PATH)[0]
PATH = os.path.join(PATH, 'Client.log')

# Подготовка имени файла для логирования
log_Formatter = logging.Formatter('%(acstime)s %(levelname)s %(filename)s %(message)s')

# создаём потоки вывода логов
file_handler = TimedRotatingFileHandler(PATH, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_Formatter)

# создаём регистратор и настраиваем его
cl_LOGGER = logging.getLogger('Server')
cl_LOGGER.setLevel(LOGGING_LEVEL)
cl_LOGGER.addHandler(file_handler)

if __name__ == '__main__':
    cl_LOGGER.debug('Это дебаг')
    cl_LOGGER.info('Информационное сообщение')
    cl_LOGGER.error('Вышла ошибка')
    cl_LOGGER.critical('Ещё чуточку и будет экран смерти!')