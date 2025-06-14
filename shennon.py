import random
#from tkinter import *
#root = Tk()
#btn1 = Button(root, text="")
#btn.config(command=lambda: print("Привет, Tkinter!"))
#import telebot
#from telebot import types
#bot = telebot.TeleBot("5411126548:AAEi5SIYevtm4jCyMb4QFKCkTebsB_i5dJc")

games = {}

@bot.message_handler(commands = ['allgames'])
def allgames(m):
    if m.from_user.id != 441399484:
        return

    text = ''
    for ids in games:
        text += 'Игрок: '+games[ids]['name']+'\nСчет: '+str(games[ids]['score'])+'\n\n'
    if text == '':
        text = 'Нет активных игр.'
    bot.send_message(m.chat.id, text)
    

@bot.message_handler()
def allm(m):
    if m.chat.id not in games:
        games.update({m.chat.id:{'demons':{}, 'user_answers':[], 'score':0, 'name':m.from_user.first_name}})
        bot.send_message(441399484, m.from_user.first_name+" начал игру!")
        for i in range(10000):
            cdemon = {}
            for d1 in range(2):
                for d2 in range(2):
                    for d3 in range(2):
                        for d4 in range(2):
                            for d5 in range(2):
                                cdemon.update({str(d1)+str(d2)+str(d3)+str(d4)+str(d5):random.randint(0, 1)})
            games[m.chat.id]['demons'].update({i:{'choices':cdemon, 'score':0}})
    
    if m.text not in ["0", "1"]:
        bot.send_message(m.chat.id, "Введите число от 0 до 1 а я попытаюсь его отгадать. "+\
                         "Цель - набрать 50 очков. Если вы уйдете в минус 50 очков - демон "+\
                         "победит и игра сбросится. Ваш счет: "+str(games[m.chat.id]['score']))
    else:
        game_tg(m, int(m.text))


demons = {}
user_answers = []

def create_demon():
    d = random.randint(1, 100)
    demons.append(d)

bdlen = 5

for i in range(100):
    cdemon = {}
    for d1 in range(2):
        for d2 in range(2):
            for d3 in range(2):
                for d4 in range(2):
                    for d5 in range(2):
                        cdemon.update({str(d1)+str(d2)+str(d3)+str(d4)+str(d5):random.randint(0, 1)})
    demons.update({i:{'choices':cdemon, 'score':0}})
    #print(i)

copies = 0
for ids in demons:
    for idss in demons:
        if demons[ids] == demons[idss] and ids != idss:
            copies += 1
print(copies)
                                      
                                    
#print(demons)
        

while len(demons) < 100:
    create_demon()

checklen = 5

def game_tg(m, ua):
        game = games[m.chat.id]
        if len(game['user_answers']) < checklen:
            demon_answer = random.choice([0,1])
        else:
            #print("1")
            top_demons = []
            top_demon_score = -1
            last_user_answers = []
            x = -1
            while len(last_user_answers) < checklen:
                      last_user_answers.append(game['user_answers'][x])
                      x -= 1
                                               
            for ids in game['demons']:
                demon = game['demons'][ids]
                if demon['score'] >= top_demon_score:
                    top_demon_score = demon['score']
            for ids in game['demons']:
                demon = game['demons'][ids]
                if demon['score'] == top_demon_score:
                    top_demons.append(demon)
            demon = random.choice(top_demons)

            string = ''
            for ids in last_user_answers:
                string += str(ids)
            demon_answer = demon['choices'][string]

        if len(game['user_answers']) >= checklen:
            for ids in game['demons']:
                demon = game['demons'][ids]
                if demon['choices'][string] == ua:
                    demon['score'] += 1
                else:
                    demon['score'] -= 1
        kb = types.ReplyKeyboardMarkup()
        kb.add("0", "1")
        if demon_answer == ua:
            game['score'] -= 1
            bot.send_message(m.chat.id, "Demon wins. Score: "+str(game['score']), reply_markup = kb)
        else:
            game['score'] +=1 
            bot.send_message(m.chat.id,"User wins. Score: "+str(game['score']), reply_markup = kb)
        if game['score'] <= -50:
            bot.send_message(m.chat.id,"Демон победил!")
            bot.send_message(441399484, "Демон победил игрока "+m.from_user.first_name+"!")
            del games[m.chat.id]
            return
        if game['score'] >= 50:
            bot.send_message(m.chat.id,"Игрок победил!")
            bot.send_message(441399484, "Игрок "+m.from_user.first_name+" победил демона!")
            del games[m.chat.id]
            return
        game['user_answers'].append(ua)

        

score = 0
def game():
    while True:
        ua = "h"
        while ua not in ["0", "1"]:
            ua = input("Введите 0 или 1: ")
        ua = int(ua)
        if len(user_answers) < checklen:
            demon_answer = random.choice([0,1])
        else:
            top_demons = []
            top_demon_score = -1
            last_user_answers = []
            x = -1
            while len(last_user_answers) < checklen:
                      last_user_answers.append(user_answers[x])
                      x -= 1
            #print(last_user_answers)
                                               
            for ids in demons:
                demon = demons[ids]
                if demon['score'] >= top_demon_score:
                    top_demon_score = demon['score']
            for ids in demons:
                demon = demons[ids]
                if demon['score'] == top_demon_score:
                    top_demons.append(demon)
            demon = random.choice(top_demons)

            string = ''
            for ids in last_user_answers:
                string += str(ids)
            demon_answer = demon['choices'][string]

        if len(user_answers) >= checklen:
            for ids in demons:
                demon = demons[ids]
                if demon['choices'][string] == ua:
                    demon['score'] += 1
                else:
                    demon['score'] -= 1
        if demon_answer == ua:
            score -= 1
            print("Demon wins. Score: "+str(score))
        else:
            score +=1 
            print("User wins. Score: "+str(score))
        if score <= -50:
            print("Демон победил!")
            break
        if score >= 50:
            print("Игрок победил!")
            break
        user_answers.append(ua)


#game()

#bot.infinity_polling()


        
            
