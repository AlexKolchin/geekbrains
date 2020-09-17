import json
friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 456]},
    {'name': 'Leo', 'age': 33}
]
print(friends)
print(type(friends))
# преобразуем список в json
json_friends = json.dumps(friends)
print(json_friends)
print(type(json_friends))
# обратно из json в объект
friends = json.loads(json_friends)
print(friends)
print(type(friends))
