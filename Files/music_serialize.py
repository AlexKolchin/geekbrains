import json, pickle
my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'albums': [{'name': 'Делать панк-рок','year': 2016},{'name': 'Шапито','year': 2014}]
}
with open('group.json', 'w', encoding='utf-8') as f:
    json_my_favourite_group = json.dump(my_favourite_group, f)

with open('group.pickle', 'wb') as f:
    # сразу пишем объект целиком с помощью pickle
    pickle.dump(my_favourite_group, f)