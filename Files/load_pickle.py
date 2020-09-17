import pickle

with open('person.dat', 'rb') as f:
    # сразу читаем объект целиком с помощью pickle
    person = pickle.load(f)

print(person)