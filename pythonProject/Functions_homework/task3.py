player_name = input('Enter your name: ')

player = {
    "name": player_name,
    "health": 100,
    "damage": 23,
    "armor": 100
}
enemy_name = input('Enter your name: ')
enemy = {
    "name": enemy_name,
    "health": 100,
    "damage": 33,
    "armor": 100
}

def attack(attacker, target):
    target['health'] = target['health'] - attacker['damage']

print(attack(player,enemy))

print(enemy)

print(attack(enemy, player))
print(player)
