def my_func(name, age, city):
    return f'{name.capitalize()}, {age} год(а), проживает в городе {city.capitalize()}'

print(my_func(input('Введите имя - '), input('Введите возраст - '), input('введите город - ')))

