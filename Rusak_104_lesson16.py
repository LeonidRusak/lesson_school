# Калькулятор

def calc(num1, oper_, num2):
    def sum_():
        print(num1 + num2)

    def sub_():
        print(num1 - num2)

    def mult_():
        print(num1 * num2)

    def div_():
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print('Деление на 0!')
            calc(int(input('Введите число: ')), input('Введите знак операции '), int(input('Введите число ')))

    if oper_ == '+':
        sum_()
    elif oper_ == '-':
        sub_()
    elif oper_ == '*':
        mult_()
    else:
        div_()


calc(int(input('Введите число: ')), input('Введите знак операции '), int(input('Введите число ')))


# Домашнее задание

def div_num():  # Функция находящая частное 2х чисел введенных строкой, числа не должны отличаться больше 1го порядка
    str_ = input('Введите 2 числа через пробел: ')
    try:
        num_1 = int(str_[0: len(str_) // 2])
        num_2 = int(str_[len(str_) // 2:])
        print(f'Результат деления: {num_1 / num_2}')
    except ZeroDivisionError:
        print(f'Деление на 0, попробуйте еще раз')
        div_num()
    except ValueError:
        print('Вы ввели не числа')


div_num()
