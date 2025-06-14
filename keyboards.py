import time

from telebot import types
import random
from gametexts import getname 
import weaponlist
import threading
import os
from pymongo import MongoClient

from config import database, database2

client = MongoClient(database2)
db=client.veganwars_rebuild
users=db.users

has_charge = []
has_bomber = []
has_necrostaff = []
has_dark_energy = []
has_miner = []
has_hell_reward = []
has_dragon_power = []
has_doom = [1134827568, 674065123]

def check_charge():
    while True:
        has_charge.clear()
        has_bomber.clear()
        has_necrostaff.clear()
        has_dark_energy.clear()
        has_miner.clear()
        has_hell_reward.clear()
        has_dragon_power.clear()
        for ids in users.find({}):
            try:
                if ids['rhinosoul']:
                    has_charge.append(ids['id'])
            except:
                pass
            try:
                if ids['EXPLOSION']:
                    has_bomber.append(ids['id'])
            except:
                pass
            try:
                if ids['staff_of_necromant']:
                    has_necrostaff.append(ids['id'])
            except:
                pass
            try:
                if ids['dark_reward']:
                    has_dark_energy.append(ids['id'])
            except:
                pass
            try:
                if ids['miner']:
                    has_miner.append(ids['id'])
            except:
                pass
            try:
                if ids['hell_reward']:
                    has_hell_reward.append(ids['id'])
            except:
                pass
            try:
                if ids['dragon_reward']:
                    has_dragon_power.append(ids['id'])
            except:
                pass

        time.sleep(900)



threading.Thread(target=check_charge).start()
  
skills = ['sniper', 'shieldgen', 'medic', 'dvuzhil', 'zombie',
          'bicepc', 'pyromancer', 'sadist', 'berserk', 'zapas', 'visor', 'protivogaz', 'narkoman',
         'vor', 'ritualist', 'navod', 'oruzh', 'necromant', 'incvizitor', 'pyrotech', 'cherep', 'alchemist',
         'ninja', 'multicast', 'lastchance', 'invoker', 'inzhener']#, 'priest']

summon_wars_skills = ['+1en', 'no_stun']
summon_wars_units = ['slime', '']

skills_classic = ['sniper', 'shieldgen', 'medic', 'dvuzhil', 'zombie',
          'bicepc_classic', 'pyromancer_classic', 'sadist', 'berserk', 'zapas', 'visor', 'protivogaz_classic', 'narkoman',
         'vor', 'ritualist', 'navod', 'oruzh', 'necromant', 'cherep_classic', 'hypnotist_classic', 'armor_classic']

blockskills = ['monk', 'autist', 'invoker', 'charge', 'bomber']
blockweapons = ['Посох Некроманта', 'Пулемет', 'One punch']

weapons = [weaponlist.Pistol, weaponlist.Baseball, weaponlist.Knife, weaponlist.Obrez,
           weaponlist.Drobovik, weaponlist.Revolver, weaponlist.Torch, weaponlist.Flamethrower,
           weaponlist.Rifle, weaponlist.Axe, weaponlist.Bulava, weaponlist.Kastet, weaponlist.Kuvalda, weaponlist.Chain,
          weaponlist.Spear, weaponlist.Saber, weaponlist.Granatomet, weaponlist.Bow, weaponlist.Claws,
          weaponlist.Saw, weaponlist.Police, weaponlist.Water,
          weaponlist.Shurikens, weaponlist.Molot, weaponlist.Shest, weaponlist.MachineGun, weaponlist.Tesak, weaponlist.FrozenBow, weaponlist.OnePunch, weaponlist.Yatagan]

weapons_classic = [weaponlist.Pistol_classic, weaponlist.Baseball_classic, weaponlist.Knife_classic, weaponlist.Obrez_classic,
           weaponlist.Drobovik_classic, weaponlist.Revolver_classic, weaponlist.Torch_classic, weaponlist.Flamethrower_classic,
           weaponlist.Rifle_classic, weaponlist.Axe_classic, weaponlist.Bulava_classic, weaponlist.Kastet_classic, weaponlist.Kuvalda_classic, weaponlist.Chain_classic,
          weaponlist.Spear_classic, weaponlist.Police_classic]

allw = [weaponlist.Pistol, weaponlist.Baseball, weaponlist.Knife, weaponlist.Obrez,
           weaponlist.Drobovik, weaponlist.Revolver, weaponlist.Torch, weaponlist.Flamethrower,
           weaponlist.Rifle, weaponlist.Axe, weaponlist.Kastet, weaponlist.Kuvalda, weaponlist.Chain,
       weaponlist.Narsil, weaponlist.Fist, weaponlist.Spear, weaponlist.BowAsgard, weaponlist.Katana, weaponlist.Saber, weaponlist.Granatomet, weaponlist.Bow,
        weaponlist.Claws, weaponlist.VirusHit, weaponlist.FireSword, weaponlist.Bite,
       weaponlist.Non, weaponlist.Bulava, weaponlist.Saw, weaponlist.Police, weaponlist.Rock, weaponlist.Sword, weaponlist.Water,
       weaponlist.Shurikens, weaponlist.VampireBite, weaponlist.DemonlordEye, weaponlist.SkeletonKingSword,
       weaponlist.Horn, weaponlist.Shield, weaponlist.Molot, weaponlist.Sword2, weaponlist.Treant_hand, weaponlist.LightSword, weaponlist.Shest,
       weaponlist.WeakSkeleSword, weaponlist.GhoulTeeth, weaponlist.MadSkeleWeapon, weaponlist.NecromantStaff_players, weaponlist.MachineGun, weaponlist.DuelRapier,
        weaponlist.MagicStaff, weaponlist.Tesak, weaponlist.FrozenBow, weaponlist.OnePunch,

        weaponlist.Pistol_classic, weaponlist.Baseball_classic, weaponlist.Knife_classic, weaponlist.Obrez_classic,
        weaponlist.Drobovik_classic, weaponlist.Revolver_classic, weaponlist.Torch_classic,
        weaponlist.Flamethrower_classic,
        weaponlist.Rifle_classic, weaponlist.Axe_classic, weaponlist.Bulava_classic, weaponlist.Kastet_classic,
        weaponlist.Kuvalda_classic, weaponlist.Chain_classic,
        weaponlist.Spear_classic, weaponlist.Police_classic,

        weaponlist.Flamethrower_narsil,
        weaponlist.Yatagan
        ]
  
def getbosskb(game, player):
    kb = types.InlineKeyboardMarkup()
    bosses = ['vampire', 'skeletonking', 'demonlord']
    for ids in bosses:
        kb.add(types.InlineKeyboardButton(text = getname(ids), callback_data = 'selectboss?'+str(game['id'])+'?'+ids),
              types.InlineKeyboardButton(text = 'Информация', callback_data = 'getbossinfo?'+ids))
    return kb
  
def getskillkb(game, player):
    kb = types.InlineKeyboardMarkup()
    s = []
    allys = []
    for ids in game['players']:
        target = game['players'][ids]
        if target['id'] != player['id'] and target['team'] == player['team']:
            allys.append(target['id'])
    skills2 = skills.copy()
    if not game['tournier']:
        if player['id'] in has_charge:
            skills2.append('charge')
    event_explosion = False
    if event_explosion:
        skills2.append('bomber')
    if player['id'] in has_dark_energy:
            allow_de = False
            x = 'dark_energy'
            can_pick_de = True
            if game['dungeon']:
                if game['dungeon_type'] == 'rhino':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_charge:
                            can_pick_de = False
                            break
                    if can_pick_de and 'dark_energy' not in player['skills']:
                        allow_de = True
                if game['dungeon_type'] == 'dragon':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_dragon_power:
                            can_pick_de = False
                            break
                    if can_pick_de and 'dark_energy' not in player['skills']:
                        allow_de = True
                if game['dungeon_type'] == 'ghoul':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids][
                            'id'] not in has_necrostaff:
                            can_pick_de = False
                            break

                    if can_pick_de and 'dark_energy' not in player['skills']:
                        allow_de = True
            else:
                if 'dark_energy' not in player['skills'] and not game['tournier'] and not game['dungeon']:
                    allow_de = True
            if allow_de:
                skills2.append('dark_energy')
    allow_dp = False
    if player['id'] in has_dragon_power:
            allow_dp = False
            x = 'dragon_power'
            can_pick_dp = True
            if game['dungeon']:
                if game['dungeon_type'] == 'rhino':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_charge:
                            can_pick_dp = False
                            break
                    if can_pick_dp and 'dragon_power' not in player['skills']:
                        allow_dp = True
                if game['dungeon_type'] == 'ghoul':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids][
                            'id'] not in has_necrostaff:
                            can_pick_dp = False
                            break
                    if can_pick_dp and 'dragon_power' not in player['skills']:
                        allow_dp = True
                if game['dungeon_type'] == 'dragon':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_dragon_power:
                            can_pick_dp = False
                            break
                    if can_pick_dp and 'dragon_power' not in player['skills']:
                        allow_dp = True
            else:
                if 'dragon_power' not in player['skills'] and not game['tournier'] and not game['dungeon']:
                    allow_dp = True
            if allow_dp:
                skills2.append('dragon_power')

    if player['id'] in has_hell_reward:
            allow_hr = False
            x = 'add_tentacles'
            can_pick_hr = True
            if game['dungeon']:
                if game['dungeon_type'] == 'rhino':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_charge:
                            can_pick_hr = False
                            break
                    if can_pick_hr and 'add_tentacles' not in player['skills']:
                        allow_hr = True
                if game['dungeon_type'] == 'ghoul':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids][
                            'id'] not in has_necrostaff:
                            can_pick_hr = False
                            break
                    if can_pick_hr and 'add_tentacles' not in player['skills']:
                        allow_hr = True
                if game['dungeon_type'] == 'dragon':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids][
                            'id'] not in has_dragon_power:
                            can_pick_hr = False
                            break
                    if can_pick_hr and 'add_tentacles' not in player['skills']:
                        allow_hr = True
            else:
                if 'add_tentacles' not in player['skills'] and not game['tournier'] and not game['dungeon']:
                    allow_hr = True
            if allow_hr:
                skills2.append('add_tentacles')

    if player['id'] == 1134827568:
        if not game['tournier'] and not game['dungeon']:
            skills2.append('demon')
    if game['testequipgame']:
        for ids in skills2:
            x = ids
            kb.add(types.InlineKeyboardButton(text=getname(x),
                   callback_data='selectskill?' + str(game['id']) + '?' + str(x)+"?te%"),
                   types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
    if game['testequipgame_tournier']:
        for ids in skills2:
            x = ids
            kb.add(types.InlineKeyboardButton(text=getname(x),
                   callback_data='selectskill?' + str(game['id']) + '?' + str(x)+"?te%"),
                   types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
    else:
        if game['classic_game']:
            skills2 = skills_classic.copy()
        while len(s) < 5:
            x = random.choice(skills2)
            notallowed = True
            while x in s or x in player['skills'] or notallowed:
                notallowed = False
                x = random.choice(skills2)
                if game['dungeon'] and game['dungeon_type'] == 'dark' and game['dungeonlvl'] == 1 and 'medic' not in player['skills'] and 'medic' not in s and random.randint(1, 100) <= 7:
                    x = 'medic'
                if x in ['bicepc', 'berserk', 'charge', 'multicast', 'bicepc_classic'] and player['weapon'].ranged:
                    notallowed = True
                if x in ['invoker', 'bloodseeker', 'bomber', 'inzhener'] and game['dungeon']:
                    notallowed = True
                if x in ['necromant'] and game['dungeon'] and game['dungeon_type'] == 'dark':
                    notallowed = True
                #if x in ['robot'] and player['weapon'].name in ['Дробовик', 'Обрез']:
                #    notallowed = True
                if x in ['sniper', 'sniper_classic'] and not player['weapon'].ranged:
                    notallowed = True
                if x in ['navod', 'defer'] and len(allys) == 0:
                    notallowed = True
                if x in ['necromant'] and len(allys) == 0:
                    #if player['weapon'].name != 'Посох Некроманта':
                        notallowed = True
                if not game['classic_game']:
                    if x in ['sniper', 'visor', 'sniper_classic', 'visor_classic'] and player['weapon'].name in ['Дробовик']:
                        notallowed = True
                if x in blockskills and game['tournier']:
                    notallowed = True
            event = True
            if event:
                if player['id'] in has_dragon_power and allow_dp and random.randint(1, 100) <= 10 and "dragon_power" not in s:
                    x = "dragon_power"
            kb.add(types.InlineKeyboardButton(text = getname(x), callback_data = 'selectskill?'+str(game['id'])+'?'+str(x)),
                  types.InlineKeyboardButton(text = 'Информация', callback_data = 'getskillinfo?'+str(x)))
            s.append(x)
        if player['id'] in has_dark_energy and game['dungeon_type'] == 'hell' and game['dungeonlvl'] == 3:
            x = 'dark_energy'
            kb.add(types.InlineKeyboardButton(text=getname(x),
                                              callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                   types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
        if player['id'] in has_charge and game['dungeon_type'] == 'hell' and game['dungeonlvl'] == 3 and 'charge' not in s:
            x = 'charge'
            kb.add(types.InlineKeyboardButton(text=getname(x),
                                              callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                   types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
    if not game['classic_game']:
        if player['id'] == 253478906:
            x = 'elmo'
            if 'elmo' not in player['skills'] and not game['tournier']:
                kb.add(types.InlineKeyboardButton(text = getname(x), callback_data = 'selectskill?'+str(game['id'])+'?'+str(x)),
                  types.InlineKeyboardButton(text = 'Информация', callback_data = 'getskillinfo?'+str(x)))
        #if player['id'] == 1134827568:
        #    x = 'demon'
        #    if 'demon' not in player['skills'] and not game['tournier']:
        #        if game['dungeonlvl'] <= 1:
        #            kb.add(types.InlineKeyboardButton(text = getname(x), callback_data = 'selectskill?'+str(game['id'])+'?'+str(x)),
        #            types.InlineKeyboardButton(text = 'Информация', callback_data = 'getskillinfo?'+str(x)))
        if player['id'] in has_bomber:
            x = 'bomber'
            can_pick_bomber = True
            if game['dungeon']:
                if game['dungeon_type'] == 'rhino':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_charge:
                            can_pick_bomber = False
                            break
                    if can_pick_bomber and 'bomber' not in player['skills']:
                        kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                            types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
                if game['dungeon_type'] == 'ghoul':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_necrostaff:
                            can_pick_bomber = False
                            break
                    if can_pick_bomber and 'bomber' not in player['skills']:
                        kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                            types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
            else:
                if 'bomber' not in player['skills'] and not game['tournier'] and not game['dungeon']:
                    kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                           types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))


        if player['id'] in has_miner:
            x = 'miner'
            can_pick_miner = True
            if game['dungeon']:
                if game['dungeon_type'] == 'rhino':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_charge:
                            can_pick_miner = False
                            break
                    if can_pick_miner and 'miner' not in player['skills']:
                        kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                            types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
                if game['dungeon_type'] == 'ghoul':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_necrostaff:
                            can_pick_miner = False
                            break
                    if can_pick_miner and 'miner' not in player['skills']:
                        kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                            types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
            else:
                if 'miner' not in player['skills'] and not game['tournier'] and not game['dungeon']:
                    kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                           types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))

        if player['id'] in has_doom:
            x = 'doom'
            can_pick_doom = True
            if game['dungeon']:
                if game['dungeon_type'] == 'rhino':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_charge:
                            can_pick_doom = False
                            break
                    if can_pick_doom and 'doom' not in player['skills']:
                        kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                            types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
                if game['dungeon_type'] == 'ghoul':
                    for ids in game['players']:
                        if game['players'][ids]['controller'] != 'bot' and game['players'][ids]['id'] not in has_necrostaff:
                            can_pick_doom = False
                            break
                    if can_pick_doom and 'doom' not in player['skills']:
                        kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                            types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))
            else:
                if 'doom' not in player['skills'] and not game['tournier'] and not game['dungeon']:
                    kb.add(types.InlineKeyboardButton(text=getname(x),
                                                      callback_data='selectskill?' + str(game['id']) + '?' + str(x)),
                           types.InlineKeyboardButton(text='Информация', callback_data='getskillinfo?' + str(x)))


    #if player['id'] in has_charge:
     #   x = 'charge'
    #    if x not in player['skills'] and not player['weapon'].ranged:
    #        kb.add(types.InlineKeyboardButton(text = getname(x), callback_data = 'selectskill?'+str(game['id'])+'?'+str(x)),
   #           types.InlineKeyboardButton(text = 'Информация', callback_data = 'getskillinfo?'+str(x)))
    if player['team'] == game['gl']:
        if not game['g']:
            x = 'gurren'
            kb.add(types.InlineKeyboardButton(text = 'ГУРРЕН', callback_data = 'selectskill?'+str(game['id'])+'?'+str(x)),
                types.InlineKeyboardButton(text = 'Информация', callback_data = 'getskillinfo?'+str(x)))
            game['g'] = True
        else:
            x = 'lagann'
            kb.add(types.InlineKeyboardButton(text = 'ЛАГАНН', callback_data = 'selectskill?'+str(game['id'])+'?'+str(x)),
                types.InlineKeyboardButton(text = 'Информация', callback_data = 'getskillinfo?'+str(x)))
    
    return kb
  
def getoruzhkb(game, player = None):
    #global testweapon
    kb = types.InlineKeyboardMarkup()
    w = []
    weaponlen = 4
    if game['classic_game']:
        weaponlen = 3
    while len(w) < weaponlen:
        notallowed = True
        if not game['classic_game']:
            x = random.choice(weapons)()
        else:
            x = random.choice(weapons_classic)()
        #if x.name == 'Дробовик' and player['id'] == 1134827568:
        #    notallowed = True
        while x.id in w or x.id == player['weapon'].id or notallowed:
            notallowed = False
            if not game['classic_game']:
                x = random.choice(weapons)()
            else:
                x = random.choice(weapons_classic)()
            #if x.name == 'Дробовик' and player['id'] == 1134827568:
            #    notallowed = True
            if x.name in blockweapons and game['tournier']:
                notallowed = True
            if x.name in ['One punch']:
                notallowed = True
            if x.name in ['Пулемет', 'One punch'] and game['dungeon']:
                notallowed = True
            if x.name in ['Гранатомет'] and len(game['players']) > 2 and not game['dungeon']:
                notallowed = True
        kb.add(types.InlineKeyboardButton(text = x.name, callback_data = 'selectoruzhweapon?'+str(game['id'])+'?'+str(x.id)))
        w.append(x.id)
    return kb
  
def getfightkb(game, player):
    kb = types.InlineKeyboardMarkup()
    frozen_buttons = []
    for ids in player['frozen_buttons']:
        frozen_buttons.append(ids[0])
    if "attack" not in frozen_buttons:
        attacktext = 'Атака'
        attackcalldata = 'fightact?'+str(game['id'])+'?attackselect'
    else:
        attacktext = '(🔒)Атака'
        attackcalldata = 'fightact?' + str(game['id']) + '?frozen_act'
    if "perekat" not in frozen_buttons:
        perekattext = 'Перекат'
        perekatcalldata = 'fightact?'+str(game['id'])+'?perekat'
    else:
        perekattext = '(🔒)Перекат'
        perekatcalldata = 'fightact?' + str(game['id']) + '?frozen_act'
    if "addition" not in frozen_buttons and len(player['doomedskills']) == 0:
        additiontext = 'Дополнительно'
        additioncalldata = 'fightact?'+str(game['id'])+'?addition'
    else:
        additiontext = '(🔒)Дополнительно'
        additioncalldata = 'fightact?' + str(game['id']) + '?frozen_act'
    if 'robot' not in player['skills']:
        if "reload" not in frozen_buttons:
            reloadtext = 'Перезарядка'
            reloadcalldata = 'fightact?' + str(game['id']) + '?reload'
        else:
            reloadtext = '(🔒)Перезарядка'
            reloadcalldata = 'fightact?' + str(game['id']) + '?frozen_act'
        if player['weapon'].name == 'Дробовик' and player['drobovik_charges'] <= 0:
            if not player['fell']:
                
                kb.add(types.InlineKeyboardButton(text=reloadtext, callback_data=reloadcalldata))
            else:
                kb.add(types.InlineKeyboardButton(text='Подняться',
                                                  callback_data='fightact?' + str(game['id']) + '?standup'),
                       types.InlineKeyboardButton(text=reloadtext,
                                                  callback_data=reloadcalldata))
        else:
            if not player['fell']:
                if game['classic_game']:
                    if player['energy'] > 0:
                        kb.add(types.InlineKeyboardButton(text=attacktext, callback_data=attackcalldata),
                               types.InlineKeyboardButton(text=reloadtext, callback_data=reloadcalldata))
                    else:
                        kb.add(types.InlineKeyboardButton(text=reloadtext, callback_data=reloadcalldata))
                else:
                    kb.add(types.InlineKeyboardButton(text = attacktext, callback_data = attackcalldata),
                        types.InlineKeyboardButton(text = reloadtext, callback_data = reloadcalldata))
            else:
                kb.add(types.InlineKeyboardButton(text = 'Подняться', callback_data = 'fightact?'+str(game['id'])+'?standup'),
                    types.InlineKeyboardButton(text = reloadtext, callback_data = reloadcalldata))
    else:
        kb.add(types.InlineKeyboardButton(text = attacktext, callback_data = attackcalldata),
           types.InlineKeyboardButton(text = 'Охлаждение', callback_data = 'fightact?'+str(game['id'])+'?reload'))
    if player['droppedweapon'] != None:
        kb.add(types.InlineKeyboardButton(text = 'Поднять оружие', callback_data = 'fightact?'+str(game['id'])+'?pickupweapon'))
    if player['weapon'].name == 'Гранатомет':
        kb.add(types.InlineKeyboardButton(text = 'Граната: '+getname(player['grenade']), callback_data = 'fightact?'+str(game['id'])+'?grenadeselect'))
    if player['perekatcd'] <= 0 and not player['fell']:
        kb.add(types.InlineKeyboardButton(text = perekattext, callback_data = perekatcalldata),
          types.InlineKeyboardButton(text = 'Инфо', callback_data = 'fightact?'+str(game['id'])+'?info'))
    else:
        kb.add(types.InlineKeyboardButton(text = 'Инфо', callback_data = 'fightact?'+str(game['id'])+'?info'))
    
    kb.add(types.InlineKeyboardButton(text = additiontext, callback_data = additioncalldata))
    for ids in game['players']:
        target = game['players'][ids]
        if target['team'] != player['team'] and (target['id'] not in player['nearplayers'] or "dragon_power" in target["skills"] or target["is_dragon"]):
            kb.add(types.InlineKeyboardButton(text = 'Подойти', callback_data = 'fightact?'+str(game['id'])+'?walk'))
            break
    if player['fireticks'] > 0:
        text = 'Потушиться'
    else:
        if 'autist' not in player['skills']:
            text = 'Пропустить'
        else:
            text = 'Тупить'
    skipcalldata = 'fightact?'+str(game['id'])+'?skip'
    if 'skip' in frozen_buttons:
        text = "(🔒)"+text
        skipcalldata = 'fightact?' + str(game['id']) + '?frozen_act'
    kb.add(types.InlineKeyboardButton(text = text, callback_data = skipcalldata))
    
    if player['lasthit'] > 0:
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text = 'Умереть', callback_data = 'fightact?'+str(game['id'])+'?die'))

    if player['darkness_sleep']:
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Увернуться вправо', callback_data='fightact?' + str(game['id']) + '?perekat_right'),
               types.InlineKeyboardButton(text='Увернуться влево', callback_data='fightact?' + str(game['id']) + '?perekat_left'))

    return kb

def getdrinkname(x):
    if x == 'vodka':
        return 'Водка'
    return 'Неизвестно'

def getfoodname(x):
    if x == 'goose':
        return 'Жареный гусь'
    return 'Неизвестно'

def getbarkb(game, player):
    kb = types.InlineKeyboardMarkup()

    ordertext = 'Сделать заказ'
    ordercalldata = 'fightact?' + str(game['id']) + '?orderselect'

    drinktext = 'Выпить ('+getdrinkname(player['napitok'])+')'
    drinkcalldata = 'fightact?' + str(game['id']) + '?drink'

    eattext = 'Съесть ('+getfoodname(player['food'])+')'
    eatcalldata = 'fightact?' + str(game['id']) + '?eat'

    throwstakantext = 'Швырнуть пустой стакан'
    throwstakancalldata = 'fightact?' + str(game['id']) + '?throwstakan'


    kb.add(types.InlineKeyboardButton(text=attacktext, callback_data=attackcalldata),
                           types.InlineKeyboardButton(text=reloadtext, callback_data=reloadcalldata))

    kb.add(types.InlineKeyboardButton(text=perekattext, callback_data=perekatcalldata),
               types.InlineKeyboardButton(text='Инфо', callback_data='fightact?' + str(game['id']) + '?info'))


    kb.add(types.InlineKeyboardButton(text=additiontext, callback_data=additioncalldata))
    #for ids in game['players']:
    #    target = game['players'][ids]
    #    if target['team'] != player['team'] and target['id'] not in player['nearplayers']:
    #        kb.add(types.InlineKeyboardButton(text='Подойти', callback_data='fightact?' + str(game['id']) + '?walk'))
    #        break

    kb.add(types.InlineKeyboardButton(text=text, callback_data=skipcalldata))

    return kb

def getdarkkb(game, player):
    kb = types.InlineKeyboardMarkup()
    if game['dungeon']:
        seetext = 'БЕЖАТЬ'
    else:
        if 'dark_energy' in player['skills']:
            seetext = 'БЕЖАТЬ'
        else:
            seetext = 'БЕЖАТЬ'
    kb.add(types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'),
               types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'))
    if player['perekatcd'] <= 0 and not player['fell']:
        kb.add(types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'),
               types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'))
    else:
        kb.add(types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'))

    kb.add(types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'))
    for ids in game['players']:
        target = game['players'][ids]
        if target['team'] != player['team'] and target['id'] not in player['nearplayers']:
            kb.add(types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'))
            break
    if player['fireticks'] > 0:
        text = 'Потушиться'
    else:
        if 'autist' not in player['skills']:
            text = 'Пропустить'
        else:
            text = 'Тупить'
    kb.add(types.InlineKeyboardButton(text=seetext, callback_data='fightact?' + str(game['id']) + '?run'))

    if player['lasthit'] > 0:
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Умереть', callback_data='fightact?' + str(game['id']) + '?die'))

    return kb

def getitemskb(game, player):
    itemlist = ['grenade', 'adrenaline', 'shield', 'flash', 'knife', 'molotov', 'dzet', 'hitin']
    kb = types.InlineKeyboardMarkup()
    for ids in itemlist:
        if ids not in player['inventory']:
            kb.add(types.InlineKeyboardButton(text = getname(ids), callback_data='selectitem?'+str(game['id'])+'?'+ids))
    return kb
  
def gettargetkb(game, player, calldata, targettype = 'enemy', sniper = False, only_far=False):
    kb = types.InlineKeyboardMarkup()
    for ids in game['players']:
        target = game['players'][ids]
        if target['dead']:
            if targettype == 'deadally':
                if target['team'] == player['team']:
                    kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))
            elif targettype == 'notblowndead':
                if not target['blown']:
                    kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))
            else:
                continue
        if target['burrowtarget'] != None:
            continue
        if targettype == 'enemy':
            if target['team'] != player['team']:
                if calldata == 'attack':
                    em = ""
                    if target["hp"] == 1 and player["weapon"].name == "Катана":
                        em = "㊙️|"
                    if not player['weapon'].ranged:
                        if player['weapon'].name == 'Копье Нарсил':
                            allowthrow = False
                            if player['energy'] >= 3 and player['narsilcd'] <= 0:
                                allowthrow = True
                            allowhit = False
                            if target['id'] in player['nearplayers']:
                                allowhit = True
                            nkb = []
                            if allowhit:
                                nkb.append(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))
                            if allowthrow:
                                nkb.append(types.InlineKeyboardButton(text = 'Метнуть', callback_data = 'fightact?'+str(game['id'])+'?'+'narsil'+'?'+str(target['id'])))
                            kb.add(*nkb)

                        else:
                            if target['id'] in player['nearplayers']:
                                if player['weapon'].name == 'Кувалда' and player['sokrusheniecd'] <= 0 and player['energy'] >= 4:
                                    kb.add(types.InlineKeyboardButton(text = em+target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])),
                                    types.InlineKeyboardButton(text = 'Сокрушить', callback_data = 'fightact?'+str(game['id'])+'?'+'sokrush'+'?'+str(target['id'])))

                                elif player['weapon'].name == 'Молот' and player['molotcd'] <= 0 and player['energy'] >= 4:
                                    kb.add(types.InlineKeyboardButton(text = em+target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])),
                                    types.InlineKeyboardButton(text = 'Точный удар', callback_data = 'fightact?'+str(game['id'])+'?'+'truestrike'+'?'+str(target['id'])))

                                            
                                elif player['weapon'].name == 'Цепь' and player['chaincd'] <= 0:
                                    kb.add(types.InlineKeyboardButton(text = em+target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])),
                                    types.InlineKeyboardButton(text = 'Выбить оружие', callback_data = 'fightact?'+str(game['id'])+'?'+'chain'+'?'+str(target['id'])))

                                #elif player['weapon'].name == 'Катана' and target['hp'] <= 1 and player['energy'] >= 5:
                                #    kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])),
                                #    types.InlineKeyboardButton(text = 'Казнь', callback_data = 'fightact?'+str(game['id'])+'?'+'execution'+'?'+str(target['id'])))

                                else:
                                    kb.add(types.InlineKeyboardButton(text = em+target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))

                    else:
                        if not sniper:
                            obrezz = False
                            try:
                                if player['weapon'].lvl == 1 or player['weapon'].lvl == 2 or player['weapon'].lvl == 3 or player['weapon'].lvl == 4:
                                    obrezz = True
                            except:
                                pass
                            if player['weapon'].name == 'Лук' and player['firearrowcd'] <= 0:
                                kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])), 
                                types.InlineKeyboardButton(text = 'Огненная стрела', callback_data = 'fightact?'+str(game['id'])+'?'+'firearrow'+'?'+str(target['id'])))

                            elif player['weapon'].name == 'Обрез' and player['obrezcd'] <= 0 and obrezz:
                                kb.add(types.InlineKeyboardButton(text=target['name'], callback_data='fightact?' + str(game['id']) + '?' + calldata + '?' + str(target['id'])),
                                       types.InlineKeyboardButton(text='Мощный выстрел',callback_data='fightact?' + str(game['id']) + '?' + 'strongshot' + '?' + str(target['id'])))
                            elif player['weapon'].name == 'Пулемет' and player['machinegun_charges'] < 4:
                                pass
                            else:
                                kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))

                        else:
                            if game['classic_game']:
                                if player['maintarget'] != None and player['maintarget']['target'] == target['id'] and player['maintarget']['power'] >= 2:
                                    kb.add(types.InlineKeyboardButton(text=target['name'],
                                                                      callback_data='fightact?' + str(
                                                                          game['id']) + '?' + calldata + '?' + str(
                                                                          target['id'])))
                                else:
                                    kb.add(types.InlineKeyboardButton(text=target['name'],
                                                                      callback_data='fightact?' + str(
                                                                          game['id']) + '?' + calldata + '?' + str(
                                                                          target['id'])),
                                           types.InlineKeyboardButton(text='Выцелить', callback_data='fightact?' + str(
                                               game['id']) + '?' + 'pricel' + '?' + str(target['id'])))
                            else:
                                kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])),
                                types.InlineKeyboardButton(text = 'Выцелить', callback_data = 'fightact?'+str(game['id'])+'?'+'pricel'+'?'+str(target['id'])))

                else:
                    if only_far and target["id"] in player["nearplayers"]:
                        pass
                    else:
                        kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))

        elif targettype == 'ally':
            if calldata == 'stimulator' and game['dungeon'] and game['dungeon_type'] == 'dark' and game['dungeonlvl'] == 1:
                kb.add(types.InlineKeyboardButton(text=target['name'], callback_data='fightact?' + str(game['id']) + '?' + calldata + '?' + str(target['id'])))
            else:
                if target['team'] == player['team']:
                    kb.add(types.InlineKeyboardButton(text = target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))
        elif targettype == 'all':
            if target['team'] != player['team']:
                doptext = '(Враг) '
            else:
                doptext = '(Союзник) '
            kb.add(types.InlineKeyboardButton(text = doptext+target['name'], callback_data = 'fightact?'+str(game['id'])+'?'+calldata+'?'+str(target['id'])))

    if calldata == 'attack':
        if player['weapon'].name in ['Копье', 'Копье Нарсил'] and player['spearcd'] <= 0 and player['energy'] >= 1:
            kb.add(types.InlineKeyboardButton(text = 'Контратака', callback_data = 'fightact?'+str(game['id'])+'?'+'counterattack'))
        elif player['weapon'].name in ['Посох Некроманта'] and player['necrostaffabilitycd'] <= 0 and player['can_summon_zombie']:
            kb.add(types.InlineKeyboardButton(text = '💀|Поднять мертвеца', callback_data = 'fightact?'+str(game['id'])+'?'+'necrostaffability'))
        elif player['weapon'].name in ['Лук Асгард'] and (player['energy'] >= 5 or player['energy'] >= 1+(player['bowcharge'])) and player['bowcharge'] < 3:
            kb.add(types.InlineKeyboardButton(text = 'Натянуть', callback_data = 'fightact?'+str(game['id'])+'?'+'chargebow'))
        elif player['weapon'].name == 'Сабля' and player['parrycd'] <= 0:
            kb.add(types.InlineKeyboardButton(text = 'Парировать', callback_data = 'fightact?'+str(game['id'])+'?'+'parryselect'))
        elif player['weapon'].name == 'Шест' and player['shestcd'] <= 0:
            kb.add(types.InlineKeyboardButton(text = 'Сбить с ног', callback_data = 'fightact?'+str(game['id'])+'?'+'hitdownselect'))
        elif player['weapon'].name == 'Стальные когти' and player['clawscd'] <= 0:# and not (player['weapon'].lvl == 4 and player['weapon'].modification == 1):
            if player['claws']:
                kb.add(types.InlineKeyboardButton(text = 'Спрятать когти', callback_data = 'fightact?'+str(game['id'])+'?'+'clawsoff'))
            else:
                kb.add(types.InlineKeyboardButton(text = 'Выдвинуть когти', callback_data = 'fightact?'+str(game['id'])+'?'+'clawson'))
        elif player['weapon'].name == 'Сюрикены':
            kb.add(types.InlineKeyboardButton(text = 'Бросок: '+str(player['shurikenstothrow'])+' сюрикен(а)', callback_data = 'fightact?'+str(game['id'])+'?'+'shurikenamount'))
        elif player['weapon'].name == 'Щит':
            kb.add(types.InlineKeyboardButton(text = 'Блокировать ('+str(player['shieldarmor'])+')', callback_data = 'fightact?'+str(game['id'])+'?'+'blockshieldweapon'))
        elif player['weapon'].name == 'Пулемет':
            kb.add(types.InlineKeyboardButton(text='Зарядить пулемет (' + str(player['machinegun_charges']) + ')', callback_data='fightact?' + str(game['id']) + '?' + 'machinegun_charge'))
        elif player['weapon'].name == 'Волшебный посох' and player['energy'] >= 2:
            kb.add(types.InlineKeyboardButton(text='Восстановить ману',
                                              callback_data='fightact?' + str(game['id']) + '?' + 'invoker_charge'))

        elif player['weapon'].name == 'Огнемет Нарсил' and player['energy'] >= 2:
            kb.add(types.InlineKeyboardButton(text='Взорвать огнемет',
                                              callback_data='fightact?' + str(game['id']) + '?' + 'blow_flamethrower'))

        if 'charge' in player['skills'] and player['chargecd'] <= 0:
            kb.add(types.InlineKeyboardButton(text = 'Рывок', callback_data = 'fightact?'+str(game['id'])+'?'+'chargeselect'))
        if 'multicast' in player['skills'] and player['multicastcd'] <= 0:
            kb.add(types.InlineKeyboardButton(text = 'Концентрация: x'+str(player['multicast']), callback_data = 'fightact?'+str(game['id'])+'?'+'multicastselect'))
        if 'dragon_power' in player['skills'] and player['dragon_fireballcd'] <= 0 and player["energy"] >= 3:
            kb.add(types.InlineKeyboardButton(text='Огненный шар',
                                              callback_data='fightact?' + str(game['id']) + '?' + 'dragon_fireballselect'))


      
    kb.add(types.InlineKeyboardButton(text = 'Главное меню', callback_data = 'fightact?'+str(game['id'])+'?'+'mainmenu'))
    return kb
  
def getadditionkb(game, player):
    kb = types.InlineKeyboardMarkup()
    if 'robot' in player['skills']:
        player['energy'] = player['hp']
    if ('shieldgen' in player['skills'] or 'shieldgen?1' in player['skills'] or \
            'shieldgen?2' in player['skills'] or 'shieldgen?3' in player['skills']) \
            and player['shieldgencd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Щит|генератор', callback_data = 'fightact?'+str(game['id'])+'?'+'shieldgenselect'))
    if ('hypnotist' in player['skills'] or 'hypnotist_classic' in player['skills']) and player['hypnotistcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Гипноз', callback_data = 'fightact?'+str(game['id'])+'?'+'hypnotistselect'))
    if 'stimulator' in player['inventory']:
        amount = player['inventory'].count('stimulator')
        kb.add(types.InlineKeyboardButton(text = 'Стимулятор ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'stimulatorselect'))
    if 'shield' in player['inventory']:
        amount = player['inventory'].count('shield')
        kb.add(types.InlineKeyboardButton(text = 'Щит ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'shieldselect'))
    if 'grenade' in player['inventory'] and player['energy'] >= 2 and not player['fell']:
        amount = player['inventory'].count('grenade')
        kb.add(types.InlineKeyboardButton(text = 'Граната ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'grenade'))
    if 'molotov' in player['inventory'] and player['energy'] >= 2 and not player['fell']:
        amount = player['inventory'].count('molotov')
        kb.add(types.InlineKeyboardButton(text = 'Коктейль Молотова ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'molotov'))
    if 'flash' in player['inventory']:
        amount = player['inventory'].count('flash')
        kb.add(types.InlineKeyboardButton(text = 'Световая граната ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'flashselect'))
    if 'visor' in player['skills'] and player['visorcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Визор', callback_data = 'fightact?'+str(game['id'])+'?'+'visorselect'))
    if "dragon_power" in player["skills"] and player["wing_attackcd"] <= 0 and player["energy"] >= 2:
        kb.add(
            types.InlineKeyboardButton(text='Взмах крыльями', callback_data='fightact?' + str(game['id']) + '?' + 'wing_attack'))
    if 'knife' in player['inventory'] and not player['fell']:
        amount = player['inventory'].count('knife')
        energy = player['energy']
        if not game['classic_game']:
            if 'sniper' in player['skills']:
                energy += 2
            if 'visor' in player['skills']:
                energy += 1
            if 'vor' in player['skills'] or 'vor?2' in player['skills'] or 'vor?3' in player['skills']:
                energy += 1
            if 'narkoman' in player['skills']:
                energy -= 1
            if 'narkoman?1' in player['skills']:
                energy -= 2
            if 'narkoman?2' in player['skills']:
                energy -= 1
            if 'narkoman?3' in player['skills']:
                energy -= 1
        naturalchance = 40 + (energy*10)
        if naturalchance > 100:
            naturalchance = 100
        kb.add(types.InlineKeyboardButton(text = 'Метательный нож ('+str(amount)+') ('+str(naturalchance)+'%)', callback_data = 'fightact?'+str(game['id'])+'?'+'knifeselect'))
    if 'adrenaline' in player['inventory']:
        amount = player['inventory'].count('adrenaline')
        kb.add(types.InlineKeyboardButton(text = 'Адреналин ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'adrenalineselect'))
    if 'dzet' in player['inventory']:
        amount = player['inventory'].count('dzet')
        kb.add(types.InlineKeyboardButton(text = 'Джет ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'dzetselect'))
    if 'hitin' in player['inventory']:
        amount = player['inventory'].count('hitin')
        kb.add(types.InlineKeyboardButton(text = 'Хитин ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'hitinselect'))
    if 'madpotion' in player['inventory']:
        amount = player['inventory'].count('madpotion')
        kb.add(types.InlineKeyboardButton(text = 'Сыворотка бешенсва ('+str(amount)+')', callback_data = 'fightact?'+str(game['id'])+'?'+'madpotionselect'))
    if ('vor' in player['skills'] or 'vor?1' in player['skills'] or 'vor?2' in player['skills'] or 'vor?3' in player['skills'] or 'vor_classic' in player['skills']) and player['vorcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Украсть предмет', callback_data = 'fightact?'+str(game['id'])+'?'+'vorselect'))
    if 'ritualist' in player['skills'] and player['ritualistamount'] >= 1:
        kb.add(types.InlineKeyboardButton(text = 'Ритуал: начало', callback_data = 'fightact?'+str(game['id'])+'?'+'ritualselect'))
    if player['ritual_ability']:
        kb.add(types.InlineKeyboardButton(text = 'Ритуал: молния', callback_data = 'fightact?'+str(game['id'])+'?'+'lightingselect'))
    if 'navod' in player['skills'] and player['navodcd'] <= 0 and not player['fell']:
        kb.add(types.InlineKeyboardButton(text = 'Наводчик', callback_data = 'fightact?'+str(game['id'])+'?'+'navodselect'))
    if 'oruzh' in player['skills'] and player['changeweaponcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Сменить оружие', callback_data = 'fightact?'+str(game['id'])+'?'+'changeweapon'))
    deads = []
    bdeads = []
    for ids in game['players']:
        target = game['players'][ids]
        if target['dead'] and target['team'] == player['team']:
            deads.append(target['id'])
        if target['dead'] and not target['blown']:
            bdeads.append(target['id'])
    if 'necromant' in player['skills'] and len(deads) > 0:
        kb.add(types.InlineKeyboardButton(text = 'Поднять зомби', callback_data = 'fightact?'+str(game['id'])+'?'+'zombieupselect'))
    if 'warlock' in player['skills'] and len(bdeads) > 0:
        kb.add(types.InlineKeyboardButton(text = 'Взорвать труп', callback_data = 'fightact?'+str(game['id'])+'?'+'blowselect'))
    if ('incvizitor' in player['skills'] or 'incvizitor?1' in player['skills'] or 'incvizitor?2' in player['skills'] or 'incvizitor?3' in player['skills'])\
            and player['incvizitorcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Направить взор небес', callback_data = 'fightact?'+str(game['id'])+'?'+'incvizitorselect'))
    if 'illusionist' in player['skills'] and player['illusioncd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Создать иллюзию', callback_data = 'fightact?'+str(game['id'])+'?'+'illusion'))   
    if 'demon' in player['skills'] and player['demoncd'] <= 0 and player['energy'] >= 3:
        kb.add(types.InlineKeyboardButton(text = 'Кража жизни', callback_data = 'fightact?'+str(game['id'])+'?'+'demonselect'))
    if 'bomb' in player['inventory'] and ('pyrotech' in player['skills'] or 'pyrotech?1' in player['skills'] or 'pyrotech?2' in player['skills'] or \
                                          'pyrotech?3' in player['skills']):
        kb.add(types.InlineKeyboardButton(text = 'Улучшить бомбу', callback_data = 'fightact?'+str(game['id'])+'?'+'pyrotechcharge'))   
    if 'bomb' in player['inventory'] and player['energy'] >= 2 and not player['fell']:
        bdmg = 1+(player['bombcharge']*2)
        if 'pyrotech?1' in player['skills']:
            bdmg = 1 + (player['bombcharge'] * 1)
        if 'pyrotech?2' in player['skills']:
            bdmg = 1 + (player['bombcharge'] * 2)
        if 'pyrotech?3' in player['skills']:
            bdmg = 1 + (player['bombcharge'] * 3)
        kb.add(types.InlineKeyboardButton(text = 'Бросить бомбу ('+str(bdmg)+' урона)', callback_data = 'fightact?'+str(game['id'])+'?'+'pyrotechselect'))
    if player['weapon'].name == 'Водомет' and player['watershieldcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Водяной щит', callback_data = 'fightact?'+str(game['id'])+'?'+'watershieldselect'))   
    if 'monk' in player['skills'] and player['meditationcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Медитация', callback_data = 'fightact?'+str(game['id'])+'?'+'meditationselect'))   
    if 'lastchance' in player['skills']:
        kb.add(types.InlineKeyboardButton(text = 'Последний удар', callback_data = 'fightact?'+str(game['id'])+'?'+'lastchance'))   
    if 'priest' in player['skills'] and player['priestcd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Освятить оружие', callback_data = 'fightact?'+str(game['id'])+'?'+'priestselect'))       
    if 'invoker' in player['skills'] and player['invokercd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'К҉̧͍̯̂̐͝о̶̡͖̟́̊̆͡л̸̢̰͕̋͝д҈̣̟̎͒́͜͡о̸̲̆͋͢͝ͅв҉̡̪̦̮̆̑̕а̵̳͆̎͜͞т̶̧̛̩̗͇͗͒̚ь̶̲͖̿͢͞', callback_data = 'fightact?'+str(game['id'])+'?'+'elementmenu'))
    if 'bint' in player['inventory']:
        amount = player['inventory'].count('bint')
        kb.add(types.InlineKeyboardButton(text='Бинт ('+str(amount)+')', callback_data='fightact?' + str(game['id']) + '?' + 'bintselect'))
    if 'bomber' in player['skills'] and player['EXPLOSIONcd'] <= 0 and player['energy'] >= 5:
        kb.add(types.InlineKeyboardButton(text='ВЗРЫВ!', callback_data='fightact?' + str(game['id']) + '?' + 'EXPLOSIONselect'))
    if 'miner' in player['skills'] and player['minercd'] <= 0:
        kb.add(types.InlineKeyboardButton(text='Установить мину', callback_data='fightact?' + str(game['id']) + '?' + 'minetimerselect'))
    if ('inzhener' in player['skills'] or 'inzhener?1' in player['skills'] or 'inzhener?2' in player['skills'] or 'inzhener?3' in player['skills']) and player['inzhenercd'] <= 0:
        kb.add(types.InlineKeyboardButton(text='Создать предмет',callback_data='fightact?' + str(game['id']) + '?' + 'inzhenerselect'))
    if player['weapon'].name == 'Лира' and player['liracd'] <= 0:
        kb.add(types.InlineKeyboardButton(text='Играть на лире',callback_data='fightact?' + str(game['id']) + '?' + 'liramelodyselect'))
    if 'skeletonking' in player['skills'] and player['skeletonfirecd'] <= 0 and not player['fell']:
        kb.add(types.InlineKeyboardButton(text = 'Адский огонь', callback_data = 'fightact?'+str(game['id'])+'?'+'skeletonfireselect'))   
    if 'vampire' in player['skills'] and player['batcd'] <= 0:
      kb.add(types.InlineKeyboardButton(text = 'Запустить летучую мышь', callback_data = 'fightact?'+str(game['id'])+'?'+'batselect'))  
    if 'demonlord' in player['skills']:
        kb.add(types.InlineKeyboardButton(text = 'Адское пламя (заряды: '+str(player['hellfirecharges'])+')', callback_data = 'fightact?'+str(game['id'])+'?'+'hellfire')) 
    if player['demonlordform'] and player['energydraincd'] <= 0:
        kb.add(types.InlineKeyboardButton(text = 'Выпить энергию', callback_data = 'fightact?'+str(game['id'])+'?'+'energydrainselect'))
    if game['can_hide_dark']:
        kb.add(types.InlineKeyboardButton(text = 'Выбежать из комнаты', callback_data = 'fightact?'+str(game['id'])+'?'+'hide_in_door'))
    if 'dark_energy' in player['skills'] and player['dark_energycd'] <= 0:
        kb.add(types.InlineKeyboardButton(text='Энергия тьмы',callback_data='fightact?' + str(game['id']) + '?' + 'dark_energyselect'))
    if player['have_rat_toy']:
        kb.add(types.InlineKeyboardButton(text='Приручить крысу', callback_data='fightact?' + str(game['id']) + '?' + 'tame_rat'))
    if 'doom' in player['skills'] and player['doomcd'] <= 0 and player['energy'] >= 1:
        kb.add(types.InlineKeyboardButton(text='DOOM',
                                          callback_data='fightact?' + str(game['id']) + '?' + 'doomselect'))

    #if player['weapon'].name == 'Бита' and player['baseballcd'] <= 0:
    #    kb.add(types.InlineKeyboardButton(text = 'Оглушающий удар', callback_data = 'fightact?'+str(game['id'])+'?'+'stunhit'))   
        
    if player['id'] == 86190439:
        kb.add(types.InlineKeyboardButton(text = 'Послать нахуй', callback_data = 'fightact?'+str(game['id'])+'?'+'isaevselect'))
    if player['id'] == 319372123 and not game['tournier']:
        kb.add(types.InlineKeyboardButton(text='🍺Пивная победа',
                                          callback_data='fightact?' + str(game['id']) + '?' + 'eugenwin'))
    kb.add(types.InlineKeyboardButton(text = 'Главное меню', callback_data = 'fightact?'+str(game['id'])+'?'+'mainmenu'))
    return kb
  
def getgrenadeselect(game, player):
    kb = types.InlineKeyboardMarkup()
    x = ['grenade', 'molotov']
    for ids in x:
        kb.add(types.InlineKeyboardButton(text = getname(ids), callback_data = 'fightact?'+str(game['id'])+'?'+'selectg'+'?'+ids))
    return kb

def getinzhenerselect(game, player):
    kb = types.InlineKeyboardMarkup()
    for ids in player['inzheneritems']:
        kb.add(types.InlineKeyboardButton(text=getname(ids),callback_data='fightact?' + str(game['id']) + '?' + 'inzhener?'+ids))
    return kb
    
def getshurikenselect(game, player):
    kb = types.InlineKeyboardMarkup()
    x = ['1', '2']
    for ids in x:
        kb.add(types.InlineKeyboardButton(text = ids, callback_data = 'fightact?'+str(game['id'])+'?'+'setshurikenamount'+'?'+ids))
    return kb

def getmulticastselect(game, player):
    kb = types.InlineKeyboardMarkup()
    x = ['1', '2', '3', '4']
    for ids in x:
        kb.add(types.InlineKeyboardButton(text = 'x'+ids, callback_data = 'fightact?'+str(game['id'])+'?'+'setmulticast'+'?'+ids))
    return kb

def getlirakb(game, player):
    kb = types.InlineKeyboardMarkup()
    x = ['wind_protect', 'battle_march', 'heal_melody', '4']
    for ids in x:
        kb.add(types.InlineKeyboardButton(text='x' + ids, callback_data='fightact?' + str(
            game['id']) + '?' + 'selectliratarget' + '?' + ids))
    return kb

def getminetimerselect(game, player):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='1', callback_data='fightact?' + str(
        game['id']) + '?' + 'setminetimer' + '?' + '1'), types.InlineKeyboardButton(text='2', callback_data='fightact?' + str(
        game['id']) + '?' + 'setminetimer' + '?' + '2'))
    kb.add(types.InlineKeyboardButton(text='3', callback_data='fightact?' + str(
        game['id']) + '?' + 'setminetimer' + '?' + '3'), types.InlineKeyboardButton(text='4', callback_data='fightact?' + str(
        game['id']) + '?' + 'setminetimer' + '?' + '4'))
    return kb

def meditationselect(game, player):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text = 'Стойкость', callback_data = 'fightact?'+str(game['id'])+'?'+'meditationstoikost'+'?'+'self'))
    kb.add(types.InlineKeyboardButton(text = 'Концентрация', callback_data = 'fightact?'+str(game['id'])+'?'+'meditationconcselect'+'?'+'self'))
    kb.add(types.InlineKeyboardButton(text = 'Главное меню', callback_data = 'fightact?'+str(game['id'])+'?'+'mainmenu'))
    return kb

def elem_to_emoji(x):
    if x == 'fire':
        return '🔥'
    if x == 'water':
        return '💧'
    if x == 'ice':
        return '❄️'
    if x == 'light':
        return '☀️'
    if x == 'electro':
        return '⚡️'
    if x == 'air':
        return '🌫'
    if x == 'life':
        return '❤️'
    if x == 'random':
        return '🎲'
    if x == 'virus':
        return '🦠'
    if x == 'blood':
        return '🩸'
    if x == 'death':
        return '💀'
    if x == 'mech':
        return '⚙️'
    if x == 'nature':
        return '🌳'
    return '❓'

def spell_exists(elems):
    if 'ice' in elems and 'water' in elems and 'air' in elems:
        return 'freeze_energy'
    if 'electro' in elems and 'random' in elems and 'death' in elems:
        return 'random_lighting'
    if 'ice' in elems and 'fire' in elems and 'mech' in elems:
        return 'break_weapons'
    if 'life' in elems and 'nature' in elems and 'mech' in elems:
        return 'summon_treant'
    if 'nature' in elems and 'light' in elems and 'blood' in elems:
        return 'roots'
    if 'light' in elems and 'blood' in elems and 'fire' in elems:
        return 'light_sword'
    if 'light' in elems and 'electro' in elems and 'fire' in elems:
        return 'sunstrike'
    if 'virus' in elems and 'electro' in elems and 'blood' in elems:
        return 'drink_energy'
    if 'virus' in elems and 'air' in elems and 'death' in elems:
        return 'infection'
    electro = elems.count('electro')
    if 'electro' in elems and 'death' in elems and electro == 2:
        return 'target_lighting'
    if 'electro' in elems and 'life' in elems and electro == 2:
        return 'inc_energy'
    blood = elems.count('blood')
    if 'blood' in elems and 'air' in elems and blood == 2:
        return 'blood_to_enemy'
    virus = elems.count('virus')
    if 'virus' in elems and 'mech' in elems and virus == 2:
        return 'infect_weapon'
    water = elems.count('water')
    if 'water' in elems and 'life' in elems and water == 2:
        return 'invoker_water_shield'
    ice = elems.count('ice')
    if 'ice' in elems and 'life' in elems and ice == 2:
        return 'iceheart'
    if elems.count('electro') == 3:
        return 'big_light_strike'
    if elems.count('random') == 3:
        return 'change_skill'  
    if elems.count('death') == 3:
        return 'suicide'  
    if elems.count('blood') == 3:
        return 'blood_to_all'
    if elems.count('virus') == 3:
        return 'big_virus_mutant'
    if elems.count('fire') == 3:
        return 'fire_all'
    return False

def getspellselect(game, player):
    kb = types.InlineKeyboardMarkup()
    i = 0
    spisok = []
    for ids in player['turnelements']:
        spisok.append(types.InlineKeyboardButton(text = elem_to_emoji(ids), callback_data = 'fightact?'+str(game['id'])+'?'+'selectelement'+'?'+ids))
        i += 1
        if i > 2:
            i = 0
            kb.add(*spisok)
            spisok = []
    kb.add(types.InlineKeyboardButton(text = 'Главное меню', callback_data = 'fightact?'+str(game['id'])+'?'+'mainmenu'))
    return kb

