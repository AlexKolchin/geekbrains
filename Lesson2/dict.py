str = input('Enter string: ')
i = 1
while i < len(str):
    if ord(str[i - 1]) != ord(str[len(str)-i]):
        break
        print('This is not poli')
    i += 1

print('this is poli')
