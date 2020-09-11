digit = int(input('Enter some number: '))
number = 0
while digit > 10 or digit <= 0:
    print('Try again between 0 and 10')
    digit = int(input('Enter some number: '))
    number += 1
else:
    print(digit**2)

print('end')



