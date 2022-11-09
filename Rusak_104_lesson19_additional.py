def count_not_div_3(func):  # Декоратор возвращает в консоль количество значений не кратных 3 из обернутой функции

    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        print(f'Количество значений не кратных 3 из функции {func.__name__}: {len(new_list_([]))- len(f)}')
        """ 
        Функция new_list_ возвращает список, в обертке передаем пустой список, при вызове функции в нее будет
        передан список с теми же значениями что и в f
        """
        return f

    return wrapper


def new_list_(old_list: list, new_list=[]):  # Функция возвращающая список из элементов во вложенных списках
    for i in old_list:
        if isinstance(i, list):
            new_list_(i)
        else:
            new_list.append(i)
    return new_list


@count_not_div_3
def div_3(list_dig):
    list_div_3 = []
    list_dig = new_list_(list_dig)  # Вызовем функцию чтобы убрать вложенные списки если они есть
    for i in list_dig:
        if i % 3 == 0:
            list_div_3.append(i)
    return list_div_3


list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(div_3(list_))
