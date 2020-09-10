"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_seconds = int(input("Введите Ваше число в секундах: "))
sec = user_seconds % 100
minutes = user_seconds // 60
min_to_display = minutes % 100
hours = minutes // 60
hours_to_display = hours % 100
if sec < 10:
    null = "0"
else:
    null = ""
if min_to_display < 10:
    null_for_min = "0"
else:
    null_for_min = ""
if hours_to_display < 10:
    null_for_hours = "0"
else:
    null_for_hours = ""
print(str(null_for_hours) + str(hours_to_display), ":", str(null_for_min) + str(min_to_display), ':', str(null) + str(sec))