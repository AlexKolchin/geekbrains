name = input('Enter your name: ')
age = int(input('Enter your age: '))
weight = int(input('Enter your weight: '))

if age < 30 and  50 < weight < 120:
    print(f"{name}, {age} years, {weight} kilos - good health")
elif (age > 30 and age < 40) and (weight < 50 or weight > 120):
    print(name, end=',')
    print(age, 'years', end=',')
    print(weight, 'kilos', end='')
    print(' - you should go sports')
elif age > 40 and 50 > weight or weight > 120:
    print(name, end=',')
    print(age, 'years', end=',')
    print(weight, 'kilos', end='')
    print(' - you should visit a doctor')
else:
    print('not investigated')


