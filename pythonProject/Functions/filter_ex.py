# набор чисел
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
# получить только четные числа
def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
print(result)
result = list(result)
print(result)

# набор строк
names = ['Max', 'Leo', 'Kate']
# получить строки больше 3-х символов
# print(filter(names, ))
print(list(filter(lambda name: len(name) > 3, names)))