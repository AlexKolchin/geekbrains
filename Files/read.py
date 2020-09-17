# Открываем файл на запись - файла не существует
f = open('first.txt', 'r')

# print(f.read())

#for line in f:
#    print(line.replace('\n', ''))

print(f.readlines())