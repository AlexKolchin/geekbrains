# записать в список только положительные числа
numbers = [1, 3, 4, 6, -3, -3, -6, 6, 3432, -34]
new_number = []
# классический способ
for number in numbers:
    if number > 0:
        new_number.append(number)
print(new_number)
# через функцию filter
new_number = filter(lambda number: number < 0, numbers)
print(list(new_number))
# через генератор
new_number = [number for number in numbers if number > 0]
print((new_number))