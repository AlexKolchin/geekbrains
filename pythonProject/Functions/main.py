counter = int(input('Enter how much numbers you want: '))
numbers = []
for i in range(counter):
    number = int(input(f'Enter {i+1} number: '))
    numbers.append(number)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
