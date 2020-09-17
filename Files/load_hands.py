# читаем объект из фай

# откроем фай
with open('person.dat', 'rb') as f:
    # теперь нам надо знать как мы записывали объект
    # прочитаем файл в список
    result = f.readlines()

# теперь воссоздаем исходный объект
person = {}
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телефоны
phones = []
for bphone  in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# получили исходный объектю Это было достаточно тяжело. А что если он немного изменится?
print(person)
