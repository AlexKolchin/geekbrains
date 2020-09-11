max = 100
min = 1
var = None

print('Сейчас компьютер угадает число которое вы загадали!!!"')
yes = int(input('Загадайте число и когда будете готовы нажмите "1" '))

while var != 3:
    number = (max + min) // 2
    print(f'Ваше число {number} ?')
    var = int(input('Выберите вариант: 1 - ваше число больше, 2 - ваше число меньше, 3 - ваше число равно: '))
    if var == 1:
        min = number + 1
    elif var == 2:
        max = number - 1
print(f'Вы загадали число {number} - компьютер победил')
