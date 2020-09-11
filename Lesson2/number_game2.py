# компьютер загадывает случайное число от 1 до 100
import random
number = random.randint(1, 100)
# print(number)
user_number = None
while number != user_number:
    user_number = int(input('Введите число от 1 до 100: '))
    if number < user_number:
        print('Вы не угадали, попробуйте меньше:')
    elif number > user_number:
        print('Вы не угадали, попробуйте больше')
print('Вы угадали!')

