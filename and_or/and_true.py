import math

# Есть список чисел
numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# создать список из тех чисел которые имеют квадратный корень меньше 2 [1, 2, 3]
# обычный способ
result = []
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            result.append(number)
print(result)
# через ленивый and
result = []
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# через генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)
