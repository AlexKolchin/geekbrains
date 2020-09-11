# компьютер загадывает случайное число от 1 до 100
import random
number = random.randint(1, 100)
# print(number)
print('Вас приветствует игра - "Угадай число!"')
user_number = None
user_count = int(input('Введите количество игроков: '))
users = []
k = 1
for i in range(user_count):
    user_name = input(f'Введите имя игрока {k}: ')
    users.append(user_name)
    k += 1
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности: 1 - 10 попыток, 2 - 5 попыток, 3 - 3 попытки: '))
max_count = levels[level]

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все игроки проиграли, исчерпав все попытки =(')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход игрока {user}: ')
        user_number = int(input('Введите число от 1 до 100: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Вы не угадали, попробуйте меньше:')
        else:
            print('Вы не угадали, попробуйте больше')
else:
    print(f'Поздравляем, {winner_name}! Вы выиграли! =)')

