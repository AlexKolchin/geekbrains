number = int(input('Введите число \n'))

try:
    result = 100 / number
except ZeroDivisionError as e:
    print('Попытка деления на 0')
    print('Информация об исключении', e)
except Exception as e:
    print('Неизвестная ошибка')
    print('Информация об исключении', e)