# Homework

import logging
from datetime import datetime


def debug(func): # Функция декоратор
    # Настройка базовой конфигурации логирования в текстовый файл
    logging.basicConfig(level=logging.INFO, filename="log.txt", filemode="a+", encoding='UTF-8')
    logging.info(f'Вызвана функция: {func.__name__} в {datetime.now()}')

    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print(f'Имя функции - {func.__name__}, в функцию передали аргументы -{*args, *kwargs}')
        print(f'Функция возвращает - {a}')

    return wrapper


@debug
def func_div(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        logging.error("ZeroDivisionError", exc_info=True)
        return 'Деление на 0!'


@debug
def func_mult(c, d):
    if c * d <= 10000:
        return c * d
    else:
        logging.info('Получилось слишком большое число!')
        return c * d


func_div(1, 0)
func_mult(500, 3000)
