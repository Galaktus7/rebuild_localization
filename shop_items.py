import random
from chatwars import cw_weaponlist

scrolls_to_sale = {
        #'enduring':{'code':'enduring', 'name':'Выносливый', 'lvl':1, 'cost':440, 'buy_command':'/buy_scroll_enduring', 'use_command':'/use_scroll_enduring',
        #            'description': "Увеличивает максимальную энергию на 1/2/3."},
    
        'resistant':{'code':'resistant', 'name':'Стойкий', 'lvl':1, 'cost':100, 'buy_command':'/buy_scroll_resistant', 'use_command':'/use_scroll_resistant',
                     'description': "Увеличивает лимит урона для потери жизней на 1/2/4."},
    
        'dvuzhil':{'code':'dvuzhil', 'name':'Двужильность', 'lvl':1, 'cost':400, 'buy_command':'/buy_scroll_dvuzhil', 'use_command':'/use_scroll_dvuzhil',
                   'description': "Увеличивает максимум жизней (1/1/2) и сопротивление кровотечению (0/2/2)."},
    
        'zapas':{'code':'zapas', 'name':'Запасливый', 'lvl':1, 'cost':350, 'buy_command':'/buy_scroll_zapas', 'use_command':'/use_scroll_zapas',
                 'description': "В начале боя вы получаете 1/2/3 случайных дополнительных предмета."},
    
        'armor':{'code':'armor', 'name':'Бронежилет', 'lvl':1, 'cost':200, 'buy_command':'/buy_scroll_armor', 'use_command':'/use_scroll_armor',
                 'description': "Вы получаете 10/15/20% шанс заблокировать 1/1/2 урона каждый ход."},
    }

allscrolls = [{'code':'shieldgen', 'name':'Генератор щитов', 'lvl':1}, {'code':'medic', 'name':'Медик', 'lvl':1},
              {'code':'zombie', 'name':'Зомби', 'lvl':1}, {'code':'bicepc', 'name':'Бицепс', 'lvl':1}, {'code':'sadist', 'name':'Садист', 'lvl':1},
              {'code':'berserk', 'name':'Берсерк', 'lvl':1}, {'code':'protivogaz', 'name':'Противогаз', 'lvl':1},
              {'code':'vor', 'name':'Вор', 'lvl':1}, {'code':'incvizitor', 'name':'Инквизитор', 'lvl':1},
              {'code':'pyrotech', 'name':'Пиротехник', 'lvl':1}, {'code':'cherep', 'name':'Крепкий череп', 'lvl':1}, {'code':'alchemist', 'name':'Алхимик', 'lvl':1},
              {'code':'ninja', 'name':'Ниндзя', 'lvl':1}, {'code':'inzhener', 'name':'Инженер', 'lvl':1}, {'code':'greedy', 'name':'Жадность', 'lvl':1},
              {'code':'goodsleep', 'name':'Здоровый сон', 'lvl':1}]

allrecipes = ['recipe_baseball', 'recipe_knife', 'recipe_obrez', 'recipe_torch', 'recipe_flamethrower', 'recipe_revolver']

allrecipes_red = ['recipe_baseball', 'recipe_obrez', 'recipe_bulava', 'recipe_chain', 'recipe_bow', 'recipe_claws', 'recipe_shurikens']
allrecipes_green = ['recipe_knife', 'recipe_torch', 'recipe_rifle', 'recipe_kastet', 'recipe_saber', 'recipe_saw', 'recipe_molot', 'recipe_tesak']
allrecipes_blue = ['recipe_flamethrower', 'recipe_revolver', 'recipe_axe', 'recipe_kuvalda', 'recipe_spear', 'recipe_police', 'recipe_shest']

weapons_to_sale = {
    'shortsword':{'code':'shortsword', 'name':'Короткий меч', 'lvl':1, 'cost':75, 'buy_command':'/buy_weapon_shortsword',
                  'cubes':3, 'accuracybonus':1, 'dmgbonus':0, 'energycost':2, 'ranged':False,
                  'description': "Обыкновенный меч. Не имеет никаких особенностей, но все же это лучше, чем голые кулаки."},

    'pistol':{'code':'pistol', 'name':'Пистолет', 'lvl':1, 'cost':200, 'buy_command':'/buy_weapon_pistol',
                  'cubes':3, 'accuracybonus':1, 'dmgbonus':0, 'energycost':3, 'ranged':True,
                  'description': "Дальнобойное оружие без эффектов."}
        
}

all_weapons = {
#    'baseball':{'code':'baseball', 'name':'Бита', 'lvl':1,
#                  'cubes':3, 'accuracybonus':1, 'dmgbonus':0, 'energycost':2, 'ranged':False,
#                  'description': "Имеет 10% шанс оглушить соперника при атаке."},

#    'revolver':{'code':'revolver', 'name':'Револьвер', 'lvl':1,
#                  'cubes':3, 'accuracybonus':1, 'dmgbonus':0, 'energycost':3, 'ranged':True,
#                  'description': "Всегда имеет стабильный урон."}

}

def get_cw_battleitem_name(result):
    if result == 'grenade':
        return '💣Граната'
    if result == 'adrenaline':
        return '💉Адреналин'
    if result == 'shield':
        return '🔵Щит'
    if result == 'flash':
        return '😵Световая граната'
    if result == 'dzet':
        return '💉Джет'
    if result == 'molotov':
        return '🍸Коктейль Молотова'
    if result == 'hitin':
        return '💉Хитин'
    if result == 'knife':
        return '🔪Метательный нож'
    return 'Неизвестно'


def name_to_weapon(code):
    if code == 'baseball':
        return 'Бита'
    if code == 'revolver':
        return 'Револьвер'
    if code == 'shortsword':
        return 'Короткий меч'
    if code == 'pistol':
        return 'Пистолет'
    if code == 'knife':
        return 'Нож'
    if code == 'obrez':
        return 'Обрез'
    if code == 'torch':
        return 'Факел'
    if code == 'flamethrower':
        return 'Огнемет'
    if code == 'rifle':
        return 'Снайперская винтовка'
    if code == 'axe':
        return 'Топор'
    if code == 'bulava':
        return 'Булава'
    if code == 'kastet':
        return 'Кастет'
    if code == 'kuvalda':
        return 'Кувалда'
    if code == 'chain':
        return 'Цепь'
    if code == 'spear':
        return 'Копье'
    if code == 'saber':
        return 'Сабля'
    if code == 'bow':
        return 'Лук'
    if code == 'claws':
        return 'Стальные когти'
    if code == 'saw':
        return 'Пиломет'
    if code == 'police':
        return 'Полицейская дубинка'
    if code == 'shurikens':
        return 'Сюрикены'
    if code == 'molot':
        return 'Молот'
    if code == 'shest':
        return 'Шест'
    if code == 'tesak':
        return 'Тесак'
    return 'Неизвестно'

def get_lvl_weapon(weapon, objectcode = None, code = None, lvl=None, need_create = False, modification = None):
    if need_create:
        name = name_to_weapon(code)
        if name == 'Неизвестно':
            return None
        weapon = create_weapon(None, objectcode, lite=True, name=name, code=code, lvl=lvl, modification = modification)
    if weapon['code'] == 'baseball':
        if weapon['lvl'] == 1:
            weapon['description'] = "Имеет 10% шанс оглушить соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Имеет 20% шанс оглушить соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Имеет 35% шанс оглушить соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Имеет 50% шанс оглушить соперника при атаке."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Имеет 35% шанс оглушить соперника при атаке на 2 хода."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'shortsword':
        if weapon['lvl'] == 1:
            weapon['description'] = "Обыкновенный меч. Не имеет никаких особенностей, но все же это лучше, чем голые кулаки."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Обыкновенный меч. Не имеет никаких особенностей, но все же это лучше, чем голые кулаки."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Обыкновенный меч. Не имеет никаких особенностей, но все же это лучше, чем голые кулаки."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Обыкновенный меч. Не имеет никаких особенностей, но все же это лучше, чем голые кулаки."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Обыкновенный меч. Не имеет никаких особенностей, но все же это лучше, чем голые кулаки. Полученный путем создания "+\
                    "эссенции меч имеет уникальное свойство - он может удлинняться, доставая даже соперников, не находящихся с вами в ближнем бою."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = True
    if weapon['code'] == 'revolver':
        if weapon['lvl'] == 1:
            weapon['description'] = "Всегда имеет стабильный урон."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 0
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 4
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "Всегда имеет стабильный урон."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "Всегда имеет стабильный урон."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Всегда имеет стабильный урон."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 0
                weapon['dmgbonus'] = 3
                weapon['energycost'] = 4
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "Всегда имеет стабильный урон."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = True
    if weapon['code'] == 'pistol':
        if weapon['lvl'] == 1:
            weapon['description'] = "Дальнобойное оружие без эффектов."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "Дальнобойное оружие без эффектов."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "Дальнобойное оружие без эффектов."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 3
            weapon['energycost'] = 3
            weapon['dmgbonus'] = 0
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Дальнобойное оружие без эффектов."
                weapon['cubes'] = 4
                weapon['accuracybonus'] = 3
                weapon['energycost'] = 3
                weapon['dmgbonus'] = 0
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "Дальнобойное оружие без эффектов."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['energycost'] = 2
                weapon['dmgbonus'] = 0
                weapon['ranged'] = True

    if weapon['code'] == 'knife':
        if weapon['lvl'] == 1:
            weapon['description'] = "Имеет 50% шанс наложить кровотечение на цель."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Имеет 70% шанс наложить кровотечение на цель."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Имеет 99% шанс наложить кровотечение на цель."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Имеет 99% шанс наложить кровотечение на цель. Кровотечение срабатывает в этот же ход."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Имеет 99% шанс наложить кровотечение на цель. Когда кровотечение отнимает жизнь у любого соперника, вы восстанавливаете хп."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False

    if weapon['code'] == 'obrez':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете совершить мощный выстрел, потратив всю оставшуюся энергию и нанося 1 дополнительный урон."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 0
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете совершить мощный выстрел, потратив всю оставшуюся энергию и нанося 1 дополнительный урон."
            weapon['cubes'] = 4
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете совершить мощный выстрел, потратив всю оставшуюся энергию и нанося 2 дополнительных урона."
            weapon['cubes'] = 4
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете совершить мощный выстрел, потратив всю оставшуюся энергию и нанося 2 дополнительных урона."
                weapon['cubes'] = 5
                weapon['accuracybonus'] = 1
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете совершить мощный выстрел, потратив всю оставшуюся энергию и нанося 2 дополнительных урона. Любой выстрел с шансом 75% накладывает кровотечение."
                weapon['cubes'] = 4
                weapon['accuracybonus'] = 1
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 3
                weapon['ranged'] = True

    if weapon['code'] == 'torch':
        if weapon['lvl'] == 1:
            weapon['description'] = "Имеет 25% шанс поджечь соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Имеет 40% шанс поджечь соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Имеет 60% шанс поджечь соперника при атаке. 15% шанс поджечь с силой 2."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Имеет 60% шанс поджечь соперника на 3 при атаке."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Имеет 60% шанс поджечь соперника на 5, а себя на 2 при атаке."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False

    if weapon['code'] == 'flamethrower':
        if weapon['lvl'] == 1:
            weapon['description'] = "С шансом 75% поджигает соперника при атаке."
            weapon['cubes'] = 2
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 4
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "С шансом 100% поджигает соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 4
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "С шансом 100% поджигает соперника при атаке."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "С шансом 100% поджигает соперника при атаке."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 2
                weapon['energycost'] = 3
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "С шансом 100% поджигает соперника на 2 при атаке. Не наносит урон."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 1
                weapon['ranged'] = True

    if weapon['code'] == 'rifle':
        if weapon['lvl'] == 1:
            weapon['description'] = "Имеет очень низкую точность без прицеливания. Тратой хода можно выцелить одного соперника, чтобы повысить шанс попадания в него."
            weapon['cubes'] = 1
            weapon['accuracybonus'] = -4
            weapon['dmgbonus'] = 6
            weapon['energycost'] = 5
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "Имеет очень низкую точность без прицеливания. Тратой хода можно выцелить одного соперника, чтобы повысить шанс попадания в него."
            weapon['cubes'] = 1
            weapon['accuracybonus'] = -4
            weapon['dmgbonus'] = 8
            weapon['energycost'] = 5
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "Имеет очень низкую точность без прицеливания. Тратой хода можно выцелить одного соперника, чтобы повысить шанс попадания в него."
            weapon['cubes'] = 1
            weapon['accuracybonus'] = -3
            weapon['dmgbonus'] = 10
            weapon['energycost'] = 5
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Имеет очень низкую точность без прицеливания. Тратой хода можно выцелить одного соперника, чтобы повысить шанс попадания в него. "+\
                    "С шансом 60% при атаке сначала прицелится без затраты хода а потом выстрелит."
                weapon['cubes'] = 1
                weapon['accuracybonus'] = -3
                weapon['dmgbonus'] = 10
                weapon['energycost'] = 5
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "Имеет очень низкую точность без прицеливания. Тратой хода можно выцелить одного соперника, чтобы повысить шанс попадания в него. "+\
                    "При промахе пуля попадает в другого случайного соперника."
                weapon['cubes'] = 1
                weapon['accuracybonus'] = -3
                weapon['dmgbonus'] = 10
                weapon['energycost'] = 5
                weapon['ranged'] = True
    if weapon['code'] == 'axe':
        if weapon['lvl'] == 1:
            weapon['description'] = "Имеет 40% шанс покалечить соперника, снижая его лимит получения урона для потери хп на 1."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Имеет 60% шанс покалечить соперника, снижая его лимит получения урона для потери хп на 1."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Имеет 80% шанс покалечить соперника, снижая его лимит получения урона для потери хп на 2."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Имеет 80% шанс покалечить соперника, снижая его лимит получения урона для потери хп на 4."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Имеет 80% шанс покалечить соперника, снижая его лимит получения урона для потери хп на 2."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 2
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'bulava':
        if weapon['lvl'] == 1:
            weapon['description'] = "За каждую атаку подряд получает +1 урона."
            weapon['cubes'] = 2
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "За каждую атаку подряд получает +1 урона."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "За каждую атаку подряд получает +2 урона."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "За каждую атаку подряд получает +2 урона. Каждые 3 хода постоянный бонус к урону увеличивается на 1."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "За каждую атаку подряд получает +4 урона."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 5
                weapon['ranged'] = False
    if weapon['code'] == 'kastet':
        if weapon['lvl'] == 1:
            weapon['description'] = "Если вы атаковали соперника, который перезаряжается, он потеряет 3 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Если вы атаковали соперника, который перезаряжается, он потеряет 4 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Если вы атаковали соперника, который перезаряжается, он потеряет 5 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Если вы атаковали соперника, который перезаряжается, он потеряет 5 энергии. Каждый удар дополнительно снимает сопернику 1 энергии."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Если вы атаковали соперника, который перезаряжается, он потеряет 5 энергии."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 2
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'kuvalda':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете сокрушить цель, нанося ей (1 + потраченная энергия цели) урона и затрачивая 5 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете сокрушить цель, нанося ей (1 + потраченная энергия цели) урона и затрачивая 4 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете сокрушить цель, нанося ей (2 + потраченная энергия цели) урона и затрачивая 3 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете сокрушить цель, нанося ей (2 + потраченная энергия цели*2) урона и затрачивая 3 энергии."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете сокрушить цель, нанося ей (2 + потраченная энергия цели) урона и затрачивая 3 энергии. Эта способность не имеет времени перезарядки."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 2
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'chain':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете попытаться выбить оружие из рук цели. Шанс выбить оружие: 10+(потраченная_энергия_цели*10). При перезарядке цели шанс 100%."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете попытаться выбить оружие из рук цели. Шанс выбить оружие: 20+(потраченная_энергия_цели*15). При перезарядке цели шанс 100%."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете попытаться выбить оружие из рук цели. Шанс выбить оружие: 30+(потраченная_энергия_цели*20). При перезарядке цели шанс 100%."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете попытаться выбить оружие из рук цели. Шанс выбить оружие: 100%. Перезарядка спец.способности на 1 ход быстрее."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете попытаться выбить оружие из рук цели. Шанс выбить оружие: 30+(потраченная_энергия_цели*20). При перезарядке цели шанс 100%. "+\
                    "При обычной атаке шанс выбить оружие равен 40%."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'spear':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете контратаковать всех соперников, которые атаковали вас в ход применения этой способнсти, затрачивая в сумме 1 энергию и получая +1 к урону."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете контратаковать всех соперников, которые атаковали вас в ход применения этой способнсти, затрачивая в сумме 1 энергию и получая +2 к урону."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете контратаковать всех соперников, которые атаковали вас в ход применения этой способнсти, затрачивая в сумме 1 энергию, получая +3 к урону и +1 к точности."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете контратаковать всех соперников, которые атаковали вас в ход применения этой способнсти, затрачивая в сумме 1 энергию, "+\
                                        "получая +3 к урону и +1 к точности. Контратака пассивно срабатывает на случайную атакующую вас цель раз в 10 ходов."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете контратаковать всех соперников, которые атаковали вас в ход применения этой способнсти, затрачивая в сумме 1 энергию, получая +3 к урону и +1 к точности."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 4
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'saber':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете парировать атаку соперника, если он атаковал вас, блокируя весь его урон и отнимая у него 4 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете парировать атаку соперника, если он атаковал вас, блокируя весь его урон и отнимая всю его энергию."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете парировать атаку соперника, если он атаковал вас, блокируя весь его урон и отнимая всю его энергию. Соперник получит оглушение."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете парировать атаку соперника, если он атаковал вас, блокируя весь его урон и отнимая всю его энергию. Соперник получит оглушение."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 1
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете парировать атаку соперника, если он атаковал вас, блокируя весь его урон и отнимая всю его энергию. Соперник получит оглушение, "+\
                    "а вы восстановите всю энергию. Парирование накладывает на вас щит."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
    if weapon['code'] == 'bow':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете запустить в соперника огненную стрелу, поджигающую цель на 1."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете запустить в соперника огненную стрелу, поджигающую цель на 2."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете запустить в соперника огненную стрелу, поджигающую цель на 3."
            weapon['cubes'] = 4
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете запустить в соперника огненную стрелу, поджигающую цель на 6."
                weapon['cubes'] = 4
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 3
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете запустить в соперника огненную стрелу, поджигающую цель на 3. Обычная атака поджигает цель на такую же величину с шансом 40%."
                weapon['cubes'] = 4
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 3
                weapon['ranged'] = True

    if weapon['code'] == 'claws':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете выпустить стальные когти, чтобы увеличить минимальный урон на 1 и максимальный урон на 1, но увеличить затрату энергии на 1."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете выпустить стальные когти, чтобы увеличить минимальный урон на 1 и максимальный урон на 2, но увеличить затрату энергии на 1."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете выпустить стальные когти, чтобы увеличить минимальный урон на 2 и максимальный урон на 2, но увеличить затрату энергии на 1."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете выпустить стальные когти, чтобы увеличить минимальный урон на 2 и максимальный урон на 2, но увеличить затрату энергии на 1. "+\
                    "С шансом 25% оружие наносит удвоенный урон."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете выпустить стальные когти, чтобы увеличить минимальный урон на 2 и максимальный урон на 4, но увеличить затрату энергии на 1."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False

    if weapon['code'] == 'saw':
        if weapon['lvl'] == 1:
            weapon['description'] = "При атаке имеется 50% шанс ранить соперника, увеличивая весь входящий по нему урон от атак на 1 до конца игры."
            weapon['cubes'] = 2
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "При атаке имеется 60% шанс ранить соперника, увеличивая весь входящий по нему урон от атак на 1 до конца игры."
            weapon['cubes'] = 2
            weapon['accuracybonus'] = 3
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "При атаке имеется 70% шанс ранить соперника, увеличивая весь входящий по нему урон от атак на 2 до конца игры."
            weapon['cubes'] = 2
            weapon['accuracybonus'] = 3
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "При атаке имеется 70% шанс ранить соперника, увеличивая весь входящий по нему урон от атак на 2-4 до конца игры."
                weapon['cubes'] = 2
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 3
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "При атаке имеется 70% шанс ранить соперника, увеличивая весь входящий по нему урон от атак на 2 до конца игры."
                weapon['cubes'] = 2
                weapon['accuracybonus'] = 4
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = True

    if weapon['code'] == 'police':
        if weapon['lvl'] == 1:
            weapon['description'] = "Каждая атака отнимает у соперника 1 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Каждая атака отнимает у соперника 1 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Каждая атака отнимает у соперника 2 энергии."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Каждая атака отнимает у соперника 2 энергии."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 2
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Каждая атака отнимает у соперника 2 энергии. Если в конце хода у цели не осталось энергии - она получает оглушение."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False

    if weapon['code'] == 'shurikens':
        if weapon['lvl'] == 1:
            weapon['description'] = "У вас с начала игры есть 2 сюрикена. За ход можно бросить один или два в одну цель, "+\
            "на второй бросок тратится одна энергия. Когда сюрикены израсходованы - их надо подобрать, потратив ход."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = True
        if weapon['lvl'] == 2:
            weapon['description'] = "У вас с начала игры есть 4 сюрикена. За ход можно бросить один или два в одну цель, " + \
                                 "на второй бросок тратится одна энергия. Когда сюрикены израсходованы - их надо подобрать, потратив ход."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = True
        if weapon['lvl'] == 3:
            weapon['description'] = "У вас с начала игры есть 6 сюрикенов. За ход можно бросить один или два в одну цель, " + \
                                 "на второй бросок тратится одна энергия. Когда сюрикены израсходованы - их надо подобрать, потратив ход."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 3
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = True
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "У вас с начала игры есть 6 сюрикенов. За ход можно бросить один или два в одну цель, " + \
                                     "на второй бросок тратится одна энергия. Когда сюрикены израсходованы - их надо подобрать, потратив ход. Сюрикен наносит 3 урона."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = True
            elif weapon['modification'] == 2:
                weapon['description'] = "У вас с начала игры есть бесконечное число сюрикенов. За ход можно бросить один или два в одну цель, " + \
                                     "на второй бросок тратится одна энергия. Когда сюрикены израсходованы - их надо подобрать, потратив ход."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = True

    if weapon['code'] == 'molot':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете нанести точный удар по цели с максимальным уроном и без возможности промахнуться, потратив 5 энергии. "+\
            "За каждые две отсутствующие у вас единицы энергии вы получаете +1 к урону к любым атакам."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете нанести точный удар по цели с максимальным уроном и без возможности промахнуться, потратив 4 энергии. " + \
                                 "За каждые две отсутствующие у вас единицы энергии вы получаете +1 к урону к любым атакам."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете нанести точный удар по цели с максимальным уроном и без возможности промахнуться, потратив 4 энергии. " + \
                                 "За каждые две отсутствующие у вас единицы энергии вы получаете +2 к урону к любым атакам."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете нанести точный удар по цели с максимальным уроном и без возможности промахнуться, потратив 4 энергии. " + \
                                     "За каждые две отсутствующие у вас единицы энергии вы получаете +3 к урону к любым атакам."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 3
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете нанести точный удар по цели с максимальным уроном и без возможности промахнуться, потратив 4 энергии. " + \
                                     "У этой способности нет времени перезарядки. За каждые две отсутствующие у вас единицы энергии вы получаете +2 к урону к любым атакам."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False

    if weapon['code'] == 'shest':
        if weapon['lvl'] == 1:
            weapon['description'] = "Вы можете сбить с ног цель. Эту атаку можно применить не подходя к цели вплотную. Если цель перекатывается или ставит щит - она не упадет."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Вы можете сбить с ног цель. Эту атаку можно применить не подходя к цели вплотную. Если цель ставит щит - она не упадет."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Вы можете сбить с ног цель. Эту атаку можно применить не подходя к цели вплотную."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 1
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Вы можете сбить с ног цель. Эту атаку можно применить не подходя к цели вплотную. С шансом 40% применяет эту способность при обычной атаке."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Вы можете сбить с ног цель. Эту атаку можно применить не подходя к цели вплотную. Оглушает цель."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 1
                weapon['energycost'] = 2
                weapon['ranged'] = False

    if weapon['code'] == 'tesak':
        if weapon['lvl'] == 1:
            weapon['description'] = "Изначально имеет бонус урона 3. За первое попадание по врагу бонус сокращается на 2, за последующие - на 1, до тех пор, пока не станет равным 0."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 1
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 3
            weapon['ranged'] = False
        if weapon['lvl'] == 2:
            weapon['description'] = "Изначально имеет бонус урона 4. За первое попадание по врагу бонус сокращается на 2, за последующие - на 1, до тех пор, пока не станет равным 0."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 3:
            weapon['description'] = "Изначально имеет бонус урона 5. За первое попадание по врагу бонус сокращается на 2, за последующие - на 1, до тех пор, пока не станет равным 0."
            weapon['cubes'] = 3
            weapon['accuracybonus'] = 2
            weapon['dmgbonus'] = 0
            weapon['energycost'] = 2
            weapon['ranged'] = False
        if weapon['lvl'] == 4:
            if weapon['modification'] == 1:
                weapon['description'] = "Изначально имеет бонус урона 10. За первое попадание по врагу бонус сокращается до 4, за последующие - на 1, до тех пор, "+\
                                        "пока не станет равным 0."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False
            elif weapon['modification'] == 2:
                weapon['description'] = "Изначально имеет бонус урона 5. За первое попадание по врагу бонус сокращается на 2, за последующие - на 1, до тех пор, "+\
                                        "пока не станет равным 0. Первый удар наносит урон сквозь броню, уворот и любые щиты и попадает по цели даже без энергии."
                weapon['cubes'] = 3
                weapon['accuracybonus'] = 2
                weapon['dmgbonus'] = 0
                weapon['energycost'] = 2
                weapon['ranged'] = False

    return weapon


def get_cw_player_weapon(user):
    w = cw_weaponlist.Fist_1()
    if user['weapon'] == None:
        w = cw_weaponlist.Fist_1()
        return w
    if user['weapon']['name'] == 'Короткий меч':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.ShortSword_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.ShortSword_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.ShortSword_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.ShortSword_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.ShortSword_4_2()

    if user['weapon']['name'] == 'Бита':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Baseball_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Baseball_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Baseball_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Baseball_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Baseball_4_2()

    if user['weapon']['name'] == 'Револьвер':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Revolver_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Revolver_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Revolver_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Revolver_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Revolver_4_2()

    if user['weapon']['name'] == 'Пистолет':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Pistol_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Pistol_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Pistol_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Pistol_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Pistol_4_2()

    if user['weapon']['name'] == 'Нож':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Knife_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Knife_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Knife_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Knife_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Knife_4_2()

    if user['weapon']['name'] == 'Обрез':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Obrez_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Obrez_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Obrez_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Obrez_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Obrez_4_2()

    if user['weapon']['name'] == 'Факел':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Torch_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Torch_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Torch_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Torch_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Torch_4_2()

    if user['weapon']['name'] == 'Огнемет':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Flamethrower_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Flamethrower_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Flamethrower_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Flamethrower_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Flamethrower_4_2()

    if user['weapon']['name'] == 'Снайперская винтовка':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Rifle_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Rifle_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Rifle_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Rifle_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Rifle_4_2()

    if user['weapon']['name'] == 'Топор':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Axe_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Axe_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Axe_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Axe_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Axe_4_2()

    if user['weapon']['name'] == 'Булава':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Bulava_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Bulava_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Bulava_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Bulava_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Bulava_4_2()

    if user['weapon']['name'] == 'Кастет':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Kastet_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Kastet_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Kastet_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Kastet_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Kastet_4_2()

    if user['weapon']['name'] == 'Кувалда':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Kuvalda_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Kuvalda_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Kuvalda_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Kuvalda_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Kuvalda_4_2()

    if user['weapon']['name'] == 'Цепь':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Chain_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Chain_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Chain_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Chain_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Chain_4_2()

    if user['weapon']['name'] == 'Копье':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Spear_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Spear_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Spear_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Spear_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Spear_4_2()

    if user['weapon']['name'] == 'Сабля':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Saber_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Saber_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Saber_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Saber_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Saber_4_2()

    if user['weapon']['name'] == 'Лук':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Bow_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Bow_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Bow_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Bow_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Bow_4_2()

    if user['weapon']['name'] == 'Стальные когти':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Claws_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Claws_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Claws_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Claws_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Claws_4_2()

    if user['weapon']['name'] == 'Пиломет':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Saw_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Saw_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Saw_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Saw_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Saw_4_2()

    if user['weapon']['name'] == 'Полицейская дубинка':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Police_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Police_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Police_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Police_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Police_4_2()

    if user['weapon']['name'] == 'Сюрикены':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Shurikens_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Shurikens_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Shurikens_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Shurikens_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Shurikens_4_2()

    if user['weapon']['name'] == 'Молот':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Molot_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Molot_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Molot_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Molot_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Molot_4_2()

    if user['weapon']['name'] == 'Шест':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Shest_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Shest_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Shest_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Shest_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Shest_4_2()

    if user['weapon']['name'] == 'Тесак':
        if user['weapon']['lvl'] == 1:
            w = cw_weaponlist.Tesak_1()
        if user['weapon']['lvl'] == 2:
            w = cw_weaponlist.Tesak_2()
        if user['weapon']['lvl'] == 3:
            w = cw_weaponlist.Tesak_3()
        if user['weapon']['lvl'] == 4:
            if user['weapon']['modification'] == 1:
                w = cw_weaponlist.Tesak_4_1()
            elif user['weapon']['modification'] == 2:
                w = cw_weaponlist.Tesak_4_2()

    return w

def create_scroll(scroll, objectcode):
    x = {
        'name':scroll['name'],
        'code':scroll['code'],
        'lvl':scroll['lvl'],
        'type':'scroll',
        'objectcode':objectcode,
        #'use_command':scroll['use_command'],
        'description':'Использование позволяет изучить навык ('+scroll['name']+') '+str(scroll['lvl'])+'го уровня. Просмотр информации о навыке - '+\
        '/skillinfo_'+scroll['code']+'_1 (подставить число от 1 до 3 в соответствии с уровнем навыка).'
    }
    return x

def create_essence(objectcode, weaponcode, name, modification):
    x = {
        'name': name,
        'code': weaponcode,
        'type': 'essence',
        'objectcode': objectcode,
        'modification':modification,
        'kills':0,
        'description': 'Когда эта эссенция накопит силу ста жертв, она превратится в оружие.'
    }
    return x

def create_undefined_scroll(objectcode, name):
    x = {
        'name':name,
        'code':'uscroll',
        'type':'undefined_scroll',
        'objectcode':objectcode,
        #'use_command':scroll['use_command'],
        'description':'Свиток неизвестной способности. Посетите лавку в замке, чтобы расшифровать его.'
    }
    return x

def create_recipe(recipecode, objectcode, recipename, undefined=True, color="blue"):
    rtype = 'undefined_recipe'
    if not undefined:
        rtype = 'recipe'
    return {
        'name':recipename,
        'code':recipecode,
        'type':rtype,
        'objectcode':objectcode,
        'color':color
        
    }

def create_skill(name, skillcode, lvl):
    x = {
        'name':name,
        'skillcode':skillcode,
        'lvl':lvl,
        'type':'skill'
    }
    return x

def create_weapon(weapon, objectcode, lite = False, name = None, code = None, lvl = None, modification = None):
    if lite:
        x = {
            'name':name,
            'code':code,
            'type':'weapon',
            'lvl':lvl,
            'objectcode':objectcode,
            'modification':modification,
            'kills':0
        }
    else:
        x = {
            'name':weapon['name'],
            'code':weapon['code'],
            'type':'weapon',
            'lvl':weapon['lvl'],
            'cubes':weapon['cubes'],
            'accuracybonus':weapon['accuracybonus'],
            'dmgbonus':weapon['dmgbonus'],
            'energycost':weapon['energycost'],
            'ranged':weapon['ranged'],
            'objectcode':objectcode,
            #'use_command':scroll['use_command'],
            'description':weapon['description'],
            'modification': modification,
            'kills':0
        }
    return x

def generate_object_code(user):
    symbols = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    exist_codes = []
    for ids in user['inventory']:
        exist_codes.append(user['inventory'][ids]['objectcode'])
    if user['weapon'] != None:
        exist_codes.append(user['weapon']['objectcode'])
    if user['weapon_for_battle'] != None:
        exist_codes.append(user['weapon_for_battle']['objectcode'])
    new_code = ""
    while len(new_code) < 5:
        x = random.choice(symbols)
        if random.randint(1, 100) <= 50:
            x = x.capitalize()
        new_code += x
    while new_code in exist_codes:
        new_code = ""
        while len(new_code) < 5:
            x = random.choice(symbols)
            if random.randint(1, 100) <= 50:
                x = x.capitalize()
            new_code += x
    return new_code
