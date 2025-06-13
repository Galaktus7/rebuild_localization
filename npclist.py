from gametexts import gethitchance
import random
import traceback
import time

import telebot
import os
token = os.environ['token']

bot = telebot.TeleBot('7761726947:AAGOpSlfreC-GPanhCb89Vs5hS4vafxV0RQ')

testbot = telebot.TeleBot('1619953738:AAEu-D9-8K-GoJPrp2y3S3kWCqJq8BEt4fA')

def npcact_fullneural(game, player):
    for ids in game['players']:
        if game['players'][ids]['id'] != player['id']:
            target = game['players'][ids]
            break
    demon = player['fullneuraldemonobject']
    game_state = ""
    if 'adrenaline' in player['inventory']:
        is_adrenaline = "1"
    else:
        is_adrenaline = "0"
    if 'flash' in player['inventory']:
        is_flash = "1"
    else:
        is_flash = "0"
    if player['shieldgencd'] > 0:
        is_shield = "0"
    else:
        is_shield = "1"
    if player['perekatcd'] > 0:
        is_perekat = "0"
    else:
        is_perekat = "1"
    if player['vorcd'] > 0:
        is_vor = "0"
    else:
        is_vor = "1"


    if 'adrenaline' in target['inventory']:
        is_target_adrenaline = "1"
    else:
        is_target_adrenaline = "0"
    if 'flash' in target['inventory']:
        is_target_flash = "1"
    else:
        is_target_flash = "0"
    if target['shieldgencd'] > 0:
        is_target_shield = "0"
    else:
        is_target_shield = "1"
    if target['perekatcd'] > 0:
        is_target_perekat = "0"
    else:
        is_target_perekat = "1"
    if target['vorcd'] > 0:
        is_target_vor = "0"
    else:
        is_target_vor = "1"

    #print(demon['pattern'])
    game_state += str(player['energy'])+str(player['hp'])+is_adrenaline+is_flash+is_shield+is_perekat+is_vor+str(target['energy'])+str(target['hp'])+is_target_adrenaline+is_target_flash+is_target_shield+is_target_perekat+is_target_vor
    act = demon['pattern'][game_state]

    if act == 'attack':
        player['act'] = ['attack', target['id']]

    if act == 'adrenaline':
        if 'adrenaline' in player['inventory']:
            player['act'] = ['attack', target['id']]
            player['dopuseditems'].append(['adrenaline', player['id']])
        else:
            player['act'] = ['cant_do_adrenaline', 'self']

    if act == 'reload':
        player['act'] = ['reload', 'self']

    if act == 'perekat':
        if player['perekatcd'] <= 0:
            player['act'] = ['perekat', 'self']
        else:
            player['act'] = ['cant_do_perekat', 'self']

    if act == 'shield':
        if player['shieldgencd'] <= 0:
            player['act'] = ['shieldgen', player['id']]
        else:
            player['act'] = ['cant_do_shieldgen', 'self']

    if act == 'vor':
        if player['vorcd'] <= 0:
            player['act'] = ['vor', target['id']]
        else:
            player['act'] = ['cant_do_vor', 'self']

    if act == 'flash':
        if 'flash' in player['inventory']:
            player['act'] = ['flash', target['id']]
        else:
            player['act'] = ['cant_do_flash', 'self']


def random_duelrat_weights():
    weights = {
        'attack':random.randint(1, 100),
        'adrenaline': random.randint(1, 100),
        'flash': random.randint(1, 100),
        'perekat': random.randint(1, 100),
        'shield': random.randint(1, 100),
        'vor': random.randint(1, 100),
        'reload':random.randint(1, 100)

    }
    return weights

def select_most_value_demon(demons):
    maxscore = -9999
    most_value_demons = []
    #print(demons)
    for ids in demons:
        if demons[ids]['score'] >= maxscore:
            maxscore = demons[ids]['score']
    for ids in demons:
        if demons[ids]['score'] == maxscore:
            most_value_demons.append(demons[ids])
    demon = random.choice(most_value_demons)
    return demon


def get_act_weights(player, target):
    my_damage = 0
    target_damage = 0
    ien = player['energy']
    een = target['energy']
    while ien > 0:
        ien -= 2
        my_damage += 1
    while een > 0:
        een -= 2
        target_damage += 1

    my_damage_with_adrenaline = 0
    ien = player['energy'] + 3
    while ien > 0:
        ien -= 2
        my_damage_with_adrenaline += 1
    if 'adrenaline' not in player['inventory']:
        my_damage_with_adrenaline = my_damage

    target_damage_with_adrenaline = 0
    een = target['energy'] + 3
    while een > 0:
        een -= 2
        target_damage_with_adrenaline += 1
    if 'adrenaline' not in target['inventory']:
        target_damage_with_adrenaline = target_damage


    player_attack_rat_perekat = 0
    if target['energy'] >= 5:
        player_attack_rat_perekat = -2
    else:
        player_attack_rat_perekat = 1

    player_adrenaline_rat_perekat = 0
    if target['energy'] + 3 >= 5:
        player_adrenaline_rat_perekat = -2
    else:
        player_adrenaline_rat_perekat = 1

    player_perekat_rat_attack = 0
    if player['energy'] >= 5:
        player_perekat_rat_attack = 2
    else:
        player_perekat_rat_attack = -1

    player_perekat_rat_adrenaline = 0
    if player['energy'] + 3 >= 5:
        player_perekat_rat_adrenaline = 2
    else:
        player_perekat_rat_adrenaline = -1

    player_adrenaline_rat_adrenaline = 0
    if target_damage_with_adrenaline == my_damage_with_adrenaline:
        if target['hp'] < player['hp']:
            player_adrenaline_rat_adrenaline = 2
        elif target['hp'] > player['hp']:
            player_adrenaline_rat_adrenaline = -2
        elif target['hp'] == player['hp']:
            player_adrenaline_rat_adrenaline = 0
    elif target_damage_with_adrenaline < my_damage_with_adrenaline:
        player_adrenaline_rat_adrenaline = 2
    elif target_damage_with_adrenaline > my_damage_with_adrenaline:
        player_adrenaline_rat_adrenaline = -2

    if target['hp'] < player['hp']:
        both_attack_value = 2
    elif target['hp'] > player['hp']:
        both_attack_value = -2
    elif target['hp'] == player['hp']:
        both_attack_value = 0
    same_damage = {
        'player_flash': {'rat_flash': 0, 'rat_attack': -1, 'rat_shield': -1, 'rat_vor': 1, 'rat_reload': 1,
                         'rat_adrenaline': -1, 'rat_perekat': -1},
        'player_attack': {'rat_flash': 1, 'rat_attack': both_attack_value, 'rat_shield': 1, 'rat_vor': -2,
                          'rat_reload': -2, 'rat_adrenaline': 2, 'rat_perekat': player_attack_rat_perekat},
        'player_shield': {'rat_flash': 1, 'rat_attack': -1, 'rat_shield': 0, 'rat_vor': 0, 'rat_reload': 1,
                          'rat_adrenaline': -1, 'rat_perekat': 0},
        'player_vor': {'rat_flash': -1, 'rat_attack': 2, 'rat_shield': 0, 'rat_vor': 0, 'rat_reload': 1,
                       'rat_adrenaline': 2, 'rat_perekat': 0},
        'player_reload': {'rat_flash': -1, 'rat_attack': 2, 'rat_shield': -1, 'rat_vor': -1, 'rat_reload': 0,
                          'rat_adrenaline': 2, 'rat_perekat': -1},
        'player_adrenaline': {'rat_flash': 1, 'rat_attack': -2, 'rat_shield': 1, 'rat_vor': -2, 'rat_reload': -2,
                              'rat_adrenaline': player_adrenaline_rat_adrenaline,
                              'rat_perekat': player_adrenaline_rat_perekat},
        'player_perekat': {'rat_flash': 1, 'rat_attack': player_perekat_rat_attack, 'rat_shield': 0, 'rat_vor': 0,
                           'rat_reload': 1, 'rat_adrenaline': player_perekat_rat_adrenaline, 'rat_perekat': 0}
    }

    player_adrenaline_rat_attack = 0
    if target_damage_with_adrenaline == my_damage:
        if target['hp'] < player['hp']:
            player_adrenaline_rat_attack = 2
        elif target['hp'] > player['hp']:
            player_adrenaline_rat_attack = -2
        elif target['hp'] == player['hp']:
            player_adrenaline_rat_attack = 0
    elif target_damage_with_adrenaline < my_damage:
        player_adrenaline_rat_attack = 2
    elif target_damage_with_adrenaline > my_damage:
        player_adrenaline_rat_attack = -2

    rat_more_damage = {
        'player_flash': {'rat_flash': 0, 'rat_attack': -1, 'rat_shield': -1, 'rat_vor': 1, 'rat_reload': 1,
                         'rat_adrenaline': -1, 'rat_perekat': -1},
        'player_attack': {'rat_flash': 1, 'rat_attack': 2, 'rat_shield': 1, 'rat_vor': -2, 'rat_reload': -2,
                          'rat_adrenaline': 2, 'rat_perekat': player_attack_rat_perekat},
        'player_shield': {'rat_flash': 1, 'rat_attack': -1, 'rat_shield': 0, 'rat_vor': 0, 'rat_reload': 1,
                          'rat_adrenaline': -1, 'rat_perekat': 0},
        'player_vor': {'rat_flash': -1, 'rat_attack': 2, 'rat_shield': 0, 'rat_vor': 0, 'rat_reload': 1,
                       'rat_adrenaline': 2, 'rat_perekat': 0},
        'player_reload': {'rat_flash': -1, 'rat_attack': 2, 'rat_shield': -1, 'rat_vor': -1, 'rat_reload': 0,
                          'rat_adrenaline': 2, 'rat_perekat': -1},
        'player_adrenaline': {'rat_flash': 1, 'rat_attack': player_adrenaline_rat_attack, 'rat_shield': 0,
                              'rat_vor': -2, 'rat_reload': -2, 'rat_adrenaline': 2,
                              'rat_perekat': player_adrenaline_rat_perekat},
        'player_perekat': {'rat_flash': 1, 'rat_attack': player_perekat_rat_attack, 'rat_shield': 0, 'rat_vor': 0,
                           'rat_reload': 1, 'rat_adrenaline': player_perekat_rat_adrenaline, 'rat_perekat': 0}

    }

    player_attack_rat_adrenaline = 0
    if target_damage == my_damage_with_adrenaline:
        if target['hp'] < player['hp']:
            player_attack_rat_adrenaline = 2
        elif target['hp'] > player['hp']:
            player_attack_rat_adrenaline = -2
        elif target['hp'] == player['hp']:
            player_attack_rat_adrenaline = 0
    elif target_damage < my_damage_with_adrenaline:
        player_attack_rat_adrenaline = 2
    elif target_damage > my_damage_with_adrenaline:
        player_attack_rat_adrenaline = -2

    rat_less_damage = {
        'player_flash': {'rat_flash': 0, 'rat_attack': -1, 'rat_shield': -1, 'rat_vor': 1, 'rat_reload': 1,
                         'rat_adrenaline': -1, 'rat_perekat': -1},
        'player_attack': {'rat_flash': 1, 'rat_attack': -2, 'rat_shield': 1, 'rat_vor': -2, 'rat_reload': -2,
                          'rat_adrenaline': player_attack_rat_adrenaline, 'rat_perekat': player_attack_rat_perekat},
        'player_shield': {'rat_flash': 1, 'rat_attack': -1, 'rat_shield': 0, 'rat_vor': 0, 'rat_reload': 1,
                          'rat_adrenaline': -1, 'rat_perekat': 0},
        'player_vor': {'rat_flash': -1, 'rat_attack': 2, 'rat_shield': 0, 'rat_vor': 0, 'rat_reload': 1,
                       'rat_adrenaline': 2, 'rat_perekat': 0},
        'player_reload': {'rat_flash': -1, 'rat_attack': 2, 'rat_shield': -1, 'rat_vor': -1, 'rat_reload': 0,
                          'rat_adrenaline': 2, 'rat_perekat': -1},
        'player_adrenaline': {'rat_flash': 1, 'rat_attack': -2, 'rat_shield': 0, 'rat_vor': -2, 'rat_reload': -2,
                              'rat_adrenaline': -2, 'rat_perekat': player_adrenaline_rat_perekat},
        'player_perekat': {'rat_flash': 1, 'rat_attack': player_perekat_rat_attack, 'rat_shield': 0, 'rat_vor': 0,
                           'rat_reload': 1, 'rat_adrenaline': player_perekat_rat_adrenaline, 'rat_perekat': 0}

    }

    if my_damage == target_damage:
        table = same_damage
    elif my_damage > target_damage:
        table = rat_more_damage
    elif my_damage < target_damage:
        table = rat_less_damage

    return table


class NPC(object):
    def __init__(self, npcid = 0, npcname = 'None'):
        self.id = npcid
        self.first_name = npcname

def npcact_duel(game, player):
    target = None
    for ids in game['players']:
        if game['players'][ids]['controller'] != 'bot':
            target = game['players'][ids]
            break
    if target == None:
        return
    my_damage = 0
    target_damage = 0
    ien = player['energy']
    een = target['energy']
    while ien > 0:
        ien -= 2
        my_damage += 1
    while een > 0:
        een -= 2
        target_damage += 1

    my_damage_with_adrenaline = 0
    ien = player['energy']+3
    while ien > 0:
        ien -= 2
        my_damage_with_adrenaline += 1
    if 'adrenaline' not in player['inventory']:
        my_damage_with_adrenaline = my_damage

    target_damage_with_adrenaline = 0
    een = target['energy'] + 3
    while een > 0:
        een -= 2
        target_damage_with_adrenaline += 1
    if 'adrenaline' not in target['inventory']:
        target_damage_with_adrenaline = target_damage


    target_potential_acts = ['flash', 'attack', 'shield', 'vor', 'reload', 'adrenaline', 'perekat']
    player_potential_acts = ['flash', 'attack', 'shield', 'vor', 'reload', 'adrenaline', 'perekat']
    if target['energy'] <= 0:
        target_potential_acts.remove('attack')
    if 'flash' not in target['inventory']:
        target_potential_acts.remove('flash')
    if 'adrenaline' not in target['inventory']:
        target_potential_acts.remove('adrenaline')
    if target['shieldgencd'] > 0:
        target_potential_acts.remove('shield')
    if target['vorcd'] > 0:
        target_potential_acts.remove('vor')
    if target['perekatcd'] > 0:
        target_potential_acts.remove('perekat')
    if len(player['inventory']) == 0:
        try:
            target_potential_acts.remove('vor')
        except:
            pass
    if player['energy'] >= 5:
        try:
            target_potential_acts.remove('perekat')
        except:
            pass
    if player['energy'] == 0:
        try:
            target_potential_acts.remove('flash')
        except:
            pass
    if target_damage - my_damage >= 2:
        try:
            target_potential_acts.remove('flash')
        except:
            pass
    if my_damage_with_adrenaline < target_damage:
        try:
            target_potential_acts.remove('flash')
        except:
            pass
        try:
            player_potential_acts.remove('adrenaline')
        except:
            pass
        try:
            target_potential_acts.remove('shield')
        except:
            pass
        try:
            target_potential_acts.remove('perekat')
        except:
            pass
    if target_damage > my_damage:
        try:
            target_potential_acts.remove('perekat')
        except:
            pass
    if player['energy'] < target['energy']:
        if target['hp'] > 1:
            try:
                target_potential_acts.remove('flash')
            except:
                pass
    if my_damage_with_adrenaline == target_damage:
        if target['hp'] > player['hp']:
            try:
                target_potential_acts.remove('flash')
            except:
                pass
            try:
                target_potential_acts.remove('shield')
            except:
                pass
            try:
                target_potential_acts.remove('perekat')
            except:
                pass
    if 'adrenaline' not in player['inventory'] and 'flash' in player['inventory'] and target['energy'] < player['energy']:
        try:
            target_potential_acts.remove('vor')
        except:
            pass
    if 'adrenaline' not in player_potential_acts and 'flash' not in player_potential_acts:
        try:
            target_potential_acts.remove('vor')
        except:
            pass
    if target_damage < my_damage and 'flash' not in player_potential_acts:
        try:
            target_potential_acts.remove('vor')
        except:
            pass
    if target['hp'] == 1 and 'flash' not in player_potential_acts and player['energy'] > 0:
        try:
            target_potential_acts.remove('vor')
        except:
            pass


    if player['energy'] <= 0:
        player_potential_acts.remove('attack')
    if 'flash' not in player['inventory']:
        player_potential_acts.remove('flash')
    if 'adrenaline' not in player['inventory']:
        try:
            player_potential_acts.remove('adrenaline')
        except:
            pass
    if player['shieldgencd'] > 0:
        if 'shield' in player_potential_acts:
            player_potential_acts.remove('shield')
    if player['vorcd'] > 0:
        if 'vor' in player_potential_acts:
            player_potential_acts.remove('vor')
    if player['perekatcd'] > 0:
        if 'perekat' in player_potential_acts:
            player_potential_acts.remove('perekat')
    if len(target['inventory']) <= 0:
        try:
            player_potential_acts.remove('vor')
        except:
            pass
    if target['energy'] >= 5:
        try:
            player_potential_acts.remove('perekat')
        except:
            pass
    if target['energy'] == 0:
        try:
            player_potential_acts.remove('flash')
        except:
            pass
    if my_damage - target_damage >= 2:
        try:
            player_potential_acts.remove('flash')
        except:
            pass
    if target_damage_with_adrenaline < my_damage:
        try:
            player_potential_acts.remove('flash')
        except:
            pass
        try:
            target_potential_acts.remove('adrenaline')
        except:
            pass
        try:
            player_potential_acts.remove('shield')
        except:
            pass
        try:
            player_potential_acts.remove('perekat')
        except:
            pass
    if target['energy'] < player['energy']:
        if player['hp'] > 1:
            try:
                player_potential_acts.remove('flash')
            except:
                pass
    if target_damage_with_adrenaline == my_damage:
        if player['hp'] > target['hp']:
            try:
                player_potential_acts.remove('flash')
            except:
                pass
            try:
                player_potential_acts.remove('shield')
            except:
                pass
            try:
                player_potential_acts.remove('perekat')
            except:
                pass
    if my_damage > target_damage:
        try:
            player_potential_acts.remove('perekat')
        except:
            pass

    if 'adrenaline' not in target['inventory'] and 'flash' in target['inventory'] and player['energy'] < target['energy']:
        try:
            player_potential_acts.remove('vor')
        except:
            pass
    if 'adrenaline' not in target_potential_acts and 'flash' not in target_potential_acts:
        try:
            player_potential_acts.remove('vor')
        except:
            pass
    if my_damage < target_damage and 'flash' not in target_potential_acts:
        try:
            player_potential_acts.remove('vor')
        except:
            pass

    if player['hp'] == 1 and 'flash' not in target_potential_acts and target['energy'] > 0:
        try:
            player_potential_acts.remove('vor')
        except:
            pass

    player['target_potential_acts'] = target_potential_acts

    table = get_act_weights(player, target)

    delkeys = []
    for ids in table:
        if ids.replace('player_', '') not in target_potential_acts:
            delkeys.append(ids)
    for ids in delkeys:
        del table[ids]

    for ids in table:
        delkeys = []
        for idss in table[ids]:
            if idss.replace('rat_', '') not in player_potential_acts:
                delkeys.append(idss)
        for idss in delkeys:
            del table[ids][idss]


    #print(table)
    reversed_table = {}
    for ids in player_potential_acts:
        reversed_table.update({'rat_'+ids:{}})
    for ids in reversed_table:
        for idss in table:
            if idss not in reversed_table[ids]:
                reversed_table[ids].update({idss:table[idss][ids]})
    #print(reversed_table)

    most_value_act = 'reload'
    acts_value = {}
    for ids in reversed_table:
        max_value = -3
        for idss in reversed_table[ids]:
            if reversed_table[ids][idss] > max_value:
                max_value = reversed_table[ids][idss]
        min_value = 3
        for idss in reversed_table[ids]:
            if reversed_table[ids][idss] < min_value:
                min_value = reversed_table[ids][idss]
        acts_value.update({ids:{'max_value':max_value, 'min_value':min_value}})

    #print(acts_value)

    maxvalueselect = False
    choicen_acts = []
    for ids in acts_value:
        if acts_value[ids]['min_value'] >= 2:
            choicen_acts.append(ids)
    if len(choicen_acts) == 0:
        for ids in acts_value:
            if acts_value[ids]['min_value'] >= 1:
                choicen_acts.append(ids)


    #if len(choicen_acts) == 0:
    #    for ids in acts_value:
    #        if acts_value[ids]['min_value'] >= 0:
    #            choicen_acts.append(ids)

    #if len(choicen_acts) == 0:
    #    for ids in acts_value:
    #        if acts_value[ids]['max_value'] >= 1:
    #            choicen_acts.append(ids)


    if len(choicen_acts) == 0:
        for ids in acts_value:
            if acts_value[ids]['max_value'] >= 0:
                choicen_acts.append(ids)


    if player['hp'] == 1:
        if len(choicen_acts) == 0:
            for ids in acts_value:
                if acts_value[ids]['max_value'] >= -1:
                    choicen_acts.append(ids)

    #if len(choicen_acts) == 0:
    #    for ids in acts_value:
    #        if acts_value[ids]['max_value'] >= 1:
    #            choicen_acts.append(ids)

    #if len(choicen_acts) == 0:
    #    for ids in acts_value:
    #        if acts_value[ids]['max_value'] >= 0:
    #            choicen_acts.append(ids)

    #if len(choicen_acts) == 0:
    #    for ids in acts_value:
    #        if acts_value[ids]['max_value'] >= -1:
    #            choicen_acts.append(ids)

    if len(choicen_acts) == 0:
        for ids in acts_value:
            choicen_acts.append(ids)


    #print("turn "+str(game['turn'])+':')
    if 'rat_adrenaline' in choicen_acts:
        if 'rat_attack' in choicen_acts:
            if my_damage > target_damage_with_adrenaline:
                choicen_acts.remove('rat_adrenaline')
            if my_damage == target_damage_with_adrenaline and player['hp'] > target['hp']:
                try:
                    choicen_acts.remove('rat_adrenaline')
                except:
                    pass
            #if not maxvalueselect:
            #    if acts_value['rat_adrenaline']['min_value'] == acts_value['rat_attack']['min_value']:
            #        choicen_acts.remove('rat_adrenaline')
            #else:
            #    pass

    categories = {
        'attack':'attack',
        'adrenaline':'attack',
        'reload':'advantage',
        'perekat':'def',
        'shield':'def',
        'vor':'advantage',
        'flash':'def'
    }

    if 'rat_flash' in choicen_acts and 'rat_perekat' in choicen_acts:
        choicen_acts.remove('rat_flash')
    if 'rat_flash' in choicen_acts and 'rat_shield' in choicen_acts:
        choicen_acts.remove('rat_flash')

    #print(choicen_acts)

    current_categories = {}
    for ids in choicen_acts:
        cname = ids.replace('rat_', '')
        if categories[cname] not in current_categories:
            current_categories.update({categories[cname]:[cname]})
        else:
            current_categories[categories[cname]].append(cname)

    #print(current_categories)
    categ = random.choice(list(current_categories))
    #currentact = random.choice(current_categories[categ])

    player['my_potential_acts'] = choicen_acts

    choicenact_weights = []
    choicen_demon = select_most_value_demon(player['rat_demons'])
    player['choicen_demon'] = choicen_demon['number']
    #print(choicen_demon)
    for ids in choicen_acts:
        choicenact_weights.append(choicen_demon['pattern'][ids.replace('rat_', '')])
    currentact = random.choices(choicen_acts, weights=choicenact_weights)[0]
    currentact = currentact.replace('rat_', '')

    if currentact == 'attack':
        player['act'] = ['attack', target['id']]

    if currentact == 'adrenaline':
        player['act'] = ['attack', target['id']]
        player['dopuseditems'].append(['adrenaline', player['id']])

    if currentact == 'reload':
        player['act'] = ['reload', 'self']

    if currentact == 'perekat':
        player['act'] = ['perekat', 'self']

    if currentact == 'shield':
        player['act'] = ['shieldgen', player['id']]

    if currentact == 'vor':
        player['act'] = ['vor', target['id']]

    if currentact == 'flash':
        player['act'] = ['flash', target['id']]



        
def npcact_necromant(game, player):
    try:
        if game['turn'] == 1:
            player['act'] = ['summon_mad_skeletons', 'self']
        else:
            has_skeletons = False
            for ids in game['players']:
                target = game['players'][ids]
                if 'Огромный злобный скелет' in target['name'] and target['controller'] == 'bot' and not target['dead']:
                    has_skeletons = True
                    break
            if has_skeletons:
                player['act'] = ['drink_tea', 'self']
            else:
                if player['summoned_mad_skeletons']:
                    if player['hp'] == 3:
                        if not player['summoned_weak_skeletons']:
                            player['act'] = ['summon_weak_skeletons', 'self']
                        else:
                            player['act'] = ['wait_in_magic_barrier', 'self']
                    elif player['hp'] == 2:
                        if not player['summoned_weak_ghouls']:
                            player['act'] = ['summon_weak_ghouls', 'self']
                        else:
                            player['act'] = ['wait_in_magic_barrier', 'self']
                    elif player['hp'] == 1:
                        if not player['summoned_zombie_rats']:
                            player['act'] = ['summon_zombie_rats', 'self']
                        else:
                            all_rats_dead = True
                            for ids in game['players']:
                                target = game['players'][ids]
                                if 'Зомби-крыса' in target['name'] and target['controller'] == 'bot' and not target['dead']:
                                    all_rats_dead = False
                                    break
                            if all_rats_dead:
                                player['act'] = ['wait_for_death', 'self']
                            else:
                                player['act'] = ['wait_in_magic_barrier', 'self']
                else:
                    print('????')
        if player['act'] == None:
            player['act'] = ['wait_in_magic_barrier', 'self']
        if game['turn'] >= 150:
            player['act'] = ['lighting_to_heroes', 'self']
    except:
        #print(traceback.format_exc())
        player['act'] = ['wait_in_magic_barrier', 'self']
        bot.send_message(441399484, traceback.format_exc())

def npcact_darkness(game, player):
    try:
        enemys_i_can_attack = []
        for ids in game['players']:
            target = game['players'][ids]
            if target['team'] != player['team'] and not target['dead'] and target['team'] != 'dark':
                enemys_i_can_attack.append(target['id'])
        if not player['dark_true_form']:
            player['act'] = ['run_to_player', 'self']
        else:
            if player['dark_die_stage'] > 0:
                player['act'] = ['dark_die', 'self']
            else:
                if player['prepared_beam'] == None:
                    d_acts = ['blue_beam_prepare', 'red_beam_prepare', 'violet_beam_prepare']
                    target = random.choice(enemys_i_can_attack)
                    if len(player['last_dark_acts']) == len(d_acts):
                        player['act'] = ['big_dark_wave', target]
                    else:
                        d_act = random.choice(d_acts)
                        while d_act in player['last_dark_acts']:
                            d_act = random.choice(d_acts)
                        player['act'] = [d_act, target]
                        if len(player['last_dark_acts']) == 1 and player['last_dark_acts'][0] != 'blue_beam_prepare':
                            player['act'] = ['blue_beam_prepare', target]

                else:
                    player['act'] = [player['prepared_beam'][0], player['prepared_beam'][1]]
    except:
        #print(traceback.format_exc())
        player['act'] = ['skip', 'self']
        bot.send_message(441399484, traceback.format_exc())

def npcact_darkdemon(game, player):
    enemys, enemys_close, enemys_can_attack_me, enemys_i_can_attack, enemys_zombie, enemys_stunned, enemys_hitin, enemys_lostweapon, allys, lowesthealth, highesthealth, hitins, enemys_not_zombie = getenemys(
        game, player)
    if player['darkcastle_demon']:
        #bot.send_message(441399484, "demon=True")
        demonacts = []
        if len(enemys_can_attack_me) >= len(allys) and player['demonshieldcd'] <= 0:
            demonacts.append('demonshield')
        if player['energy'] <= 0:
            demonacts.append('demonreload')
        if player['energy'] > 0:
            demonacts.append('demonattack')
        if player['darkdemon_strenght'] >= 40 and player['demondestroycd'] <= 0:
            demonacts.append("demondestroy")
        if demonacts == []:
            if player['energy'] > 0:
                demonacts.append('demonattack')
            else:
                demonacts.append('demonreload')
        demonact = random.choice(demonacts)
        #print(demonact)
        if demonact == "demonattack":
            beams = ['red', 'blue', 'violet']
            beam = random.choice(beams)
            player['demonbeam'] = beam
            targets = []
            if len(enemys_zombie) == len(enemys_i_can_attack):
                for ids in enemys_i_can_attack:
                    targets.append(ids)
                    if game['players'][ids]['hp'] == lowesthealth:
                        targets.append(ids)
            elif len(hitins) == len(enemys_i_can_attack):
                for ids in enemys_i_can_attack:
                    if not game['players'][ids]['zombie']:
                        targets.append(ids)
                        if game['players'][ids]['hp'] == lowesthealth:
                            targets.append(ids)
            else:
                for ids in enemys_i_can_attack:
                    if len(game['players'][ids]['hitins']) == 0 and not game['players'][ids][
                        'zombie']:  # and game['players'][ids]['necrozombie'] <= 0:
                        targets.append(ids)
                        if game['botfight']:
                            if game['players'][ids]['hp'] == highesthealth:
                                targets.append(ids)
                        else:
                            if game['players'][ids]['hp'] == lowesthealth:
                                targets.append(ids)
            if len(targets) > 0:
                target = random.choice(targets)
                player['act'] = ['demonattack', target]
        elif demonact == "demonshield":
            player['act'] = ['demonshield', "self"]
        elif demonact == "demonreload":
            player['act'] = ['demonreload', "self"]
        elif demonact == "demondestroy":
            targets = []
            for ids in enemys:
                if game['players'][ids]['hp'] == highesthealth:
                    targets.append(ids)
            target = random.choice(targets)
            player['act'] = ['demondestroy', target]
        return

def getenemys(game, player):
    enemys = []
    enemys_close = []
    enemys_can_attack_me = []
    enemys_i_can_attack = []
    enemys_zombie = []
    enemys_stunned = []
    enemys_hitin = []
    enemys_lostweapon = []
    allys = []
    enemys_not_zombie = []
    lowesthealth = 10000
    highesthealth = -1
    for ids in game['players']:
        target = game['players'][ids]
        if (target['team'] in player['allies'] or target['team'] == player['team']) and not target['dead']:
            allys.append(target['id'])
        if target['team'] != player['team'] and not target['dead'] and target['team'] not in player['allies']:
            if target['id'] not in enemys:
                enemys.append(target['id'])
            if target['id'] in player['nearplayers']:
                enemys_close.append(target['id'])
            if target['zombie'] <= 0 and target['necrozombie'] <= 0 and target["controllable_necrofighter"] == None:
                enemys_not_zombie.append(target['id'])
            if target['weapon'].ranged or player['id'] in target['nearplayers'] or (
                    target['weapon'].name == 'Шест' and target['shestcd'] <= 0):
                if target['controllable_necrofighter'] == None:
                    if target['weapon'].name == 'Пулемет' and target['machinegun_charges'] < 4:
                        pass
                    elif target['weapon'].name == 'Дробовик' and target['drobovik_charges'] < 1:
                        pass
                    else:
                        enemys_can_attack_me.append(target['id'])
            if ("dragon_power" in target["skills"] and target["energy"] >= 3) or (target["is_dragon"] and target["energy"] >= 2):
                if target['id'] not in enemys_can_attack_me:
                    enemys_can_attack_me.append(target['id'])
            if player['weapon'].ranged or target['id'] in player['nearplayers'] or 'носорог' in player['name'].lower() or (
                    'charge' in player['skills'] and player['chargecd'] <= 0) or (player['darkcastle_demon']):
                if target['controllable_necrofighter'] == None:
                    enemys_i_can_attack.append(target['id'])
                else:
                    if target['stun'] > 0:
                        enemys_i_can_attack.append(target['id'])
            if target['zombie'] > 0 or target['necrozombie'] > 0:
                enemys_zombie.append(target['id'])
            if target['stun'] > 0:
                enemys_stunned.append(target['id'])
            if len(target['hitins']) > 0:
                enemys_hitin.append(target['id'])
            if target['hp'] < lowesthealth:
                lowesthealth = target['hp']
            if target['hp'] > highesthealth:
                highesthealth = target['hp']
            if target['droppedweapon'] != None:
                enemys_lostweapon.append(target['id'])
    hitins = []
    for ids in game['players']:
        target = game['players'][ids]
        if target['team'] != player['team'] and not target['dead']:
            if target['id'] in player['nearplayers']:
                canattack = True
            if len(target['hitins']) > 0 and target['id'] in enemys_i_can_attack:
                hitins.append(target['id'])
    return enemys, enemys_close, enemys_can_attack_me, enemys_i_can_attack, enemys_zombie, enemys_stunned, enemys_hitin, enemys_lostweapon, allys, lowesthealth, highesthealth, hitins, enemys_not_zombie

def npcact_radiodemon(game, player):
    enemys, enemys_close, enemys_can_attack_me, enemys_i_can_attack, enemys_zombie, enemys_stunned, enemys_hitin, enemys_lostweapon, allys, lowesthealth, highesthealth, hitins, enemys_not_zombie = getenemys(
        game, player)
    if len(enemys) == 0:
        player['act'] = ['skip', 'self']
        return
    if player['tentacles_turn']:
        player['tentacles_turn'] = False
        player['act'] = ['tentacles2', player['tentacles_target']]
        return
    if player['demon_transform_turn']:
        player['demon_transform_turn'] = False
        player['act'] = ['demon_transform2', 'self']
        return
    specials = ['tentacles', 'mind_control', 'demon_transform', 'energy_blow', 'rhino_eliminate']
    if player['tentaclescd'] > 0:
        specials.remove('tentacles')
    if player['mind_controlcd'] > 0:
        specials.remove('mind_control')
    if player['demon_transformcd'] > 0:
        specials.remove('demon_transform')
    if player['energy_blowcd'] > 0:
        specials.remove('energy_blow')
    if player['rhino_eliminatecd'] > 0:
        specials.remove('rhino_eliminate')
    if len(enemys_i_can_attack) > 0:
            targets = []
            if len(enemys_zombie) == len(enemys_i_can_attack):
                for ids in enemys_i_can_attack:
                    targets.append(ids)
                    if game['players'][ids]['hp'] == lowesthealth:
                        targets.append(ids)
            elif len(hitins) == len(enemys_i_can_attack):
                for ids in enemys_i_can_attack:
                    if not game['players'][ids]['zombie']:
                        targets.append(ids)
                        if game['players'][ids]['hp'] == lowesthealth:
                            targets.append(ids)
            else:
                for ids in enemys_i_can_attack:
                    if len(game['players'][ids]['hitins']) == 0 and not game['players'][ids][
                        'zombie']:  # and game['players'][ids]['necrozombie'] <= 0:
                        targets.append(ids)
                        if game['botfight']:
                            if game['players'][ids]['hp'] == highesthealth:
                                targets.append(ids)
                        else:
                            if game['players'][ids]['hp'] == lowesthealth:
                                targets.append(ids)
            if len(targets) > 0:
                target = random.choice(targets)
                x = random.randint(1, 100)
                if len(specials) > 0 and x <= 50:
                    player['act'] = [random.choice(specials), target]
                else:
                    player['act'] = ['attack', target]
            else:
                if player['energy'] < player['maxenergy']:
                    act = 'reload'
                else:
                    act = 'skip'
    else:
        player['act'] = ['skip', 'self']

def npcact(game, player):
  try:
    if player["maintarget"] != None and game["players"][player["maintarget"]["target"]]["dead"]:
        player["maintarget"] = None
    if player['lastattacktarget'] != None:
        player['act'] = ['lastcharge', player['lastattacktarget']]
        return
    if player['team'] == 'dummys':
        player['act'] = ['dummy', 'self']
        return
    hitchance = gethitchance(player)
    if player["weapon"].name == "Снайперская винтовка" and player["energy"] > 0:
        hitchance += 100
    basehitchance = hitchance
    acts = []
    neardeath = False
    nextturndeath = False
    if player['hp'] == 1 or (player['hp'] == 2 and player['blood'] == 1):
        neardeath = True
    if player['hp'] == 1 and player['blood'] == 1:
        nextturndeath = True
    can_regen = True
    debuff = 0
    for ids in player['recoverydebuff']:
        debuff += ids[0]
    if debuff >= player['maxenergy']-player['energy']:
        can_regen = False

    enemys, enemys_close, enemys_can_attack_me, enemys_i_can_attack, enemys_zombie, enemys_stunned, enemys_hitin, enemys_lostweapon, allys, lowesthealth, highesthealth, hitins, enemys_not_zombie = getenemys(game, player)
    if len(enemys) == 0:
        player['act'] = ['skip', 'self']
        return
    stun_this_turn = False
    for ids in player["hitins"]:
        if player['hitins'][ids] == 1:
            stun_this_turn = True
    if player["zombie"] == 1:
        stun_this_turn = True
    #print(player)
    #print(player['name'])
    #print("enemys_close=", str(enemys_close))
    #print("enemys_i_can_attack=", str(enemys_i_can_attack))
    if len(enemys_can_attack_me) == 0 and len(enemys_i_can_attack) == 0:
        if 'knife' in player['inventory']:
            acts.append('knife')   
    if game['turn'] == 1 and random.randint(1, 100) <= 50 and 'knife' in player['inventory']:
        acts.append('knife')  
    if "dark_energy" in player["skills"] and player["dark_energycd"] <= 0:
        if player["dark_counter"] <= 0:
            acts.append("dark_energy")
        else:
            if random.randint(1, 100) <= 40:
                acts.append("dark_energy")
    if 'demon' in player['skills'] and player['demoncd'] <= 0 and player['energy'] >= 3:
        acts.append("demon")
    if 'miner' in player['skills'] and player['minercd'] <= 0 and player["minetimer"] <= 0 and random.randint(1, 100) <= 40:
        acts.append("miner")
    if player['weapon'].name in ['Посох Некроманта'] and player['necrostaffabilitycd'] <= 0 and player['can_summon_zombie']:
        acts.append("necrostaffability")
    canattack = False
    if player['weapon'].ranged:
        canattack = True
    if player['is_rhino']:
        canattack = True
    low = False
    for ids in enemys_i_can_attack:
        if game['players'][ids]['energy'] <= player['energy'] or player['energy'] == player['maxenergy'] or game['players'][ids]['id'] not in enemys_can_attack_me:
            low = True
    if ('berserk' in player['skills'] or 'berserk?1' in player['skills'] or 'berserk?2' in player['skills'] or 'berserk?3' in player['skills']) and player['hp'] == 1:
        low = True
    if (player['energy'] >= 4 or player['energy'] == player['maxenergy']) and random.randint(1, 100) <= 50 and 'knife' in player['inventory']:
        acts.append('knife')
    if "wing_attack" in player["skills"] and player["wing_attackcd"] <= 0 and len(enemys_close) >= 1:
        acts.append("wing_attack")

    
    if not low:
        hitchance -= 40
    if len(hitins) == len(enemys_i_can_attack):
        hitchance -= 50
    if basehitchance < 70:
        hitchance -= 20
    if basehitchance < 60:
        hitchance -= 20
    if len(enemys_i_can_attack) == len(enemys_zombie):
        hitchance -= 100
    if player['droppedweapon'] != None:
        hitchance -= 100
        acts.append('pickupweapon')
    if player['fell']:
        hitchance -= 100
    if 'носорог' in player['name'].lower() and hitchance > 0:
        hitchance += 20
    if random.randint(1, 100) <= hitchance and canattack:
        acts.append('attack')
    need_pricel = True
    if player["maintarget"] != None:
        need_pricel = False
    if player["energy"] > 0 and player["weapon"].name == "Снайперская винтовка" and need_pricel:
        acts.append("pricel")
    if "dragon_fireball" in player["skills"] and len(enemys_close) == 0 and player["dragon_fireballcd"] <= 0 and player["energy"] >= 2:
        acts.append('dragon_fireball')
    if 'bomber' in player['skills'] and player['EXPLOSIONcd'] <= 0 and player['energy'] >= 5 and random.randint(1, 100) <= 40:
        acts.append('EXPLOSION')
    if 'doom' in player['skills'] and player['doomcd'] <= 0 and player['energy'] >= 1 and random.randint(1, 100) <= 40:
        acts.append('doom')
    else:
        if player['energy'] >= 2:
            if 'grenade' in player['inventory'] and random.randint(1, 100) <= 50 and not player['fell']:
                acts.append('grenade')
            if True: #len(enemys_can_attack_me) > 0 or len(enemys_i_can_attack) > 0:
                if 'molotov' in player['inventory']:
                    molotov = True
                    for ids in enemys:
                        if game['players'][ids]['fireticks'] > 1:
                            molotov = False
                    if molotov and random.randint(1, 100) <= 50 and not player['fell']:
                        acts.append('molotov')
            if 'knife' in player['inventory'] and player['energy'] >= 4:
                if len(enemys) != len(enemys_zombie) and random.randint(1, 100) <= 50 and not player['fell']:
                    acts.append('knife')
        if player['energy'] <= 3 and player['energy'] < player['maxenergy']:
            if game['freeze_energy'] <= 0:             
                if can_regen:
                    if random.randint(1, 100) <= 100-(player['energy']*15):
                        acts.append('reload')
    if game['castlefight']:
        if 'molotov' in player['inventory'] and player['energy'] >= 2:
            molotov = True
            for ids in enemys:
                if game['players'][ids]['fireticks'] > 1:
                    molotov = False
            if random.randint(1, 100) <= 50 and molotov and not player['fell']:
                acts.append('molotov')
        if player['energy'] >= 2 and 'grenade' in player['inventory'] and random.randint(1, 100) <= 50 and not player['fell']:
            acts.append('grenade')
    if player['energy'] == 0:
        if 'reload' not in acts:
            if game['freeze_energy'] <= 0 and can_regen:
                acts.append('reload')
        if 'adrenaline' in player['inventory']:
            if len(enemys_i_can_attack) != len(enemys_zombie) and random.randint(1, 100) <= 50:
                if game['freeze_energy'] <= 0:
                    if debuff <= 1 and not player['fell']:
                        if player["weapon"].name != "Снайперская винтовка":
                            acts.append('adrenaline')
                        else:
                            if player['maintarget'] != None:
                                acts.append('adrenaline')
                                
                            
                            
    if player['energy'] > 0 and 'носорог' in player['name'].lower():
        if 'attack' not in acts:
            acts.append('attack')
        if 'reload' in acts:
            acts.remove('reload')
    if player["weapon"].name == "Копье Нарсил" and random.randint(1, 100) <= 60 and player['energy'] >= 3 and player[
        'narsilcd'] <= 0:
        acts.append('throw_narsil')
    dopacts = []
    dopitems = []
    flashtargets = []
    hypnotargets = []
    for ids in game['players']:
        target = game['players'][ids]
        if target['team'] != player['team'] and not target['dead']:
            targethitchance = gethitchance(target)
            if target['maintarget'] != None and target['weapon'].name == 'Снайперская винтовка':
                if target['energy'] > 0:
                    targethitchance += (target['maintarget']['power']*60)
            if target['stun'] > 0 or target['fell']:
                targethitchance = 0
            if "dragon_power" in target["skills"] and target["wing_attackcd"] <= 0 and player["id"] in target["nearplayers"]:
                targethitchance -= 50
            if "dragon_power" in target["skills"] and player["id"] not in target["nearplayers"] and target["energy"] >= 3:
                if target["energy"] == 3:
                    targethitchance = 92
                elif target["energy"] == 4:
                    targethitchance = 97
                elif target["energy"] == 5:
                    targethitchance = 99
                else:
                    targethitchance = 100
            perekatchance = targethitchance - 30
            shieldchance = targethitchance - 30
            flashchance = targethitchance - 30
            hypnotistchance = targethitchance - 30
            counterattackchance = targethitchance
            molitvachance = 0
            if neardeath:
                molitvachance += targethitchance
            if player['fell'] and neardeath and targethitchance > 50:
                shieldchance += 40
                flashchance += 40
                hypnotistchance += 40
            if targethitchance > 98 and 'ninja' not in player['skills']:
                perekatchance = 0
            if player['is_vurdalak'] or player['is_magmaworm'] or player['is_lucifer']:
                perekatchance -= 100
            if 'Дряхлый скелет' in player['name'] and player['weakskeletype'] != 'afraid_of_loneliness':
                perekatchance -= 100
            if targethitchance < 70:
                if not neardeath:
                    shieldchance = 0
                    flashchance = 0
                    hypnotistchance = 0
                    perekatchance = 0
                    counterattackchance = 0
                else:
                    if targethitchance < 50:
                        shieldchance = 0
                        flashchance = 0
                        hypnotistchance = 0
                        perekatchance = 0
                        counterattackchance = 0
            if player['weapon'].name == 'Мраморная колонна':
                perekatchance = 0
            if target['fireticks'] > 1 and target['firestrength'] > 1:
                perekatchance = 0
                shieldchance = 0
                flashchance = 0
                hypnotistchance = 0
                counterattackchance = 0
                molitvachance = 0
            if len(player['hitins']) > 0:
                perekatchance = 0
                shieldchance = 0
                flashchance = 0
                hypnotistchance = 0
                counterattackchance = 0
                molitvachance = 0
            if target['energy'] < 4:
                flashchance = 0
            if len(enemys_can_attack_me) == 0:
                perekatchance = 0
                shieldchance = 0
                flashchance = 0
                hypnotistchance = 0
                counterattackchance = 0
                molitvachance = 0
            if len(enemys_lostweapon) == len(enemys_can_attack_me):
                perekatchance = 0
                shieldchance = 0
                flashchance = 0
                hypnotistchance = 0
                molitvachance = 0
            if target['zombie'] and target['energy'] > 1:
                perekatchance = 100
                shieldchance = 100
                flashchance = 100
                hypnotistchance = 100
                counterattackchance = 100
                if neardeath:
                    molitvachance = 100
            if player['zombie'] != False:
                perekatchance = 0
                shieldchance = 0
                flashchance = 0
                hypnotistchance = 0
                counterattackchance = 0
                molitvachance = 0
            if len(enemys_stunned) == len(enemys_can_attack_me):
                perekatchance = 0
                shieldchance = 0
                flashchance = 0
                hypnotistchance = 0
                molitvachance = 0
            if player['fell']:
                perekatchance = 0
                counterattackchance = 0
            if 'носорог' in player['name'].lower():
                perekatchance = 0
            if player["is_knight"]:
                counterattackchance = 0
            if random.randint(1, 100) <= perekatchance:
                if 'perekat' not in dopacts and player['perekatcd'] <= 0:
                    dopacts.append('perekat')
            if random.randint(1, 100) <= shieldchance:
                if player['weapon'].name in ['Посох Некроманта'] and player['necrostaffabilitycd'] <= 0 and player['can_summon_zombie']:
                    dopacts.append('necrostaffability')
                else:
                    if 'shieldgen' not in dopacts and player['shieldgencd'] <= 0 and 'shieldgen' in player['skills']:
                        dopacts.append('shieldgen')
                    if 'shield' not in dopacts and 'shield' in player['inventory'] and 'shieldgen' not in dopacts:
                        dopacts.append('shield')
                    if 'hitin' in player['inventory'] and 'shield' not in dopacts and 'shieldgen' not in dopacts and 'perekat' not in dopacts:
                        if random.randint(1, 100) <= 60:
                            dopitems.append('hitin')
            if random.randint(1, 100) <= counterattackchance:
                if player['spearcd'] <= 0 and player['weapon'].name in ['Копье', 'Копье Нарсил']:
                    if len(allys) <= len(enemys_can_attack_me):
                        if basehitchance >= 70:
                            if random.randint(1, 100) <= basehitchance:
                                dopacts.append('counterattack')
            if random.randint(1, 100) <= molitvachance:
                if player['incvizitorcd'] <= 0 and ('incvizitor' in player['skills'] or 'incvizitor?1' in player['skills'] or 'incvizitor?2' in player['skills'] or 'incvizitor?3' in player['skills']):
                    dopacts.append('molitva')
            if random.randint(1, 100) <= flashchance:
                if 'flash' in player['inventory']:
                    if target['id'] not in game['flashed'] and 'hitin' not in dopitems:
                        if target['id'] in enemys_can_attack_me:
                            if 'protivogaz' not in target['skills']:
                                dopacts.append('flash')
                                flashtargets.append(target['id'])
            if random.randint(1, 100) <= hypnotistchance and 'hypnotist' in player['skills']:
                if player['hypnotistcd'] <= 0 and 'hitin' not in dopitems:
                    if target['id'] not in game['flashed']:
                        if target['id'] in enemys_can_attack_me:
                            dopacts.append('hypnotist')
                            hypnotargets.append(target['id'])
            if target['hp'] == 1:
                if 'adrenaline' in player['inventory'] and player['energy'] <= 3:
                    if game['freeze_energy'] <= 0:
                        if debuff <= 1:
                            dopacts.append('adrenaline')
                
    
    for ids in dopacts:
        acts.append(ids)
    if len(enemys) != len(enemys_close) and not player['weapon'].ranged and 'носорог' not in player['name'].lower():
        if len(enemys_can_attack_me) == 0 and len(enemys_i_can_attack) == 0 and player['energy'] < player['maxenergy'] and can_regen and "dragon_power" not in target["skills"]:
            acts.append('reload')
        else:
            if 'charge' not in player['skills'] or ('charge' in player['skills'] and player['chargecd'] > 0):
                if len(enemys_i_can_attack) == 0 and "dragon_fireball" not in player["skills"]:
                    if player["weapon"].name == "Копье Нарсил" and random.randint(1, 100) <= 75 and player['energy'] >= 3 and player['narsilcd'] <= 0:
                        acts.append('throw_narsil')
                    else:
                        acts.append('walk')
                        acts.append('walk')
                        acts.append('walk')
                        acts.append('walk')
    if 'stimulator' in player['inventory'] and (player['maxhp'] - player['hp']) >= 2 and random.randint(1, 100) <= 80:
        if len(enemys_stunned) != len(enemys):
            acts.append('stimulator')
    
    if player['fireticks'] > 1 and len(player['hitins']) == 0:
        if not player['zombie'] and 'hitin' not in dopitems and 'носорог' not in player['name'].lower() and not player['is_imp'] and not player['is_magmaworm'] and not player['is_lucifer']:
            acts.append('skip')
            if 'perekat' in acts:
                acts.remove('perekat')
            if 'flash' in acts:
                acts.remove('flash')
    for ids in enemys:
        target = game['players'][ids]
        if player["id"] not in target["nearplayers"] and ("dragon_power" in target["skills"] or "dragon_fireball" in target["skills"]) and not player["is_dragon"] and "носорог" not in player["name"].lower():
            acts.append("walk")
    if len(acts) == 0:
        if (player['energy'] <= 2 and player['energy']<player['maxenergy']):
            if game['freeze_energy'] <= 0 and can_regen:
                acts.append('reload')
            else:
                if player['energy'] > 0:
                    acts.append('attack')
                else:
                    acts.append('skip')
        else:
            acts.append('attack')
        if player['weapon'].name == 'Рог':
            if player['energy'] > 0:
                acts = ['attack']
            else:
                acts = ['reload']

    if not player['is_imp'] and not player['is_magmaworm'] and not player['is_lucifer']:
        if player['fireticks'] > 1 and len(player['hitins']) == 0 and 'hitin' not in dopitems and not player['zombie']:
            acts.append('skip')
            if 'reload' in acts:
                acts.remove('reload')
            if 'stimulator' in acts:
                acts.remove('stimulator')
            if 'walk' in acts:
                acts.remove('walk')
            if 'knife' in acts:
                acts.remove('knife')
    if player['is_imp'] or player['is_lucifer'] or player['is_magmaworm']:
        try:
            acts.remove('skip')
        except:
            pass
    
    if player["weapon"].name == "Лук Асгард":
        if player['bowcharge'] > 0:
            newacts = []
            if player["energy"] <= 0:
                pass
            else:
                dmg = 1
                dmg += player['bowcharge']*2
                if "skip" in acts and player["firestrength"] > dmg and player["fireticks"] > 1:
                    newacts.append("skip")
                else:
                    newacts.append("attack")
                acts = newacts

    act = random.choice(acts)
    if 'носорог' not in player['name'].lower() and not player['is_imp'] and not player['is_magmaworm'] and not player['is_lucifer']:
        #if player['fireticks'] > 1 and len(player['hitins']) == 0 and 'hitin' not in dopitems and not player['zombie']:
        #    act = 'skip'
        if player['fireticks'] > 1 and player['firestrength'] > 1:
            if len(player['hitins']) == 0 and not player['zombie']:
                act = 'skip'

        if player['fireticks'] > 1 and player['firestrength'] > 2 and (player['zombie'] > 1 or not player['zombie']):
            act = 'skip'
    if not player['zombie']:
        if player['blood'] == 1 and player['hp'] == 1 and 'stimulator' in player['inventory']:
            act = 'stimulator'
    if player['zombie']:
        if 'hitin' in player['inventory']:
            dopitems.append('hitin')
        if player['zombie'] >= 1:
            if player['energy'] > 0:
                if len(enemys_i_can_attack) > 0:
                    act = 'attack'
            if 'adrenaline' in player['inventory'] and debuff <= 1:
                if len(enemys_i_can_attack) > 0:
                    act = 'adrenaline'
            else:
                if 'knife' in player['inventory']:
                    act = 'knife'
            if player['energy'] >= 2 and 'grenade' in player['inventory']:
                act = 'grenade'
        else:
            if basehitchance < 50:
                if player['energy'] < player['maxenergy'] and can_regen:
                    act = 'reload'
                else:
                    if len(enemys_i_can_attack) > 0:
                        act = 'attack'
            if basehitchance <= 65 and basehitchance >= 50:
                if random.randint(1, 100) <= basehitchance:
                    if len(enemys_i_can_attack) > 0:
                        act = 'attack'
                else:
                    if player['energy'] < player['maxenergy'] and can_regen:
                        act = 'reload'
                    else:
                        if len(enemys_i_can_attack) > 0:
                            act = 'attack'
            if basehitchance > 65:
                if len(enemys_i_can_attack) > 0:
                    act = 'attack'
            if player['fireticks'] > 1 and player['firestrength'] > 2 and player['weapon'].name == 'Огнемет':
                if player['energy'] > 1:
                    act = 'skip'
                else:
                    if can_regen:
                        act = 'reload'
    if player['necrozombie'] > 0:
        if len(enemys_i_can_attack) > 0:
            act = 'attack'
        else:
            act = 'walk'

    if player['castle_explosion']:
        if len(enemys) > 0:
            enemy = random.choice(enemys)
            player['act'] = ["castle_explosion", enemy]
            return
    if player['summon_dark_demon']:
        player['act'] = ["summon_dark_demon", "self"]
        player['summon_dark_demon'] = False
        return

    #if player['weapon'].name == 'Посох Некроманта':
    #    player['act'] =

    if player['darkcastle_demon']:
        #bot.send_message(441399484, "demon=True")
        demonacts = []
        if len(enemys_can_attack_me) >= len(allys) and player['demonshieldcd'] <= 0:
            demonacts.append('demonshield')
        if player['energy'] <= 0:
            demonacts.append('demonreload')
        if player['energy'] > 0:
            demonacts.append('demonattack')
        if player['darkdemon_strenght'] >= 50 and player['demondestroycd'] <= 0:
            demonacts.append("demondestroy")
        demonact = random.choice(demonacts)
        if demonact == "demonattack":
            beams = ['red', 'blue', 'violet']
            beam = random.choice(beams)
            player['demonbeam'] = beam
            targets = []
            if len(enemys_zombie) == len(enemys_i_can_attack):
                for ids in enemys_i_can_attack:
                    targets.append(ids)
                    if game['players'][ids]['hp'] == lowesthealth:
                        targets.append(ids)
            elif len(hitins) == len(enemys_i_can_attack):
                for ids in enemys_i_can_attack:
                    if not game['players'][ids]['zombie']:
                        targets.append(ids)
                        if game['players'][ids]['hp'] == lowesthealth:
                            targets.append(ids)
            else:
                for ids in enemys_i_can_attack:
                    if len(game['players'][ids]['hitins']) == 0 and not game['players'][ids][
                        'zombie']:  # and game['players'][ids]['necrozombie'] <= 0:
                        targets.append(ids)
                        if game['botfight']:
                            if game['players'][ids]['hp'] == highesthealth:
                                targets.append(ids)
                        else:
                            if game['players'][ids]['hp'] == lowesthealth:
                                targets.append(ids)
            if len(targets) > 0:
                target = random.choice(targets)
                player['act'] = ['demonattack', target]
        elif demonact == "demonshield":
            player['act'] = ['demonshield', "self"]
        elif demonact == "demonreload":
            player['act'] = ['demonreload', "self"]
        elif demonact == "demondestroy":
            targets = []
            for ids in enemys:
                if game['players'][ids]['hp'] == highesthealth:
                    targets.append(ids)
            target = random.choice(targets)
            player['act'] = ['demondestroy', target]
        return

    if player['is_lucifer']:
        if player['hp'] <= 3:
            if not player['used_doom']:
                player['used_doom'] = True
                player['act'] = ['use_doom', 'self']
                return
        if player['rest_after_doom'] > 0:
            player['act'] = ['rest_after_doom', 'self']
            return
        if 'lucifer_hellfire' in player['skills'] and player['lucifer_hellfirecd'] <= 0:
            player['lucifer_hellfirecd'] = 6
            player['act'] = ['lucifer_hellfire', 'self']
            return
    try:
        if player['is_catapult']:
            if player['charge_stage'] == 0:
                player['act'] = ['charge_catapult_1', 'self']
                return
            if player['charge_stage'] == 1:
                player['act'] = ['charge_catapult_2', 'self']
                return
            if player['charge_stage'] == 2:
                player['act'] = ['charge_catapult_3', 'self']
                return
            if player['charge_stage'] == 3:
                if len(enemys) > 0:
                    target = random.choice(enemys)
                    for idss in enemys:
                        if game['players'][idss]['is_wall']:
                            target = game['players'][idss]['id']
                            break
                    player['act'] = ['attack_catapult', target]
                else:
                    player['act'] = ['skip', 'self']
                return
    except:
        pass

    if act == "throw_narsil":
        act = "attack"

    if act == 'attack':
        if player['hp'] >= 1 and 'grenade' in player['inventory'] and player['energy'] >= 2 and random.randint(1, 100) <= 40: 
            act = 'grenade'
    charge = False
    if act == 'attack':
        if 'носорог' in player['name'].lower() and player['chargecd'] <= 0:
            charge = True
        if 'charge' in player['skills'] and player['chargecd'] <= 0:
            charge = True
    if act == "attack":
        if player["weapon"].name == "Снайперская винтовка" and player["maintarget"] == None:
            act = "pricel"
    if act == 'attack' or act == 'adrenaline':
        who_attack = None
        targets = []
        if len(enemys_zombie) == len(enemys_i_can_attack):
            for ids in enemys_i_can_attack:
                targets.append(ids)
                if game['players'][ids]['hp'] == lowesthealth:
                    targets.append(ids)
        elif len(hitins) == len(enemys_i_can_attack):
            for ids in enemys_i_can_attack:
                if not game['players'][ids]['zombie']:
                    targets.append(ids)
                    if game['players'][ids]['hp'] == lowesthealth:
                        targets.append(ids)
        else:
            for ids in enemys_i_can_attack:
                if len(game['players'][ids]['hitins']) == 0 and not game['players'][ids]['zombie']:# and game['players'][ids]['necrozombie'] <= 0:
                    targets.append(ids)
                    if game['botfight']:
                        if game['players'][ids]['hp'] == highesthealth:
                            targets.append(ids)
                    else:
                        if game['players'][ids]['hp'] == lowesthealth:
                            targets.append(ids)
        if player["weapon"].name == "Снайперская винтовка" and player["maintarget"] != None:
            try:
                targets = [player["maintarget"]["target"]["id"]]
            except:
                targets = [player["maintarget"]["target"]]

        if len(targets) > 0:
            target = random.choice(targets)
            try:
                target = target["id"]
            except:
                pass
            if player["weapon"].name == "Лук Асгард":
                if player['bowcharge'] == 0:
                    if random.randint(1, 100) <= 75 and not stun_this_turn and player["fireticks"] <= 1:
                        player['act'] = ['chargebow', "self"]
                        if "adrenaline" in dopitems:
                            dopitems.remove("adrenaline")
                    else:
                        player['act'] = ['attack', target]
                else:
                    ch = 50
                    if player['bowcharge'] == 1:
                        ch = 60
                    if player["bowcharge"] >= 3:
                        ch = 0
                    if random.randint(1, 100) <= ch and not stun_this_turn and player["fireticks"] <= 1:
                        player['act'] = ['chargebow', "self"]
                        if "adrenaline" in dopitems:
                            dopitems.remove("adrenaline")
                    else:
                        player['act'] = ['attack', target]

            else:
                if not player['fell']:
                    if player["weapon"].name == "Копье Нарсил" and random.randint(1, 100) <= 70 and player['energy'] >= 3 and player['narsilcd'] <= 0:
                        player['act'] = ['narsil', target]
                    else:
                        player['act'] = ['attack', target]
                else:
                    player['act'] = ['standup', 'self']
        else:
            if player["weapon"].name == "Копье Нарсил" and player['energy'] >= 3 and player['narsilcd'] <= 0:
                if len(enemys_not_zombie) > 0:
                    player['act'] = ['narsil', random.choice(enemys_not_zombie)]
                else:
                    player['act'] = ['narsil', random.choice(enemys)]
            else:
                if player['energy'] < player['maxenergy']:
                    act = 'reload'
                else:
                    act = 'skip'
        if player['weapon'].name == 'Цепь' and player['chaincd'] <= 0 and random.randint(1, 100) <= 70 and game['players'][target]['energy'] < game['players'][target]['maxenergy']:
            if not player['fell']:
                player['act'] = ['chain', target]
            else:
                player['act'] = ['standup', 'self']
        if player['weapon'].name == 'Лук' and player['firearrowcd'] <= 0 and random.randint(1, 100) <= 40:
            if not player['fell']:
                player['act'] = ['firearrow', target]
            else:
                player['act'] = ['standup', 'self']
        if player['weapon'].name == 'Шест' and player['shestcd'] <= 0 and random.randint(1, 100) <= 40:
            if not player['fell']:
                player['act'] = ['hitdown', target]
            else:
                player['act'] = ['standup', 'self']
        if player['weapon'].name == 'Обрез' and player['obrezcd'] <= 0 and random.randint(1, 100) <= 40 and (game['cwrats'] or game['cwduel'] or game['cwduelrats'] or game['castlefight']):
            if not player['fell']:
                player['act'] = ['strongshot', target]
            else:
                player['act'] = ['standup', 'self']
        if player['weapon'].name == 'Молот' and player['molotcd'] <= 0 and player['energy'] >= 4 and random.randint(1, 100) <= 50:
            if not player['fell']:
                player['act'] = ['truestrike', target]
            else:
                player['act'] = ['standup', 'self']
        if player["weapon"].name == "Копье Нарсил" and random.randint(1, 100) <= 60 and player['energy'] >= 3 and player['narsilcd'] <= 0:
            player['act'] = ['narsil', target]
        if 'burrow' in player['skills'] and player['burrowcd'] <= 0 and random.randint(1, 100) <= 50:
            player['act'] = ['burrow', target]
            return
        if player["act"] == "attack" and player["weapon"].name == "Копье Нарсил" and target["id"] not in player["nearplayers"]:
            player['act'] = ['narsil', target]

        kuvalda = False
        try:
            try:
                if player['sokrusheniecd'] <= 0 and player['energy'] >= 4 and target['energy'] > 1:# and game['players'][target]['energy'] < game['players'][target]['maxenergy']:
                    kuvalda = True
            except:
                try:
                    if player['sokrusheniecd'] <= 0 and player['energy'] >= 4 and game['players'][target]['energy'] > 1:# and game['players'][target]['energy'] < game['players'][target]['maxenergy']:
                        kuvalda = True
                except:
                    pass
        except:
            pass
        if player['weapon'].name == 'Кувалда' and kuvalda and random.randint(1, 100) <= 50:
            if not player['fell']:
                player['act'] = ['sokrush', target]     
            else:
                player['act'] = ['standup', 'self']
        if act == 'adrenaline':
            if not player['fell']:
                player['dopuseditems'].append(['adrenaline', player['id']])
        if charge:
            if not player['fell']:
                player['act'] = ['charge', target]
            else:
                player['act'] = ['standup', 'self']
    elif act == 'reload':
        player['act'] = ['reload', 'self']
        if player['fell']:
            player['act'] = ['standup', 'self']
        else:
            if 'dzet' in player['inventory'] and random.randint(1, 100) <= 50:
                dopitems.append('dzet')
            if 'madpotion' in player['inventory'] and 'dzet' not in dopitems and random.randint(1, 100) <= 30:
                dopitems.append('madpotion')
            if len(enemys_i_can_attack) > 0 and game['players'][enemys_i_can_attack[0]]['hp'] == 1:
                dopitems.append('madpotion')
            for ids in player['dzets']:
                if player['dzets'][ids] == 1 and 'madpotion' in player['inventory']:
                    dopitems.append('madpotion')
    elif act == "pricel":
        priceltarget = random.choice(enemys)
        if player["maintarget"] != None and not game["players"][player["maintarget"]["target"]]["dead"]:
            priceltarget = player["maintarget"]["target"]
        player["act"] = ["pricel", priceltarget]
    elif act == 'shield':
        player['act'] = ['shield', player['id']]
    elif act == 'counterattack':
        player['act'] = ['counterattack', 'self']
    elif act == 'shieldgen':
        player['act'] = ['shieldgen', player['id']]
    elif act == 'molitva':
        player['act'] = ['incvizitor', player['id']]
    elif act == 'flash':
        ft = random.choice(flashtargets)
        player['act'] = ['flash', ft]
        game['flashed'].append(ft)
    elif act == 'walk':
        player['act'] = ['walk', 'self']
    elif act == 'skip':
        player['act'] = ['skip', 'self']
    elif act == 'grenade':
        if not player['fell']:
            player['act'] = ['grenade', 'self']
        else:
            player['act'] = ['standup', 'self']
    elif act == 'molotov':
        if not player['fell']:
            player['act'] = ['molotov', 'self']
        else:
            player['act'] = ['standup', 'self']
    elif act == 'perekat':
        if not player['fell']:
            player['act'] = ['perekat', 'self']
        else:
            if 'shieldgen' in player['skills'] and player['shieldgencd'] <= 0:
                player['act'] = ['shieldgen', player['id']]
            elif 'shield' in player['inventory']:
                player['act'] = ['shield', player['id']]
            else:
                player['act'] = ['standup', 'self']
    elif act == 'knife':
        if not player['fell']:
            player['act'] = ['knife', random.choice(enemys)]
        else:
            player['act'] = ['standup', 'self']
    elif act == 'dark_energy':
        if player["dark_counter"] <= 0:
            player['act'] = ['dark_energy', player["id"]]
        else:
            if len(enemys_not_zombie) > 0:
                player['act'] = ['dark_energy', random.choice(enemys_not_zombie)]
            else:
                player['act'] = ['dark_energy', random.choice(enemys)]
    elif act == "necrostaffability":
        player['act'] = ["necrostaffability", "self"]
    elif act == 'demon':
        if len(enemys_not_zombie) > 0:
            player['act'] = ['demon_steal', random.choice(enemys_not_zombie)]
        else:
            player['act'] = ['demon_steal', random.choice(enemys)]
    elif act == 'doom':
        if len(enemys_not_zombie) > 0:
            player['act'] = ['doom', random.choice(enemys_not_zombie)]
        else:
            player['act'] = ['doom', random.choice(enemys)]
    elif act == 'miner':
        player["act"] = ["setmine", str(random.randint(1, 4))]
    elif act == 'EXPLOSION':
        if not player['fell']:
            if len(enemys_not_zombie) > 0:
                player['act'] = ['EXPLOSION', random.choice(enemys_not_zombie)]
            else:
                player['act'] = ['EXPLOSION', random.choice(enemys)]
        else:
            player['act'] = ['standup', 'self']
    elif act == "dragon_fireball":
        if not player['fell']:
            player['act'] = ['dragon_fireball', random.choice(enemys)]
        else:
            player['act'] = ['standup', 'self']
    elif act == "wing_attack":
        if not player['fell']:
            player['act'] = ['wing_attack', "self"]
        else:
            player['act'] = ['standup', 'self']
    elif act == 'stimulator':
        player['act'] = ['stimulator', player['id']]
    elif act == 'pickupweapon':
        player['act'] = ['pickupweapon', 'self']
    elif act == 'hypnotist':
        gt = random.choice(hypnotargets)
        player['act'] = ['hypnotist', gt]
        game['flashed'].append(gt)
    illusion = False
    for ids in enemys_can_attack_me:
        if game['players'][ids]['energy'] <= 1 or game['players'][ids]['energy'] >= 5:
            illusion = True
    if game['turn'] == 1:
        illusion = True
    if 'illusionist' in player['skills'] and player['illusioncd'] <= 0:# and illusion:
        player['createillusion'] = True
    if nextturndeath:
        if player['incvizitorcd'] <= 0 and ('incvizitor' in player['skills'] or 'incvizitor?1' in player['skills'] or 'incvizitor?2' in player['skills'] or 'incvizitor?3' in player['skills']):
            player['act'] = ['incvizitor', player['id']]
            player['dopuseditems'] = []

    for ids in dopitems:
        if ids == "adrenaline" and player["act"][0] == "chargebow":
            pass
        else:
            player['dopuseditems'].append([ids, player['id']])

    if 'Вирус-мутант' in player['name']:
        if random.randint(1, 100) <= 60:
            highest_energy = 0
            for ids in enemys_i_can_attack:
                if game['players'][ids]['energy'] > highest_energy:
                    highest_energy = game['players'][ids]['energy']
            who_attack = None
            targets = []
            for ids in enemys_i_can_attack:
                if game['players'][ids]['energy'] == highest_energy:
                    targets.append(ids)

            if len(targets) > 0:
                target = random.choice(targets)
                player['act'] = ['attack', target]
                player['virus_attacks'] += 1
            else:
                player['act'] = ['virus_wait', 'self']
        else:
            player['act'] = ['virus_wait', 'self']
    if 'Дряхлый скелет' in player['name'] and player['weakskeletype'] == 'normal' and player['act'][0] == 'attack':
        if game['players'][player['act'][1]]['hp'] <= 1:
            player['act'] = ['weakskele_surrender', 'self']
            
    if 'Дряхлый скелет' in player['name'] and player['weakskeletype'] == 'afraid_of_loneliness':
        has_ghoul = False
        for ids in game['players']:
            target = game['players'][ids]
            if 'Вурдалак' in target['name'] and not target['dead'] and target['controller'] == 'bot':
                has_ghoul = True
                break
        if not has_ghoul:
            player['act'] = ['weakskele_lone_surrender', 'self']
    if player['act'] != None and player['act'][0] == 'attack' and player['weapon'].name == 'Мраморная колонна':
        if player['madskele_attack'] == 0:
            player['act'] = ['madskele_prepare', 'self']
        elif player['madskele_attack'] == 1:
            if random.randint(1, 100) <= 50 and not player['already_wait']:
                player['act'] = ['madskele_wait', 'self']
                player['already_wait'] = True
            else:
                player['madskele_attack'] = 0
                player['already_wait'] = False
    if player['weapon'].name == 'Мраморная колонна' and player['act'][0] != 'attack' and player['act'][0] != 'madskele_wait' and player['madskele_attack'] == 1:
        if random.randint(1, 100) <= 50 and not player['already_wait']:
            player['act'] = ['madskele_wait', 'self']
            player['already_wait'] = True
        else:
            if len(enemys_i_can_attack) > 0:
                target = random.choice(enemys_i_can_attack)
                player['act'] = ['attack', target]
            else:
                player['act'] = ['reload', 'self']
            player['madskele_attack'] = 0
            player['already_wait'] = False
            
    if player['weapon'].name == 'Мраморная колонна' and player['act'][0] == 'perekat':
        player['act'] = ['reload', 'self']

    for ids in enemys:
        target = game['players'][ids]
        if target['EXPLOSION'] == player['id']:
            if 'shieldgen' in player['skills'] and player['shieldgencd'] <= 0:
                player['act'] = ['shieldgen', player['id']]

            elif 'shield' in player['inventory']:
                player['act'] = ['shield', player['id']]

            else:
                if player['weapon'].name == 'Кувалда' and player['energy'] >= 4 and player['sokrusheniecd'] <= 0 and not player['fell']:
                    player['act'] = ['sokrush', target['id']]
                else:
                    player['act'] = ['skip', 'self']

    if player['dark_counter'] > 0:
        if not player["is_knight"]:
            if random.randint(1, 100) <= 95:
                player['act'] = ['get_calm_pvp', 'self']
            else:
                player['act'] = ['run', 'self']

    if player['team'] == 'dark' and player['controller'] == 'bot' and 'Тень крысы' in player['name'] and player['cant_die']:
        target = game['players'][random.choice(enemys)]
        player['act'] = ['attack', target['id']]
        player['dopuseditems'] = []
        player['energy'] = player['maxenergy']

    if player['team'] == 'dark' and player['controller'] == 'bot' and 'Амальгама' in player['name']:
        player['energy'] = player['maxenergy']
        player['dopuseditems'] = []
        target = game['players'][random.choice(enemys)]
        if player['weapon'].name == 'Отсутствует':
            player['act'] = ['amalgama_mutate', 'self']
            return
        elif not player['amalgama_must_mutate']:
            if player['weapon'].name == 'Огромный тесак':
                player['act'] = ['attack', target['id']]
                return
            elif player['weapon'].name == 'Теневая пушка':
                if player['dark_gun_charges'] == 0:
                    player['act'] = ['charge_dark_gun', 'self']
                else:
                    player['act'] = ['attack', target['id']]
                return
            elif player['weapon'].name == 'Пасть собаки':
                player['act'] = ['attack', target['id']]
        else:
            player['act'] = ['amalgama_mutate', 'self']

    if player['act'] == None:
        player['act'] = ['skip', 'self']
    try:
        if type(player["act"][1]) == dict:
            x = player["act"][1]["id"]
            player["act"].pop(1)
            player["act"].append(x)
    except:
        pass
        
  except:
    player['act'] = ['skip', 'self']
    #print(traceback.format_exc())
    bot.send_message(441399484, traceback.format_exc())
        
#def npcact2(game, player):
#    hitchance = gethitchance(player)
#    basehitchance = hitchance
#    acts = []
#    enemys = []
#    enemys_close = []
#    enemys_can_attack_me = []
#    enemys_i_can_attack = []
#    enemys_zombie = []
#    enemys_stunned = []
#    enemys_hitin = []
#    lowesthealth = 100
#    for ids in game['players']:
#        target = game['players'][ids]
#        if target['team'] != player['team'] and not target['dead']:
#            if target['id'] not in enemys:
#                enemys.append(target['id'])
#            if target['id'] in player['nearplayers']:
#                enemys_close.append(target['id'])
#            if target['weapon'].ranged or player['id'] in target['nearplayers']:
#                enemys_can_attack_me.append(target['id'])
#            if player['weapon'].ranged or target['id'] in player['nearplayers']:
#                enemys_i_can_attack.append(target['id'])
#            if target['zombie']:
#                enemys_zombie.append(target['id'])
#            if target['stun'] > 0:
#                enemys_stunned.append(target['id'])
#            if len(target['hitins']) > 0:
#                enemys_hitin.append(target['id'])
#            if target['hp'] < lowesthealth:
#                lowesthealth = target['hp']
#                
#    acttypes = ['attack', 'def', 'skip']
#                
#
