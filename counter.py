import traceback
from telebot import types, TeleBot
import time
import threading
import telebot
import os
from pymongo import MongoClient

token = ''
bot = TeleBot(token)

print('trying to connect...')
client=MongoClient('')
db=client.computer_counter
hours = db.hours
print('Success!')

x = hours.find_one({})
if 'month_started' not in x:
    hours.update_one({},{'$set':{'month_started':time.time(), 'month_el':0, 'month_eg':0}})
if 'show_hint_el' not in x:
    hours.update_one({},{'$set':{'show_hint_eg':None, 'show_hint_el':None}})
if 'shutdown_el' not in x:
    hours.update_one({},{'$set':{'shutdown_el':False, 'shutdown_eg':False}})

turned_on_eg = False
turned_on_el = False
timefromstart = 0
      
@bot.message_handler(commands = ['time'])
def gettimee(m):
    timeee(m)


def timeee(m = None):
  try:
    if m != None:
        if m.from_user.id not in [441399484, 314238081, 1029744076, 1222566089]:
            return
    text = ''
    x = hours.find_one({})
    hourss = 0
    mins = x['el']
    while mins >= 60:
        mins -= 60
        hourss += 1
    lastact_secs = time.time() - x['lastact_el']
    lastact_mins = 0
    lastact_hours = 0
    while lastact_secs >= 60:
        lastact_mins += 1
        lastact_secs -= 60
    while lastact_mins >= 60:
        lastact_hours += 1
        lastact_mins -= 60
    lastact = str(lastact_hours)+'ч '+str(lastact_mins)+'м '+str(int(lastact_secs))+'с назад'
    days = 0
    weeksecs = time.time() - x['week_started']
    weekhours = 0
    while weeksecs >= 86400:
        weeksecs -= 86400
        days += 1
    while weeksecs >= 3600:
        weekhours += 1
        weeksecs -= 3600
    weekresult = ''
    weekmins = x['week_el']
    weekhours_count = 0
    while weekmins >= 60:
        weekhours_count += 1
        weekmins -= 60
    weekresult += str(weekhours_count)+'ч '+str(weekmins)+'м'

    #days = 0
    #monthsecs = time.time() - x['month_started']
    #monthhours = 0
    #while monthsecs >= 86400:
    #    monthsecs -= 86400
     #   days += 1
    #while monthsecs >= 3600:
    #    monthhours += 1
    #    monthsecs -= 3600
    #monthresult = ''
    #monthmins = x['week_el']
    #monthhours_count = 0
    #while monthmins >= 60:
    #    monthhours_count += 1
    #    monthmins -= 60
    #monthresult += str(monthhours_count) + 'ч ' + str(monthmins) + 'м'

    dop_secs = x['el_doptime']
    dop_mins = 0
    dop_hours = 0
    while dop_secs >= 60:
        dop_mins += 1
        dop_secs -= 60
    while dop_mins >= 60:
        dop_hours += 1
        dop_mins -= 60
    dop = str(dop_hours) + 'ч ' + str(dop_mins) + 'м ' + str(int(dop_secs)) + 'с'

    text += '🔵Елисей (всего): '+str(hourss)+'ч '+str(mins)+'м\n🟠Елисей (за последние '+str(days)+'д '+str(weekhours)+'ч): '+weekresult+'\n'+\
            '💬Последняя активность: '+lastact+'\n➕Дополнительное время: '+dop+'\n\n'
    mins = x['eg']
    hourss = 0
    while mins >= 60:
        mins -= 60
        hourss += 1
    lastact_secs = time.time() - x['lastact_eg']
    lastact_mins = 0
    lastact_hours = 0
    while lastact_secs >= 60:
        lastact_mins += 1
        lastact_secs -= 60
    while lastact_mins >= 60:
        lastact_hours += 1
        lastact_mins -= 60
    lastact = str(lastact_hours)+'ч '+str(lastact_mins)+'м '+str(int(lastact_secs))+'с назад'
    weekmins = x['week_eg']
    weekhours_count = 0
    while weekmins >= 60:
        weekhours_count += 1
        weekmins -= 60
    weekresult = ''
    weekresult += str(weekhours_count)+'ч '+str(weekmins)+'м'

    dop_mins = x['eg_doptime']
    dop_hours = 0
    #while dop_secs >= 60:
    #    dop_mins += 1
    #    dop_secs -= 60
    while dop_mins >= 60:
        dop_hours += 1
        dop_mins -= 60
    dop = str(dop_hours) + 'ч ' + str(dop_mins) + 'м ' + str(int(dop_secs)) + 'с'

    text += '🔵Егор (всего): '+str(hourss)+'ч '+str(mins)+'м\n🟠Егор (за последние '+str(days)+' дней '+str(weekhours)+'ч): '+weekresult+'\n'+\
            '💬Последняя активность: '+lastact+'\n➕Дополнительное время: '+dop
    if m != None:
        bot.send_message(m.chat.id, text)
    else:
        bot.send_message(441399484, text)
  except:
    bot.send_message(441399484, traceback.format_exc())
    
@bot.message_handler(commands = ['send_message_el'])
def sendmmmsage(m):
    if m.from_user.id not in [441399484, 314238081, 1029744076, 1222566089]:
        return
    if m.from_user.id == 441399484:
        name = 'Егор'
    else:
        name = m.from_user.first_name
    x = hours.find_one({})
    if time.time() - x['lastact_el'] > 70:
        bot.send_message(m.chat.id, 'Аккаунт пользователя не в сети!')
        return
    try:
        msg = m.text.split(' ', 1)[1]
    except:
        bot.send_message(m.chat.id, 'Необходимо указать сообщение после команды!')
        return
    hours.update_one({},{'$set':{'show_hint_el':[name, msg]}})
    bot.send_message(m.chat.id, 'Сообщение придет пользователю "Елисей" в течение 10 секунд!')
    
@bot.message_handler(commands = ['shutdown_eg'])
def sendmmmsage(m):
    if m.from_user.id not in [441399484, 314238081, 1029744076, 1222566089]:
        return
    x = hours.find_one({})
    if time.time() - x['lastact_eg'] > 70:
        bot.send_message(m.chat.id, 'Аккаунт пользователя не в сети!')
        return
    hours.update_one({},{'$set':{'shutdown_eg':True}})
    bot.send_message(m.chat.id, 'Компьютер будет выключен!')
    
    
@bot.message_handler(commands = ['send_message_eg'])
def sendmmmsage(m):
    if m.from_user.id not in [441399484, 314238081, 1029744076, 1222566089]:
        return
    if m.from_user.id == 441399484:
        name = 'Егор'
    else:
        name = m.from_user.first_name
    x = hours.find_one({})
    if time.time() - x['lastact_eg'] > 70:
        bot.send_message(m.chat.id, 'Аккаунт пользователя не в сети!')
        return
    try:
        msg = m.text.split(' ', 1)[1]
    except:
        bot.send_message(m.chat.id, 'Необходимо указать сообщение после команды!')
        return
    hours.update_one({},{'$set':{'show_hint_eg':[name, msg]}})
    bot.send_message(m.chat.id, 'Сообщение придет пользователю "Егор" в течение 10 секунд!')
    
def check_week():
    global turned_on_eg
    global turned_on_el
    global timefromstart
    x = hours.find_one({})
    if time.time() - x['week_started'] >= (86400*7):
        timeee()
        hours.update_one({},{'$set':{'week_started':time.time(), 'week_el':0, 'week_eg':0}})
    if time.time() - x['month_started'] >= (86400*30):
        hours.update_one({},{'$set':{'month_started':time.time(), 'month_el':0, 'month_eg':0}})
    if time.time() - x['lastact_eg'] >= 300:
        if turned_on_eg:
            turned_on_eg = False
            if timefromstart > 6:
                bot.send_message(441399484, 'Computer turned off: EG')
    else:
        turned_on_eg = True
    if time.time() - x['lastact_el'] >= 300:
        if turned_on_el:
            turned_on_el = False
            if timefromstart > 6:
                bot.send_message(441399484, 'Computer turned off: EL')
    else:
        turned_on_el = True
    timefromstart += 1
    threading.Timer(60, check_week).start()


    
check_week()
    
        
