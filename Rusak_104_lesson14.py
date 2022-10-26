# Задание 1

def sum_digit(file_):  # Функия возвращающая сумму цифр в файле
    sum_dig = 0  # Сумма цифр в файле
    list_ = []  # Пустой список в который запишется весь текст из файла, разделенный по пробелам
    for i in file_.readlines():
        list_ = i.split(' ')
    for i in list_:
        if i.isdigit():
            sum_dig += int(i)

    return sum_dig


f = open('ex1', 'r')
print(sum_digit(f))


# Задание 2

def sort_list(f_2):  # Функция возвращающая отсортированный список из чисел и строк из файла
    list_all = []  # Исходный список, в который запишутся все элементы из файла
    list_d = []  # Список только с числами из файла
    list_w = []  # Список только со строками из файла
    for i in f_2:
        list_all.append(i[:-1])  # i[:-1] неодходим для отсечки \n
    for i in list_all:
        if i.isdigit():
            list_d.append(int(i))
        else:
            list_w.append(i)
    list_d.sort()
    list_w = sorted(list_w, key=len)
    return list_d + list_w


file_2 = open('ex2', 'r')
print(sort_list(file_2))


# Задание 3

def input_user():  # Функция для записи текста в файл пользователем
    file_3 = open('ex3', 'w')  # Создается или перезаписывается новый файл
    while True:  # Цикл для записи строк в файл
        string_ = input('Введите строку: ')
        if string_ == '':  # Условие для прерывания цикла (пустая строка)
            break
        file_3.write(string_ + '\n')  # К введенной стоке добавляется \n для перехода на новую строку


input_user()


# Задание 4

def count_line(file_4):  # Функция подсчитывающая общее количество строк в файле и количество символов в каждой строке
    count_l = 0  # Количество строк в файле
    for i in file_4:
        count_l += 1
        print(f'В стороке {i[:-1]} содержится {len(i[:-1])} символов')  # Срез используем для подсчета символов без \n
    print(f'В файле {count_l} строк')


f_ = open('ex4', 'r')
count_line(f_)


# Домашнее задание

def write_in(arr_):  # Функция принимающая массив, сортирует и записывает строки и числа
    arr_word = []  # Список для слов из исходного массива
    arr_dig = []  # Список для цисел из исходного массива
    for i in arr_:  # Цикл для разделения мух и котлет (строк и чисел)
        if type(i) == int:
            arr_dig.append(i)
        else:
            arr_word.append(i)
    arr_dig.sort()  # Сортировка списка по возрастанию
    arr_word = sorted(arr_word, key=len)  # Сортировка списка по длине строк в списке
    file_hw = open('homework', 'w')
    for i in arr_word:
        file_hw.write(str(i) + '\n')
    for i in arr_dig:
        file_hw.write(str(i) + '\n')


array_ = [1, 22, 'qwer', 12, 'qwe', 'asdfaa', 15, 'ad']
write_in(array_)
