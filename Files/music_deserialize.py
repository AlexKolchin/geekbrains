import json, pickle

with open('group.json', 'r') as f:
    list = json.load(f)

print(list)
print(type(list))

with open('group.pickle', 'rb') as f:
    blist = pickle.load(f)
print(blist)
print(type(blist))