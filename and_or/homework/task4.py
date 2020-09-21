'''4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число. Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция. Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.'''
def func(user_number):
    if user_number == 13:
        raise ValueError('Value cant be 13')
    else:
        user_number = user_number ** 2
    return user_number
number = int(input('Enter number from 1 to 100\n'))
try:
    result = func(number)
except ValueError as e:
    print(e)
else:
    print(result)










