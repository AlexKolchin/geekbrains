# набор чисел
numbers = [1, 5, 3, 4, 5, 6, 7, 11]
# Сортировка по возрастанию
print(sorted(numbers))
# Сортировка по убыванию
print(sorted(numbers, reverse=True))
# набор строк
names = ['max', 'alex', 'stanislav']
# сортировка по алфавиту
print(sorted(names))
# города и численность населения
cities = [('Киев', 1000), ('Ровно', 200), ('Харьков', 500)]
# такая сортировка работает по алфавиту
print(sorted(cities))
# как отсортировать по численности населения

def by_count(city):
    return city[1]

print(sorted(cities, key=by_count))
print(sorted(cities, key=lambda city: city[1]))

