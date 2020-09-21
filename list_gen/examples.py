import random
# Создать список из случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for number in range(10)]
print(numbers)
# Создать список квадратов чисел
numbers = [1, 2, 3, -4]
numbers = [number**2 for number in numbers]
print(numbers)

# Создать список имена на букву А
names = ['Руслан', 'Дмитрий', 'Алексей', 'Ян', 'Александр']
names = [name for name in names if name[0].lower() == 'а']
print(names)
