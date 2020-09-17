import json
friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 456]},
    {'name': 'Leo', 'age': 33}
]
with open('friends.json', 'w') as f:
    json_friends = json.dump(friends, f)

with open('friends.json', 'r') as f:
    friends = json.load(f)

print(friends)
print(tyoe(friends))