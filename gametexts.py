import random

def getname(x, user_id):
    return lt(user_id, f'name_{x}')
    
def getcustomtext(x):
    if x == 'tuman_perekat':
        return '"🌑|(Имя) скрылся под мраком ночи." - 💨|(Имя) перекатывается.'
    if x == 'zilch_revolver':
        return 'Оружие "Револьвер Нарсил" - обычный Револьвер.'
    if x == 'alex_death':
        return '"🌑|(Имя) отправился во тьму, чтобы обрести покой и свет в душе разжечь свой вновь, преодолев темноту и боль." - "☠️|(Имя) теряет сознание."'
    if x == 'alex_reload':
        return '"☕️|(Имя) наслаждается кофем, игнорируя крики страдающих. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'alex_shield':
        return '"🎇|(Имя), продолжая наслаждаться кофем, махнул рукой и отправил атаку в пустоту." - 🔵|(Имя) использует щит.\n' + \
               '"🎇|(имя), продолжая наслаждаться кофем, махнул рукой и махнул рукой и отправил предназначавшуюся атаку по (имя2) в пустоту." - 🔵|(имя) использует щит на (имя2). Урон отражен!'
    if x == 'alex_skip':
        return '"🌒|(Имя), попивая кофе, сеял разрушение своим присутствием." - ⬇️Пропуск хода (или "Потушиться")'
    if x == 'alex_perekat':
        return '"🎆|(Имя) телепортировался в бездну, исчезнув во мгле." - 💨|(Имя) перекатывается.'
    if x == 'semw_perekat':
        return '"🧠|(Имя) уклоняется силой мысли." - 💨|(Имя) перекатывается.'
    if x == 'togzhan_reload':
        return '"🚬|(Имя) отошла покурить. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'semw_zh_reload':
        return '"🚬|(Имя) делает жёсткую тяжку. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'zilch_reload':
        return '"👾|(Имя) ломает игру. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'semw_adrenaline':
        return '"🍾|(Имя) выпивает 1.5ку Жигулевского! Его энергия увеличена на 3." - 💉(Имя) использует адреналин на (Имя)! Его энергия увеличена на 3.'
    if x == 'tuman_reload':
        return '"♠️|(Имя) восстанавливает мощь, погружаясь в бездну своих мыслей. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'probel_shield':
        return '"🏠|(Имя) в домике." - 🔵|(Имя) использует щит.\n' + \
               '"🏠|(Имя) укрывает в домике (имя2), игрока не смогли найти и ушли" - 🔵|(имя) использует щит на (имя2). Урон отражен!'
    if x == 'alex_flamethrower':
        return '"Пасть Дракона" - обычный Огнемет.'
    if x == 'zilch_skip':
        return '"☕️|(Имя) пьет чай" или "🍬|(Имя) ест конфеты" - ⬇️Пропуск хода (или "Потушиться")'
    if x == 'valera_death':
        return '"🔋| У системы (имя) кончился заряд. Отключение..." - "☠️|(Имя) теряет сознание."'
    if x == 'semw_bulava':
        return '"Палка-хуялка" - обычная булава'
    if x == 'prorok_reload':
        return '"😈|(имя), видя, как врага наполняет страх, злорадно ухмыляется. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'chokopie_reload':
        return '"💉|(имя) вколол дозу в вену. Энергия восстановлена!" - 🕑Перезарядка'
    if x == 'probel_suicide':
        return '"⚰️|(имя) устал сражаться и лег в гроб." - (имя) пропускает ход (АФК)!'
    if x == 'tuman_shield':
        return '"👁‍🗨|(имя) переписывает реальность, спасаясь в вечности времени. Урон отражен!" - 🔵|(Имя) использует щит.\n' + \
               '"👁️‍🗨️|(имя) переписывает реальность, (имя2) спасен вечностью времени. Урон отражен!" - 🔵|(имя) использует щит на (имя2). Урон отражен!'
    if x == 'senw_shield':
        return '"⌛️| (имя) активирует способность "Временная петля", замедляющую время вокруг него. Враг, оказавшись внутри этой петли,      становится замороженным во времени и не может совершать действия" - 🔵|(Имя) использует щит.'
    if x == 'semw_molotov':
        return '"🎇|Фейерверк от (имя) разрывает небо яркими вспышками и цветными огнями, наполняя все вокруг восторгом и радостью!" - (имя) кидает коктейль молотова!'
    if x == 'tuman_chain':
        return '"Клинок Тумана 🌙" - обычная цепь'
    if x == 'alex_vor':
        return '"🙂|(имя2) пытается использовать (Предмет), но, (имя) изымает предмет из его рук и рассеивает в пыль!" - 😒|(имя2) пытается использовать (предмет), но предмет оказывается в руках у (имя)!\n' + \
               '"🙃|Вору (имя) нечего взять кроме души (имя2)" -  😒|Вору (имя) не удается ничего украсть у (имя2)!'
    if x == 'zilch_pistol':
        return '"Пистолет Нарсил" - обычный пистолет'
    if x == 'zilch_saw':
        return '"Пиломет Нарсил" - обычный пиломет'
    if x == 'zilch_machinegun':
        return '"Пулемет Нарсил" - обычный пулемет'
    if x == 'zilch_bow':
        return '"Лук Нарсил" - обычный лук'
    if x == 'zilch_drobovik':
        return '"Дробовик Нарсил" - обычный дробовик'
    if x == 'zilch_obrez':
        return '"Обрез Нарсил" - обычный обрез'
    if x == 'kirill_death':
        return '"🔮l Вокруг (имя) появляется непробиваемый барьер.Спустя пару секунд барьер пропадает. (имя) не находят под ним I💀" - "☠️|(Имя) теряет сознание."'
    if x == 'alex_berserk':
        return '"👿|Разум Архидемона (имя) разрушается! Получает (n) энергии." - 😡|Берсерк (имя) получает (n) энергии.\n' + \
               '"👿|Разум Архидемона (имя) разрушен! Архидемон впадает в безумие!" - 😡|Берсерк (имя) входит в боевой транс!'
    if x == 'semw_armor':
        return '"🪖| (имя) в своей броне выглядит непоколебимым, снимая всего (n) урона и продолжая побеждать врагов!" - 🛡| Броня (имя) снимает (n) урона!'
    if x == 'brun_alchemist':
        return '"👻|(имя) призывает стенд (имя) который помогает совершить атаку. MUDA!" - 💉|(имя) использует сыворотку бешенства на (имя)!'
    if x == 'alan_perekat':
        return '"🕘|(имя) пытается прокрутить коронку наручных часов, чтобы отмотать назад время вокруг себя" - 💨|(имя) перекатывается.'
    if x == 'meningoencephalitis_stimulator':
        return '"🥃|(имя) поливает коньяком (имя2)!" - 💉|(имя) использует стимулятор на (имя2)' + \
                '"🥃|(имя)принимает душ из коньяка" - 💉|(имя) использует стимулятор на (имя)'
    if x == 'meningoencephalitis_skip':
        return '"⬇️|(имя) делает киберспортивный мув" - ⬇️Пропуск хода (или "Потушиться")'
    if x == 'brun_shield':
        return '"🌿|(имя) прикрывается телом Es Tra Gon! Славон впитывает в себя весь дамаг (Бедный Славон) - 🔵|(Имя) использует щит.\n' + \
                '"🌿|(имя) прикрывает (имя2) Es Tra Gon! Славон пострадал из-за чужой ошибки..." - 🔵|(имя) использует щит на (имя2). Урон отражен!'
    if x == 'brun_grenade':
        return '"😼|(имя) призывает Killer Queen! Первая бомба! Нанесено  (n) урона следующим целям" - 💣|(имя) кидает гранату! Нанесено (n) урона следующим целям'
    if x == 'semw_grenade':
        return '"😱|(имя)  издает пронзительный крик ужаса! [Игроки(цели)] испытывают сильный страх, получая (n) ед. урона страхом. " - 💣|(имя) кидает гранату! Нанесено (n) урона следующим целям'
    if x == 'semw_jet':
        return '"🧙‍♀️ |(имя) произносит заклинание "Энергия Древних" над (имя). Через два хода (имя) будет полн магической силы и готов к подвигам!" - 💉|(имя) использует джет на (имя)!'
    if x == 'xitruiListochek_perekat':
        return '" |Сделав один шаг в сторону, смог уклониться от атаки " - 💨|(имя) перекатывается.'
    if x == 'mewcomer_stun':
        return '"😱|(имя) резко помахал головой, вспомнив, что он дерётся." - 🌀|(имя) приходит в себя."'
    if x == 'soonnatillo_reload':
        return '"👨🏻‍🔬 |Амфетамин был введён,мир начал вращаться быстрее, и каждое движение ощущается как вспышка!" - 🕑Перезарядка'
    if x == 'tuman_berserk':
        return '"◼️|(имя) горит чёрным пламенем! Получает 1 энергии." - 😡|Берсерк (имя) получает (n) энергии.\n' + \
               '"🖤|(имя) вспыхивает черным огнем, и превращается в Истинную форму!" - 😡|Берсерк (имя) входит в боевой транс!'
    if x == 'tuman_incvizitor':
        return '"♣️|(имя) прислушивается к своему сердцебиению..." - 🙏|(имя) молится за себя!\n' + \
               '"♣️|(имя)  прислушивается к сердцебиению (имя2)..." - 🙏|(имя) молится за (имя2)!\n' +\
               '"🖤|Ч‌‌‌‌‌ё‌‌‌‌‌‌‌р‌‌‌‌‌н҉҇‌‌‌‌‌о҈‌‌‌‌‌е‌‌‌‌‌‌‌‌ с҉‌‌‌‌‌‌е҉‌‌‌‌‌‌р‌‌‌‌‌‌‌д҈‌‌‌‌‌ц҉‌‌‌‌‌‌‌‌е‌‌‌‌‌‌‌ не даёт умереть (имя)!" - 😇|Высшие силы спасли (имя)!\n' +\
               '"🕋|(имя) помутняет разум (цель)!" - 🙏|(имя) молится. Над (цель) собираются тучи!\n' +\
               '"⬛️|(имя) не получается помутнить разум (Цель)!" - 💨|(имя) молится, но с (цель) ничего не происходит.\n' +\
               '"👁️|(Цель) Т‌‌‌‌‌‌‌‌‌‌‌‌‌е‌‌‌‌‌‌‌р‌‌я҈‌е‌т҉‌‌‌‌‌‌ к‌‌‌о҈‌‌‌‌‌‌‌‌‌н‌‌т‌ро҉‌‌‌‌‌‌‌‌‌л‌‌‌‌‌‌‌‌‌ь‌‌‌‌‌‌‌‌‌... (timer)" - ☁️|Над (цель) собираются тучи. (timer)\n' +\
               '"👁️❗️|Разум (Цель) с‌‌‌‌‌‌б҈‌‌‌‌‌‌и‌‌‌‌‌‌‌в‌‌‌‌‌‌‌‌а‌‌‌‌‌‌‌‌е҉҇‌‌‌‌‌т҈‌‌‌‌‌с҉҇‌‌‌‌‌я‌‌‌‌‌‌ в водовороте т‌‌‌е‌‌‌м҉‌‌н‌‌‌ы҈‌‌х‌‌‌ м‌‌‌ы‌‌‌с҈‌‌л‌‌‌е‌‌‌й‌‌‌!" - 🌩|Гнев небес обрушивается на (Цель) в виде молнии!'
    if x == 'probel_saw':
        return '"🧱|(имя) швыряет в (Цель) шлакоблоком! Нанесено (x) урона." - 💥|(имя) стреляет в (Цель) из пиломета! Нанесено (x) урона.'
    if x == 'bibizyan_shest':
        return '"Шест Бибизян 🐵" - обычный Шест'
    if x == 'calimator_shield':
        return '"🧬|Тело (имя) меняется, становясь на время атаки врага сверхпрочным. Урон отражён." - 🔵|(Имя) использует щит.\n"🧬|Тело (имя) отделяет кусочек, который становиться на время атаки врага сверхпрочным и защищает (имя2). Урон отражён." - 🔵|(имя) использует щит на (имя2). Урон отражен!'
    if x == 'wizy_sadist':
        return '"😃|Наблюдая за страданиями своих соперников (имя) ощущает невероятный прилив силы восстанавливая (x) энергии" - 😃|Садист (имя) получает (x) энергии.'
    if x == 'semw_hitin':
        return '"🌳|(имя) призывает хранителя леса, который наделяет (имя) защитной аурой, укрывая его силой природы." - 💉|(имя) использует хитин на (имя)!'


    return 'Неизвестное описание для текста "'+x+'". Перешлите это сообщение Пасюку (@Loshadkin).'

def gethitchance(player, energy=None, cubes=None):
    if energy == None:
        energy = player['energy']
        if 'robot' in player['skills']:
            energy = player['hp']
    if cubes == None:
        cubes = player['weapon'].cubes
    if 'sniper' in player['skills']:
        energy += 2
    #if 'pricel?1' in player['skills']:
    #    energy += 1
    #if 'pricel?2' in player['skills']:
    #    energy += 2
    #if 'pricel?3' in player['skills']:
    #    energy += 2
    if 'visor' in player['skills'] and player['weapon'].ranged:
        energy += 1
    if ('vor' in player['skills'] or 'vor?2' in player['skills'] or 'vor?3' in player['skills']) and player['weapon'].ranged:
        energy += 1
    if 'narkoman' in player['skills']:
        energy -= 1
    if 'narkoman?1' in player['skills']:
        energy -= 2
    if 'narkoman?2' in player['skills']:
        energy -= 1
    if 'narkoman?3' in player['skills']:
        energy -= 1
    if 'multicast' in player['skills'] and player['multicast'] == 2:
        energy -= 2
    if 'multicast' in player['skills'] and player['multicast'] == 3:
        energy -= 2
    if 'multicast' in player['skills'] and player['multicast'] == 4:
        energy -= 3
    #if player['weapon'].name == 'Молот' and player['energy'] == 1:
    #    energy += 1
    energy += player['weapon'].accuracybonus
    #if player["weapon"].name == "Снайперская винтовка":
    #    if player["maintarget"] != None:
    #        energy += (player["maintarget"]["power"]*6)
    basechance = 1-(energy/10)
    chance = 1
    for i in range(cubes):
        chance = chance*basechance
    naturalchance = (1-chance)*100
    naturalchance = round(naturalchance, 0)
    naturalchance = int(naturalchance)
    if energy >= 10:
        naturalchance = 100
    if naturalchance > 100:
        naturalchance = 100
    if energy <= 0:
        naturalchance = 0
    if 'robot' not in player['skills']:
        if player['energy'] <= 0:
            naturalchance = 0
    return naturalchance

def getplayertext(game, player):
    text = ''
    #if len(player['doomedskills']) > 0:
    #    text += '🔥💀🔥\n'
    text += lt(user_id, 'turn_number').format(turn=game['turn']) + '\n'

    text += '♥️' * player['hp'] + '|' + lt(user_id, 'hp_status').format(hp=player['hp'], maxhp=player['maxhp']) + '\n'
    if 'robot' not in player['skills']:
        text += '⚡️' * player['energy'] + '|' + lt(user_id, 'energy_status').format(energy=player['energy'], maxenergy=player['maxenergy']) + '\n'
    else:
        text += '🤖|' + lt(user_id, 'overheat_status').format(peregrev=player['peregrev']) + '\n'
    if player['weapon'].name == 'Сюрикены':
        text += '⚙|' + lt(user_id, 'shuriken_count').format(count=player['shurikens']) + '\n'
    #if player['weapon'].name == 'Дробовик':
    #    text += '🧰|Патроны: '+str(player['drobovik_charges'])+'/2\n'
  
    naturalchance = gethitchance(player)
    text += '🎯|Вероятность попасть - '+str(naturalchance)+'%'
    if player['maintarget'] != None and player['weapon'].name == 'Снайперская винтовка':
        energy = player['energy']
        if 'robot' in player['skills']:
            energy = player['hp']
        if game['classic_game']:
            energy += (player['maintarget']['power'] * 5)
        else:
            energy += (player['maintarget']['power']*6)
        chance2 = gethitchance(player, energy)
        enemy = game['players'][player['maintarget']['target']]
        text += '🎯|Вероятность попасть в '+enemy['name']+' - '+str(chance2)+'%\n'
    if len(player['doomedskills']) > 0:
        text = '🔥🔥🔥💀🔥🔥🔥\n'
    return text

def is_dark_boss(player):
    if player['is_dark_boss']:
        return True
    return False

def is_rhino_boss(player):
    if 'носорог' in player['name'].lower() and player['controller'] == 'bot' and player['team'] == 'rhino':
        return True
    return False

def is_necromant_boss(player):
    if 'Некромант' in player['name'] and player['controller'] == 'bot' and player['team'] == 'necromant':
        return True
    return False

def getplayerpodrobno(game, player):
    text = 'Информация:\n'
    text += player['name']+'\n'
    text += '♥️'*player['hp']+'|'+str(player['hp'])+' жизней. Максимум: '+str(player['maxhp'])+'\n'
    if 'robot' not in player['skills']:
        if 'носорог' in player['name'].lower() and player['controller'] == 'bot':
            text += '⚡️? энергии. Максимум: ?\n'
        else:
            text += '⚡️'*player['energy']+'|'+str(player['energy'])+' энергии. Максимум: '+str(player['maxenergy'])+'\n'
    else:
        text += '🤖|Перегрев: '+str(player['peregrev'])+'%\n'
    text += '💔x'+str(player['dmglimit'])+'/'+str(player['maxdmglimit'])+' ран. Влияет на потерю жизней\n'
    sposobnosti = ''
    for ids in player['skills']:
        sposobnosti += getname(ids)+', '
    sposobnosti = sposobnosti[:len(sposobnosti)-2]
    if player['is_necromant']:
        sposobnosti = '❓'
    text += 'Способности: '+sposobnosti+'\n'
    predmeti = ''
    for ids in player['inventory']:
        predmeti += getname(ids)+', '
    if player['is_necromant']:
        predmeti = '❓'
    if predmeti != '':
        predmeti = predmeti[:len(predmeti)-2]
        text += 'Предметы: '+predmeti+'\n'
    wdmg = 0
    if player['weapon'].name in ['Огнемет', 'Огнемет Нарсил']:
        wdmg = '1-1'
    elif player['weapon'].name == 'Пистолет':
        wdmg = '1-3'
    elif player['weapon'].name == 'Револьвер':
        wdmg = '3-3'
    elif player['weapon'].name == 'Пиломет':
        wdmg = '1-1'
    elif player['weapon'].name == 'One punch':
        wdmg = 'Очень много'
    else:
        wdmg = str(1+player['weapon'].dmgbonus)+'-'+str(1+player['weapon'].dmgbonus+player['weapon'].cubes)
    wname = player['weapon'].name
    if wname == 'Посох Некроманта':
        wname = 'Посох некроманта'
    if wname == 'Булава':
        wname = 'Булава'
    if wname == 'Меч дряхлого скелета':
        wname = 'Меч'
    if 'носорог' in player['name'].lower() and player['controller'] == 'bot':
        text += 'Оружие: рог\n'
    else:
        text += 'Оружие: '+wname+' - '+str(player['weapon'].energycost)+'⚡️\n'
    naturalchance = gethitchance(player)
    if 'носорог' in player['name'].lower() and player['controller'] == 'bot':
        text += '🎯|Вероятность попасть - ?%'
    else:
        text += '🎯|Вероятность попасть - '+str(naturalchance)+'%'
    if player['maintarget'] != None and player['weapon'].name == 'Снайперская винтовка':
        energy = player['energy']
        if 'robot' in player['skills']:
            energy = player['hp']
        energy += (player['maintarget']['power']*5)
        chance2 = gethitchance(player, energy)
        enemy = game['players'][player['maintarget']['target']]
        text += '🎯|Вероятность попасть в '+enemy['name']+' - '+str(chance2)+'%\n'
    if is_dark_boss(player):
        text = 'Неизвестно.'
    return text

def getattacktext(game, player, target, damage, bicepc = False, firetext = '', sokrushtext = False, chaintext = False, narsiltext = False, counterattack = False,
                 execution = False, executiontext = False, grenade=False, addtarget=False, firearrow = False, vampiretext = '', multicast = False,
                 lightsword = False, hitdowntext = False, lightaspect = False, strongshot = False, burrowstrike = False, luciferblade = False, claws_biceps = False):
    weapon = player['weapon']
    text = '💥|'+player['name']+' атакует '+target['name']+'! Нанесено '+str(damage)+' урона.'
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    if weapon.name == 'Короткий меч':
        text = '👊|'+player['name']+' бьет '+target['name']+' коротким мечом! Нанесено '+str(damage)+' урона.'
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    elif weapon.name == 'Пистолет':
        if 'zilch_pistol' in player['customtexts'] and player['customtexts']['zilch_pistol']:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из пистолета Нарсил! Нанесено '+str(damage)+' урона.'
        else:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из пистолета! Нанесено '+str(damage)+' урона.'

    elif weapon.name == 'Обрез':
        if not player['strongshot']:
            if 'zilch_obrez' in player['customtexts'] and player['customtexts']['zilch_obrez']:
                text = '💥|'+player['name']+' стреляет в '+target['name']+' из обреза Нарсил! Нанесено '+str(damage)+' урона.'
            else:
                text = '💥|'+player['name']+' стреляет в '+target['name']+' из обреза! Нанесено '+str(damage)+' урона.'
        else:
            if 'zilch_obrez' in player['customtexts'] and player['customtexts']['zilch_obrez']:
                text = '💥❗️|'+player['name']+' совершает мощный выстрел по '+target['name']+'! Нанесено '+str(damage)+' урона.'
            else:
                text = '💥❗️|'+player['name'] +' совершает мощный выстрел по '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Дробовик':
        if 'zilch_drobovik' in player['customtexts'] and player['customtexts']['zilch_drobovik']:
            text = '💥|'+player['name']+' стреляет в ' + target['name'] + ' из дробовика Нарсил! Нанесено '+str(damage)+' урона.'
        else:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из дробовика! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Револьвер':
        if 'zilch_revolver' in player['customtexts'] and player['customtexts']['zilch_revolver']:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из револьвера Нарсил! Нанесено '+str(
                damage)+' урона.'
        else:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из револьвера! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Электрошокер':
        text = '💥|'+player['name']+' стреляет в '+target['name']+' из электрошокера! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Огнемет':
        if 'alex_flamethrower' in player['customtexts'] and player['customtexts']['alex_flamethrower']:
            text = '💥|'+player['name'] + ' извергает пламя в '+target['name']+' из Пасти Дракона! Нанесено '+str(
                damage)+' урона.'
        else:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из огнемета! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Огнемет Нарсил':
        text = '💥|'+player['name']+' стреляет в '+target['name']+' из огнемета Нарсил! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Пиломет':
        if 'zilch_saw' in player['customtexts'] and player['customtexts']['zilch_saw']:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из пиломета Нарсил! Нанесено '+str(damage)+' урона.'
        elif 'probel_saw' in player['customtexts'] and player['customtexts']['probel_saw']:
            text = '🧱|'+player['name']+' швыряет в '+target['name']+' шлакоблоком! Нанесено '+str(damage)+' урона.'
        else:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из пиломета! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Камень':
        text = '💥|'+player['name']+' кидает камень в '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Лук Асгард':
        text = '💥|'+player['name']+' стреляет в '+target['name']+' из Лука Асгард! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Когти дракона':
        text = '💥|'+player['name']+' бьет '+target['name']+' когтями! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Волшебный посох':
        text = '✨|'+player['name']+' атакует '+target['name']+' искрами из посоха! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Снайперская винтовка':
        text = '💥|'+player['name']+' стреляет в '+target['name']+' из снайперской винтовки! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Пулемет':
        if 'zilch_machinegun' in player['customtexts'] and player['customtexts']['zilch_machinegun']:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из пулемета Нарсил! Нанесено '+str(damage)+' урона.'
        else:
            text = '💥|'+player['name']+' стреляет в '+target['name']+' из пулемета! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Тесак':
        text = '👊|'+player['name']+' бьет '+target['name']+' тесаком! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Водомет':
        text = '💥|'+player['name']+' стреляет в '+target['name']+' из водомета! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'One punch':
        text = '👊🔥|'+player['name']+' наносит смертельный удар по '+target['name']+'! Нанесено очень много урона.'
    elif weapon.name == 'Сюрикены':
        text = '💥|'+player['name']+' бросает сюрикен в '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Морозный лук':
        text = '💥|'+player['name']+' стреляет в '+target['name']+' из морозного лука! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Глаз демона':
        text = '☣️|'+player['name']+' стреляет по '+target['name']+' лазером из глаз! Нанесено '+str(damage)+' урона.'
    elif weapon.name == "Частица тьмы":
        h = '🖤'
        target['dark_counter'] += 1
        if target['dark_counter'] == 1:
            h = '💚'
        elif target['dark_counter'] == 2:
            h = '🧡'
        elif target['dark_counter'] == 3:
            h = '💙'
        elif target['dark_counter'] == 4:
            h = '💜'
        elif target['dark_counter'] >= 5:
            h = '🖤'
        if target['dark_counter'] < 3:
            text = h+'|' + player['name'] + ' погружает разум ' + target['name'] + ' во тьму. '+target['name']+' чувствует страх ('+str(target['dark_counter'])+').'
        else:
            text = h + '|̸̝͈̀͢͡' + player['name'] + ' п̷̛̣̯̂͒͜о̷̩̥̊̌̊͜͠г̷̱͚҇͛͢р̶̤̙̗͛̉͜͝ӳ̸̖͛͜͞ж̸̬̂̽͜͠а̵̡͚̳͛͝е҈̡͎̭̙҇́͊т̷̡̮͈҇̈́̇̾ р̸̧̮̗͗̐͠а̷̡̬́͞з̸̨̛̣̦́̅у̸̧̫̠̳́̇͠м҈͉̩͎͒͜͡ ' + \
                   target['name'] + ' в̷̢͍̦҇̾ͅо҈̢̛͙͛ т̶̨͕͋̅͗͠ь̴̧̬͑͠м̵̮̤̭́̎͜͡у̸̡̛͔͉̯̒.̷̡͈̆̍̉͡ ' + target['name'] + \
                   ' ч҉̛͉̜͈̃̀͢у̵̧̖̭͂͞в҉͇̣̰͂͜͝с̸̨͚͚͋̍͂͝т҈̢̘̄̎̈́͞в̵̱҇̔̏͜ӱ̶̝́͢͡ӗ̵̨̘́̕т҉̨͕͎̥҇͆̚ с̷̛̫̈͗͜т҉̧̫̓̋͠р҉̡̜͚̤̿̍̚͞а̶͉̗҇́̀̚͢х̶̨͙̞̀̍̌͠ (' + str(target['dark_counter']) + \
                   ').'

    elif weapon.name == "Огромный тесак":
        text = '👊|' + player['name'] + ' бьет ' + target['name'] + ' огромным тесаком! Нанесено ' + str(damage) + ' урона.'
    elif weapon.name == "Теневая пушка":
        text = '💥|' + player['name'] + ' выстреливает сгустком мрака в ' + target['name'] + '! Нанесено ' + str(damage) + ' урона. Цель теряет 1♥️.'
    elif weapon.name == "Пасть собаки":
        text = '👁🦷|' + player['name'] + ' кусает ' + target['name'] + '! Нанесено ' + str(damage) + ' урона.'
    elif weapon.name == "Отсутствует":
        text = '👁|Бешеная ' + player['name'] + ' поглощает ' + target['name'] + '. Нанесено '+ str(damage) + ' урона.'

    elif weapon.name == 'Нож':
        text = '👊|'+player['name']+' бьет '+target['name']+' ножом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Пылающий клинок':
        if not luciferblade:
            text = '👊|'+player['name']+' бьет '+target['name']+' пылающим клинком! Нанесено '+str(damage)+' урона.'
        else:
            text = '🗡🔥|' + player['name'] + ' наносит усиленный пламенем удар по ' + target['name'] + '. Цель загорается и получает оглушение!'
    elif weapon.name == 'Пенис-дубина':
        text = '👊|'+player['name']+' бьет '+target['name']+' пенисом-дубиной! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Бита':
        text = '👊|'+player['name']+' бьет '+target['name']+' битой! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Щупальца':
        text = '👊|'+player['name']+' бьет '+target['name']+' щупальцами! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Факел':
        text = '👊|'+player['name']+' бьет '+target['name']+' факелом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Кулаки':
        text = '👊|'+player['name']+' бьет '+target['name']+' кулаком! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Топор':
        text = '👊|'+player['name']+' бьет '+target['name']+' топором! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Булава':
        if 'semw_bulava' in player['customtexts'] and player['customtexts']['semw_bulava']:
            text = '👊|'+player['name']+' бьет '+target['name']+' Палкой-хуялкой! Нанесено '+str(
                damage)+' урона.'
        #elif 'zilch_bulava' in player['customtexts'] and player['customtexts']['zilch_bulava']:
        #    text = '👊|' + player['name'] + ' бьет ' + target['name'] + ' булавой Нарсил! Нанесено ' + str(
        #        damage) + ' урона.'
        else:
            text = '👊|'+player['name']+' бьет '+target['name']+' булавой! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Кастет':
        text = '👊|'+player['name']+' бьет '+target['name']+' кастетом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Сабля':
        text = '👊|'+player['name']+' бьет '+target['name']+' саблей! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Полицейская дубинка':
        text = '👊|'+player['name']+' бьет '+target['name']+' полицейской дубинкой! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Дуэльная рапира':
        text = '👊|'+player['name']+' атакует '+target['name']+' рапирой! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Меч':
        text = '👊|'+player['name']+' бьет '+target['name']+' мечом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Меч ':
        text = '👊|'+player['name']+' бьет '+target['name']+' мечом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Меч дряхлого скелета':
        text = '👊|'+player['name']+' бьет '+target['name']+' мечом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Ятаган':
        text = '👊|'+player['name']+' бьет '+target['name']+' ятаганом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Зубы вурдалака':
        text = '🦷|'+player['name']+' кусает '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Мраморная колонна':
        text = '💢|'+player['name']+' сокрушает '+target['name']+' мраморной колонной! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Посох некроманта' or weapon.name == 'Посох Некроманта':
        text = '⚫️|'+player['name']+' стреляет в '+target['name']+' черными искрами из посоха! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Щит':
        text = '👊|'+player['name']+' бьет '+target['name']+' щитом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Рука трента':
        text = '👊|'+player['name']+' бьет '+target['name']+' ветками! Нанесено '+str(damage)+' урона. Корни обхватили цель!'
    elif weapon.name == 'Меч Света':
        text = '👊|'+player['name']+' бьет '+target['name']+' Мечом Света! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Посох':
        text = '👊|'+player['name']+' бьет '+target['name']+' посохом! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Конечность вируса':
        text = '🤢|'+player['name']+' отправляет токсичное облако на '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Молот':
        if not player['truestrike']:
            text = '👊|'+player['name']+' бьет '+target['name']+' молотом! Нанесено '+str(damage)+' урона.'
        else:
            text = '👊❗️|'+player['name']+' наносит точный удар молотом по '+target['name']+'! Нанесено '+str(damage)+' урона.'
 
    elif weapon.name == 'Клыки вампира':
        text = '🦷|'+player['name']+' кусает '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Рог':
        if target['stun'] > 0 and 'носорог' in player['name'].lower() and player['controller'] == 'bot':
            text = '💢|'+player['name']+' топчет лежащего на земле '+target['name']+'! Нанесено '+str(damage)+' урона.'
        else:
            text = '👊|'+player['name']+' бьет '+target['name']+' рогом! Нанесено '+str(damage)+' урона.'
  
    elif weapon.name == 'Меч короля':
        text = '👊|'+player['name']+' бьет '+target['name']+' мечом короля скелетов! Нанесено '+str(damage)+' урона.'

    elif weapon.name == 'Трезубец':
        text = '👊|' + player['name'] + ' бьет ' + target['name'] + ' трезубцем! Нанесено ' + str(
            damage) + ' урона.'

    elif weapon.name == 'Демоническая сила':
        text = '🧬|' + player['name'] + ' приказывает щупальцам атаковать ' + target['name'] + '! Нанесено '+ str(
            damage) + ' урона.'
  
    elif weapon.name == 'Стальные когти':
        if player['claws']:
            text = '👊|'+player['name']+' бьет '+target['name']+' стальным когтем! Нанесено '+str(damage)+' урона.'
        else:
            text = '👊|'+player['name']+' бьет '+target['name']+' стальным кулаком! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Укус зомби':
        text = '🧟‍♂️|'+player['name']+' кусает '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Кувалда':
        if not sokrushtext:
            text = '👊|'+player['name']+' бьет '+target['name']+' кувалдой! Нанесено '+str(damage)+' урона.'
        else:
            text = '🔨|'+player['name']+' наносит сокрушительный удар по '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Шест':
        if not hitdowntext:
            if 'bibizyan_shest' in player['customtexts'] and player['customtexts']['bibizyan_shest']:
                text = '👊|'+player['name']+' бьет '+target['name']+' шестом Бибизян 🐵! Нанесено '+str(damage)+' урона.'
            else:
                text = '👊|'+player['name']+' бьет '+target['name']+' шестом! Нанесено '+str(damage)+' урона.'
        else:
            text = '🦯|'+player['name']+' пытается сбить '+target['name']+' с ног! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Цепь':
        if not chaintext:
            if 'tuman_chain' in player['customtexts'] and player['customtexts']['tuman_chain']:
                text = '👊|'+player['name']+' бьет '+target['name']+' Клинком Тумана! Нанесено '+str(damage)+' урона.'
            else:
                text = '👊|'+player['name']+' бьет '+target['name']+' цепью! Нанесено '+str(damage)+' урона.'
        else:
            if 'tuman_chain' in player['customtexts'] and player['customtexts']['tuman_chain']:
                text = '⛓|'+player['name']+' пытается выбить оружие из рук '+target['name']+'! Нанесено '+str(damage)+' урона.'
            else:
                text = '⛓|'+player['name']+' пытается выбить оружие из рук '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Копье Нарсил':
        if not narsiltext:
            if not counterattack:
                text = '👊|'+player['name']+' бьет '+target['name']+' Копьем Нарсил! Нанесено '+str(damage)+' урона.'
            else:
                text = '⚔️|'+player['name']+' бьет '+target['name']+' Копьем Нарсил! Нанесено '+str(damage)+' урона.'
        else:
            text = '💥|'+player['name']+' кидает Копье Нарсил в '+target['name']+'! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Копье':
        if not counterattack:
            text = '👊|'+player['name']+' бьет '+target['name']+' копьем! Нанесено '+str(damage)+' урона.'
        else:
            text = '⚔️|'+player['name']+' бьет '+target['name']+' копьем! Нанесено '+str(damage)+' урона.'
    elif weapon.name == 'Катана':
        if not executiontext:
            text = '👊|'+player['name']+' бьет '+target['name']+' катаной! Нанесено '+str(damage)+' урона.'
        else:
            text = '㊙️|'+player['name']+' наносит стремительный удар по '+target['name']+', оставляя страшную рану! Нанесено '+str(damage)+' урона. '+target['name']+' теряет жизнь!'

    elif weapon.name == 'Клыки червя':
        if not burrowstrike:
            text = '💥|' + player['name'] + ' кусает ' + target['name'] + '! Нанесено ' + str(
                damage) + ' урона.'
        else:
            text = '💥|' + player['name'] + ' набрасывается на ' + target['name'] + '! Нанесено ' + str(
                damage) + ' урона.'
    elif weapon.name == 'Гранатомет':        
        if addtarget == None or addtarget == False:
            if grenade == 'grenade':
                text = '💣|'+player['name']+' стреляет в '+target['name']+' из гранатомета! Нанесено '+str(damage)+' урона.'
            elif grenade == 'molotov':
                text = '🍸|'+player['name']+' стреляет в '+target['name']+' из гранатомета! '+target['name']+' в огне!'
        else:
            targetstext = ''
            targetstext += target['name']+', '
            targetstext += addtarget['name']
            if grenade == 'grenade':
                text = '💣|'+player['name']+' стреляет из гранатомета! Нанесено '+str(damage)+' урона следующим целям: '+targetstext+'.'
            elif grenade == 'molotov':
                text = '🍸|'+player['name']+' стреляет из гранатомета! '+targetstext+' в огне!'
    if weapon.name == 'Лук':
        if not firearrow:
            if 'zilch_bow' in player['customtexts'] and player['customtexts']['zilch_bow']:
                text = '💥|'+player['name']+' стреляет в '+target['name']+' из лука Нарсил! Нанесено '+str(damage)+' урона.'
            else:
                text = '💥|'+player['name']+' стреляет в '+target['name']+' из лука! Нанесено '+str(damage)+' урона.'
        else:
            if 'zilch_bow' in player['customtexts'] and player['customtexts']['zilch_bow']:
                text = '☄️|'+player['name']+' поджигает стрелу и запускает ее в '+target['name']+'!'
            else:
                text = '☄️|'+player['name']+' поджигает стрелу и запускает ее в '+target['name']+'!'
    if player['charge']:
        text = '💢|'+player['name']+' атакует '+target['name']+' с разбега! Нанесено '+str(damage)+' урона.'
    if bicepc:
        text += ' ❗️'
    if claws_biceps:
        text += ' ⚙️'
    if multicast:
        text += ' 👁'    
    if lightaspect:
        text += ' ☀️'
    if lightsword:
        text += '\n☀️|Яркий луч света ослепляет '+target['name']+'! Соперник получает 3 урона и '+\
                    'слабость (1) на 3 хода.'
    text += firetext
    text += vampiretext
    text += '\n'
    return text

def getmisstext(game, player, target, sokrushtext = False, chaintext = False, narsiltext = False, hitdowntext = False, burrowstrike = False, luciferblade = False):
    weapon = player['weapon']
    text = player['name']+' атакует '+target['name']+', но не попадает!\n'
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    if weapon.name == "Короткий меч":
        text = '💨|' + player['name'] + ' бьет ' + target['name'] + ' коротким мечом, но не попадает.\n'
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    ########################################################## CW ########################################################
    
    elif weapon.name == 'Пистолет':
        if 'zilch_pistol' in player['customtexts'] and player['customtexts']['zilch_pistol']:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из пистолета Нарсил, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из пистолета, но не попадает.\n'
    elif weapon.name == 'Обрез':
        if not player['strongshot']:
            if 'zilch_obrez' in player['customtexts'] and player['customtexts']['zilch_obrez']:
                text = '💨|'+player['name']+' стреляет в '+target['name']+' из обреза Нарсил, но не попадает.\n'
            else:
                text = '💨|'+player['name']+' стреляет в '+target['name']+' из обреза, но не попадает.\n'
        else:
            if 'zilch_obrez' in player['customtexts'] and player['customtexts']['zilch_obrez']:
                text = '💨❗️|'+player['name']+' совершает мощный выстрел по '+target['name']+', но не попадает.\n'
            else:
                text = '💨❗️|'+player['name']+' совершает мощный выстрел по '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Дробовик':
        if 'zilch_drobovik' in player['customtexts'] and player['customtexts']['zilch_drobovik']:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из дробовика Нарсил, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из дробовика, но не попадает.\n'
    elif weapon.name == 'Револьвер':
        if 'zilch_revolver' in player['customtexts'] and player['customtexts']['zilch_revolver']:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из револьвера Нарсил, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из револьвера, но не попадает.\n'
    elif weapon.name == 'Электрошокер':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из электрошокера, но не попадает.\n'
    elif weapon.name == 'Пиломет':
        if 'zilch_saw' in player['customtexts'] and player['customtexts']['zilch_saw']:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из пиломета Нарсил, но не попадает.\n'
        elif 'probel_saw' in player['customtexts'] and player['customtexts']['probel_saw']:
            text = '💨|'+player['name']+' швыряет в '+target['name']+' шлакоблоком, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из пиломета, но не попадает.\n'
    elif weapon.name == 'Камень':
        text = '💨|'+player['name']+' кидает камень в '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Огнемет':
        if 'alex_flamethrower' in player['customtexts'] and player['customtexts']['alex_flamethrower']:
            text = '💨|'+player['name']+' извергает пламя в '+target['name']+' из Пасти Дракона, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из огнемета, но не попадает.\n'
    elif weapon.name == 'Огнемет Нарсил':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из огнемета Нарсил, но не попадает.\n'
    elif weapon.name == 'Когти дракона':
        text = '💨|'+player['name']+' бьет '+target['name']+' когтями, но не попадает.\n'
    elif weapon.name == 'Водомет':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из водомета, но не попадает.\n'
    elif weapon.name == 'Сюрикены':
        text = '💨|'+player['name']+' бросает сюрикен в '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Пулемет':
        if 'zilch_machinegun' in player['customtexts'] and player['customtexts']['zilch_machinegun']:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из пулемета Нарсил, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' стреляет в '+target['name']+' из пулемета, но не попадает.\n'
    elif weapon.name == 'Морозный лук':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из морозного лука, но не попадает.\n'
    elif weapon.name == 'Волшебный посох':
        text = '💨|'+player['name']+' атакует '+target['name']+' искрами из посоха, но не попадает.\n'

    elif weapon.name == "Огромный тесак":
        text = '💨|' + player['name'] + ' бьет ' + target['name'] + ' огромным тесаком, но не попадает.\n'
    elif weapon.name == "Теневая пушка":
        text = '💨|' + player['name'] + ' выстреливает сгустком мрака в ' + target['name'] + ', но не попадает.\n'
    elif weapon.name == "Пасть собаки":
        text = '💨|' + player['name'] + ' кусает ' + target['name'] + ', но не попадает.\n'
    elif weapon.name == "Ятаган":
        text = '💨|' + player['name'] + ' бьет ' + target['name'] + ' ятаганом, но не попадает.\n'

    elif weapon.name == 'Пылающий клинок':
        if not luciferblade:
            text = '💨|'+player['name']+' бьет '+target['name']+' пылающим клинком, но не попадает.\n'
        else:
            text = '🗡🔥|' + player['name'] + ' наносит усиленный пламенем удар по ' + target['name'] + ', но не попадает.\n'

    elif weapon.name == 'Трезубец':
        text = '💨|'+player['name']+' бьет '+target['name']+' трезубцем, но не попадает.\n'

    elif weapon.name == 'Снайперская винтовка':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из снайперской винтовки, но не попадает.\n'
    elif weapon.name == 'One punch':
        text = '💨|'+player['name']+' наносит смертельный удар по '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Нож':
        text = '💨|'+player['name']+' бьет '+target['name']+' ножом, но не попадает.\n'
    elif weapon.name == 'Посох':
        text = '💨|'+player['name']+' бьет '+target['name']+' посохом, но не попадает.\n'
    elif weapon.name == 'Тесак':
        text = '💨|'+player['name']+' бьет '+target['name']+' тесаком, но не попадает.\n'
    elif weapon.name == 'Бита':
        text = '💨|'+player['name']+' бьет '+target['name']+' битой, но не попадает.\n'
    elif weapon.name == 'Щупальца':
        text = '💨|'+player['name']+' бьет '+target['name']+' щупальцами, но не попадает.\n'
    elif weapon.name == 'Факел':
        text = '💨|'+player['name']+' бьет '+target['name']+' факелом, но не попадает.\n'
    elif weapon.name == 'Лук Асгард':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из Лука Асгард, но не попадает.\n'
    elif weapon.name == 'Кулаки':
        text = '💨|'+player['name']+' бьет '+target['name']+' кулаком, но не попадает.\n'
    elif weapon.name == 'Топор':
        text = '💨|'+player['name']+' бьет '+target['name']+' топором, но не попадает.\n'
    elif weapon.name == 'Булава':
        if 'semw_bulava' in player['customtexts'] and player['customtexts']['semw_bulava']:
            text = '💨|'+player['name']+' бьет '+target['name']+' Палкой-хуялкой, но не попадает.\n'
        #elif 'zilch_bulava' in player['customtexts'] and player['customtexts']['zilch_bulava']:
        #    text = '💨|' + player['name'] + ' бьет ' + target['name'] + ' булавой Нарсил, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' бьет '+target['name']+' булавой, но не попадает.\n'
    elif weapon.name == 'Кастет':
        text = '💨|'+player['name']+' бьет '+target['name']+' кастетом, но не попадает.\n'
    elif weapon.name == 'Сабля':
        text = '💨|'+player['name']+' бьет '+target['name']+' саблей, но не попадает.\n'
    elif weapon.name == 'Дуэльная рапира':
        text = '💨|'+player['name']+' атакует '+target['name']+' рапирой, но не попадает.\n'
    elif weapon.name == 'Меч':
        text = '💨|'+player['name']+' бьет '+target['name']+' мечом, но не попадает.\n'
    elif weapon.name == 'Меч ':
        text = '💨|'+player['name']+' бьет '+target['name']+' мечом, но не попадает.\n'
    elif weapon.name == 'Щит':
        text = '💨|'+player['name']+' бьет '+target['name']+' щитом, но не попадает.\n'
    elif weapon.name == 'Рука трента':
        text = '💨|'+player['name']+' бьет '+target['name']+' ветками, но не попадает.\n'
    elif weapon.name == 'Меч Света':
        text = '💨|'+player['name']+' бьет '+target['name']+' Мечом Света, но не попадает.\n'
    elif weapon.name == 'Меч дряхлого скелета':
        text = '💨|'+player['name']+' бьет '+target['name']+' мечом, но не попадает.\n'
    elif weapon.name == 'Зубы вурдалака':
        text = '💨|'+player['name']+' кусает '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Мраморная колонна':
        text = '💨|'+player['name']+' сокрушает '+target['name']+' мраморной колонной, но не попадает. На месте удара осталась огромная дыра.\n'
    elif weapon.name == 'Посох некроманта' or weapon.name == 'Посох Некроманта':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' черными искрами из посоха, но не попадает.\n'
    elif weapon.name == 'Конечность вируса':
        text = '💨|'+player['name']+' отправляет токсичное облако на '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Молот':
        if not player['truestrike']:
            text = '💨|'+player['name']+' бьет '+target['name']+' молотом, но не попадает.\n'
        else:
            text = '💨❗️|'+player['name']+' наносит точный удар молотом по '+target['name']+', но не попадает.\n'
  
    elif weapon.name == 'Полицейская дубинка':
        text = '💨|'+player['name']+' бьет '+target['name']+' полицейской дубинкой, но не попадает.\n'
    elif weapon.name == 'Глаз демона':
        text = '💨|'+player['name']+' стреляет по '+target['name']+' лазером из глаз, но не попадает.\n'
    elif weapon.name == 'Клыки вампира':
        text = '💨|'+player['name']+' кусает '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Меч короля':
        text = '💨|'+player['name']+' бьет '+target['name']+' мечом короля скелетов, но не попадает.\n'
    elif weapon.name == 'Катана':
        text = '💨|' + player['name'] + ' бьет ' + target['name'] + ' катаной, но не попадает.\n'
   
    elif weapon.name == 'Стальные когти':
        if player['claws']:
            text = '💨|'+player['name']+' бьет '+target['name']+' стальным когтем, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' бьет '+target['name']+' стальным кулаком, но не попадает.\n'
    elif weapon.name == 'Гранатомет':
        text = '💨|'+player['name']+' стреляет в '+target['name']+' из гранатомета, но не попадает.\n'
    elif weapon.name == 'Лук':
        if not player['firearrow']:
            if 'zilch_bow' in player['customtexts'] and player['customtexts']['zilch_bow']:
                text = '💨|'+player['name']+' стреляет в '+target['name']+' из лука Нарсил, но не попадает.\n'
            else:
                text = '💨|'+player['name']+' стреляет в '+target['name']+' из лука, но не попадает.\n'
        else:
            if 'zilch_bow' in player['customtexts'] and player['customtexts']['zilch_bow']:
                text = '💨|'+player['name']+' поджигает стрелу и запускает ее в '+target['name']+', но не попадает.\n'
            else:
                text = '💨|'+player['name']+' поджигает стрелу и запускает ее в '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Укус зомби':
        text = '💨|'+player['name']+' кусает '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Кувалда':
        if sokrushtext:
            text = '💨|'+player['name']+' пытается нанести сокрушительный удар кувалдой по '+target['name']+', но не попадает.\n'
        else:
            text = '💨|'+player['name']+' бьет '+target['name']+' кувалдой, но не попадает.\n'
    elif weapon.name == 'Шест':
        if player['hitdown']:
            text = '💨|'+player['name']+' пытается сбить '+target['name']+' с ног, но не попадает.\n'
        else:
            if 'bibizyan_shest' in player['customtexts'] and player['customtexts']['bibizyan_shest']:
                text = '💨|'+player['name']+' бьет '+target['name']+' шестом Бибизян 🐵, но не попадает.\n'
            else:
                text = '💨|'+player['name']+' бьет '+target['name']+' шестом, но не попадает.\n'
    elif weapon.name == 'Цепь':
        if not chaintext:
            if 'tuman_chain' in player['customtexts'] and player['customtexts']['tuman_chain']:
                text = '💨|' + player['name']+' бьет '+target['name']+' Клинком Тумана, но не попадает.\n'
            else:
                text = '💨|' + player['name']+' бьет '+target['name']+' цепью, но не попадает.\n'
        else:
            if 'tuman_chain' in player['customtexts'] and player['customtexts']['tuman_chain']:
                text = '💨|'+player['name']+' пытается выбить оружие из рук '+target['name']+'!\n'
            else:
                text = '💨|'+player['name']+' пытается выбить оружие из рук '+target['name']+'!\n'
    elif weapon.name == 'Копье Нарсил':
        if not narsiltext:
            text = '💨|'+player['name']+' бьет '+target['name']+' Копьем Нарсил, но не попадает.\n'
        else:
            text = '💨|'+player['name']+' кидает Копье Нарсил в '+target['name']+', но не попадает.\n'
    elif weapon.name == 'Копье':
        text = '💨|'+player['name']+' бьет '+target['name']+' копьем, но не попадает.\n'
    elif weapon.name == 'Рог':
        text = '💨|'+player['name']+' бьет '+target['name']+' рогом, но не попадает.\n'

    elif weapon.name == 'Клыки червя':
        if not burrowstrike:
            text = '💨|' + player['name'] + ' кусает ' + target['name'] + ', но не попадает.\n'
        else:
            text = '💨|' + player['name'] + ' набрасывается на ' + target['name'] + ', но не попадает.\n'

    elif weapon.name == 'Демоническая сила':
        text = '💨|' + player['name'] + ' приказывает щупальцам атаковать ' + target['name'] + ', но они не попадают.\n'
  
    elif weapon.name == 'Пенис-дубина':
        text = '💨|'+player['name']+' бьет '+target['name']+' пенисом-дубиной, но не попадает.\n'
    if player['charge']:
        text = '💨|'+player['name']+' атакует '+target['name']+' с разбега, но не попадает.\n'
    return text

def getweaponhits(weapon, energy, amount = 10000):
    damage = 0
    chance = energy
    chances = {}
    for cycles in range(amount):
        wdamage = 0
        for i in range(weapon.cubes):
            x = random.randint(1, 10)
            if x <= chance:
                wdamage += 1
        if wdamage > 0:
            if weapon.name == 'Гранатомет':
                wdamage = random.randint(2, 3)
            if weapon.name in ['Огнемет', 'Огнемет Нарсил']:
                wdamage = 1
            if weapon.name == 'Револьвер':
                wdamage = 3
            if weapon.name == 'Лук Асгард':
                wdamage = 1
            if weapon.name == 'Пиломет':
                wdamage = 1
            if weapon.name == 'Электрошокер':
                if energy > 0:
                    wdamage = random.randint(1, energy)
                else:
                    wdamage = 0
        damage += wdamage
        if wdamage not in chances:
            chances.update({wdamage:1})
        else:
            chances[wdamage] += 1
    try:
        sredn = round(damage/amount, 4)
    except:
        sredn = 0
    return sredn, chances
    
            
        
