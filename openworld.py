import random
from telebot import types
import traceback

def generate_open_world(size = 50):
    openw = {}
    maxx = size
    maxy = size
    x = 0
    xi = 0
    while x <= maxx:
        y = 0
        yi = 0
        while y <= maxy:
            obj = 'free'
            if x == 0 or y == 0 or xi == maxx or yi == maxy:
                obj = 'wall'
            if random.randint(1, 100) <= 6:
                if yi > 1 and xi > 1 and yi < maxy-1 and xi < maxx-1:
                    obj = 'wall'
            openw.update({str(x)+'_'+str(y):{'object':obj, 'player':None, 'fight':False, 'home':False}})
            y += 1
            yi += 1
        x += 1
        xi += 1
    return openw

def place_new_player(user, ow):
    maxx = 0
    maxy = 0
    for ids in ow['world']:
        x = int(ids.split('_')[0])
        y = int(ids.split('_')[1])
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
    locs = []
    for ids in ow['world']:
        x = int(ids.split('_')[0])
        y = int(ids.split('_')[1])
        if x == 0 or y == 0 or x == maxx or y == maxy:
            if (x == 0 and y == 0) or (x == maxx and y == maxy):
                continue
            if ow['world'][ids]['home'] == False:
                locs.append(ids)
    pos = random.choice(locs)
    return pos

def get_player_keyboard(user, w):
    pos = user['worldpos']
    px = int(pos.split('_')[0])
    py = int(pos.split('_')[1])
    radius = 2
    kb = types.InlineKeyboardMarkup(row_width = 5)
    y = py - radius
    while y <= py+radius:
        x = px - radius
        kbs = []
        while x <= px + radius:
            try:
                checkpos = w['world'][str(x)+'_'+str(y)]
                text = '⬜️'
                if checkpos['object'] == 'wall':
                    text = '⬛️'
                if checkpos['player'] != None:
                    text = '🔴'
                    if checkpos['player'] == user['id']:
                        text = '🟡'
                    if str(checkpos['player']) in w['npc']:
                        if 'Крыса' in w['npc'][str(checkpos['player'])]['name']:
                            text = '🐭'
                        if 'Носорог' in w['npc'][str(checkpos['player'])]['name']:
                            text = '🦏'
                        if 'Скелет' in w['npc'][str(checkpos['player'])]['name']:
                            text = '💀'
                if checkpos['home'] != False:
                    text = '🟢'
            except:
                #print(traceback.format_exc())
                text = '⬛️'
            kbs.append(types.InlineKeyboardButton(text = text, callback_data = 'click?'+str(x)+'_'+str(y)))
            x += 1
        kb.add(*kbs)
        y += 1
    return kb
        

