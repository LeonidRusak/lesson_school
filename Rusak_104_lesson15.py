# Задача 1

import json


def buy_day():  # Функция записывающая в json файл название и стоимость покупок
    flag = ''
    buy_name = []  # Список с названием покупок
    buy_price = []  # Список со стоимостью покупок

    while flag != 'стоп':
        buy_name.append(input('Введите название покупки: '))
        buy_price.append(int(input('Введите стоимость покупки: ')))
        flag = input('Для окончиния работы введите "стоп", для продолжения - Enter: ')

    data_buy = {'название': buy_name, 'стоимость': buy_price}

    with open('buy.json', 'w', encoding='UTF-8') as file:
        json.dump(data_buy, file, ensure_ascii=False)
    file.close()


buy_day()


# Задача 2

def total_cost():  # Функция считающая общую стоимость покупок из предыдущей задачи
    with open('buy.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    file.close()
    cost = sum(data['стоимость'])
    print(f'Стоимость покупок составила {cost}')


total_cost()
