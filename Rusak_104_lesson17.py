# Домашнее задание

class HomeWork:

    def __init__(self):  # Инициализатор класса
        self.data_ = input('Введите строку или число: ')

    def method_1(self):
        vowel = 0  # Переменная для подсчета гласных букв
        consonant = 0  # Переменная для подсчета согласных букв
        sum_even = 0  # Переменная для подсчета четных цифр
        list_vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

        if self.data_.isalpha():  # Проверяем являются ли введенные символы строкой
            for i in self.data_:
                if i in list_vowel:
                    vowel += 1
                else:
                    consonant += 1
            if vowel * consonant <= len(self.data_):
                for i in self.data_:
                    if i in list_vowel:
                        print(i, end=' ')
            else:
                for i in self.data_:
                    if i not in list_vowel:
                        print(i, end=' ')
        elif self.data_.isdigit():  # Проверяем являются ли введенные символы числом
            for i in self.data_:
                if int(i) % 2 == 0:
                    sum_even += int(i)
            print(sum_even * len(self.data_))
        else:
            print('Вы ввели строку и число')

    def method_2(self):
        print(len(self.data_))


a = HomeWork()
a.method_1()
a.method_2()
