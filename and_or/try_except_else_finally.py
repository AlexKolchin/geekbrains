number = int(input('Введите число \n'))

try:
    # код который может вызвать исключительную ситуацию
    result = 100 / number
except:
    # что делать если воникла исключительная ситуация
    print('Попытка деления на 0')
else:
    # что делать если ошибок не было
    print('Все хорошо ошибок не было')
finally:
    # выполняется всегда
    print('Что делаем когда ошибка есть и когда ее нет')