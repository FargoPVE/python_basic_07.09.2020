"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
user_number = int(input("Введите Ваше число: "))
max_number = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10
print("Наибольшее число", max_number)