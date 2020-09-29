"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_list = input("Введите Ваши данные для списка через (запятую): ")
user_info = user_list.split(',')

id_list = 0
while id_list < len(user_info[:-1]):
    user_info[id_list], user_info[id_list + 1] = user_info[id_list + 1], user_info[id_list]
    id_list = id_list + 2
print(user_info)


