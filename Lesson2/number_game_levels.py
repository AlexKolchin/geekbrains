# компьютер загадывает случайное число от 1 до 100
import random
number = random.randint(1, 100)
print('Вас приветствует игра - "Угадай число!"')
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности: 1 - 10 попыток, 2 - 5 попыток, 3 - 3 попытки: '))
max_count = levels[level]
while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли, исчерпав все попытки =(')
        break
    print(f'Попытка № {count}')
    user_number = int(input('Введите число от 1 до 100: '))
    if number < user_number:
        print('Вы не угадали, попробуйте меньше:')
    elif number > user_number:
        print('Вы не угадали, попробуйте больше')
else:
    print('Вы выиграли! =)')

