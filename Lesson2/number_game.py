# компьютер загадывает случайное число от 1 до 100
import random
number = random.randint(1, 100)
# print(number)
i = 0
while True:
    user_number = int(input('Введите число от 1 до 100: '))
    if number == user_number:
        print('Вы угадали!')
        break
    elif number < user_number:
        print('Вы не угадали, попробуйте меньше:')
    elif number > user_number:
        print('Вы не угадали, попробуйте больше')
    else:
        print('Ошибка!')
    i += 1

