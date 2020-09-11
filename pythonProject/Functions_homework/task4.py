player_hp = 150
player_dps = 50
enemy_dps = 20
enemy_hp = 100
player_armor = 4
enemy_armor = 2
player_name = input('Enter your name: ')
enemy_name = 'Diablo'
player = {
    "name": player_name,
    "health": player_hp,
    "damage": player_dps,
    "armor": player_armor
}
enemy = {
    "name": enemy_name,
    "health": enemy_hp,
    "damage": enemy_dps,
    "armor": enemy_armor
}

def attack(attacker, target):

    def resist(attacker, target):
        return attacker["damage"] / target["armor"]

    target["health"] -= resist(attacker, target)

print(attack(player, enemy))
print(enemy)
print(attack(enemy, player))
print(player)


