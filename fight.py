import random
import time
start = None


def create_player():
    player = {}
    player['name'] = input("What's your name?").capitalize()
    player['weapon'] = input("Choose your weapon: Sword, Battle Ax, Short Bow, Staff").capitalize()
    player['health'] = 13
    player['Max health'] = 13
    player['num_potions'] = 2
    player['attack_points'] = [6, 10]
    player['xp'] = 0
    player['armor_class'] = 13
    player['Loot Gold'] = 0
    player['supplies']
    return player


monsters = ['Goblin', 'Bugbear', 'Dragon', 'Orc', 'Fire Giant', 'Frost Giant']


def choose_monster():
        return random.choice(monsters)


def roll(x=None):
    if x:
        dice = x['dice_roll']       ##this is for the monster to roll
    else:
        dice = input('What is the dice type? ')
    num_rolls = int(dice[0])
    num_sides = int(dice[2:])
    for i in range(num_rolls):
        return random.randint(1, num_sides)
    print(random.randint(1, num_sides))



def loot(loot, p):
    item = random.choice(list(loot.keys()))
    if item in list(p['supplies'].keys()):
        p['supplies'][item] += loot[item]
        print(item, loot[item])
    else:
        p['supplies'][item] = loot[item]
        print(item, loot[item])


def use_potion(person):
    if person['num_potions'] > 0:  ##person is just a placeholder
        person['health'] += 5
        person['num_potions'] -= 1
        print('Your health is now', str(person['health']) + '!')
        print('You have', person['num_potions'], 'potion(s) remaining')
        return person
    else:
                print("You don't have any potions.")


def check_stats(player):
    stats_str = u'\U0001F409' + '  PLAYER STATS  ' + u'\U0001F409'
    border = '*' * (len(stats_str) + 3)
    print(border)
    print(stats_str)
    print(border)
    for x in player:
        print(str(x).capitalize(), ':', str(player[x]))


def fight(person, monster):
    while person['health'] != 0 or monster['health'] != 0:
        answer = input('What would you like to do? \n Fight\n Potion\n run\n').capitalize()
        if answer == 'Fight':
            roll1 = roll(person)
            if roll1 >= 8:
                print('You are successful, please roll for damage.')
                roll2 = roll()
                monster['health'] -= roll2
            else:
                print('You missed!!')
            mon_roll = roll()
            if mon_roll >= 6:
                mon_roll2 = roll()
                person['health'] -= mon_roll2
            fight(person, monster)
        elif answer == 'Potion':
            use_potion()
            fight(person, monster)
        elif answer == 'Run':
            roll3 = roll()
            if roll3 >= 8:
                print('You ran away successfully!')
            else:
                print('You failed and must now fight.')
            fight(person, monster)


def _time_help(x=None):
    if x = None:
        return time.time()
    return time.time() - x


def rest(player, x=start):
    answer = input('Do you want to rest? Yes/No').upper()
    if answer == 'YES':
        _random_attack()
        if player['health'] == player['max_health']:
            print('Can\'t get any healthier. Get off your butt you lazy so and so.')
        elif x:
            check = _time_help(x)
            if check > 900:
                player['health'] += 5
                health = min(player['health'], player['max_health'])
                player['health'] = health
                print('You rested and your health is now at', player['health'])
                return _time_help()
            else:
                print('Sorry, compadre, you need to wait another', str(round(15 - (time.time() - x) / 60, 2)),
                      'minutes before you can rest again.')
                return x
        else:
            player['health'] += 5
            health = min(player['health'], player['max_health'])
            player['health'] = health
            print('You rested and your health is now at', player['health'])
            return _time_help()
    elif answer == 'NO':
        print('Play on')
    else:
        print('I don\'t understand what you want. Try again.')
        rest(player)


def _random_attack(person):
    attacks = [1, 0, 0, 0, 0, 2, 0, 0, 0, 0]
    attack = random.choice(attacks)
    if attack == 1:
        print('You were attacked by a vicious wolf!')
        person['health'] -= 5
        print('You now have', person['health'], 'health points!')
    elif attack == 2:
        print('You just got robbed!')
    elif attack == 0:
        print('You rested with no harm done.')

