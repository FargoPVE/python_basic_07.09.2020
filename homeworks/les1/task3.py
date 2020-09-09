user_number = int(input("Введите Ваше число: "))
if user_number < 10:
    first_number = user_number * 10 + user_number
    second_number = user_number * 100 + first_number
elif user_number >= 10 and user_number < 100:
    first_number = user_number * 100 + user_number
    second_number = user_number * 1000 + first_number
elif user_number >= 100 and user_number < 1000:
    first_number = user_number * 1000 + user_number
    second_number = user_number * 10000 + first_number
else:
    print("Ваше число слишком большое, выберите другое")
sum_of_numbers = user_number + first_number + second_number
print("Новое число:", sum_of_numbers)
