import folium
import pyfiglet
import traceback
import requests
import json
import os
import telebot

bot = telebot.TeleBot('')

allow = [441399484, 524034660]



def get_info(ip = '127.0.0.1'):
    try:
        response = requests.get(url='http://ip-api.com/json/'+ip).json()
        
        data = {
        '[IP]':response.get('query'),
        '[Провайдер]':response.get('isp'),
        '[Организация]':response.get('org'),
        '[Страна]':response.get('country'),
        '[Регион]':response.get('regionName'),
        '[Город]':response.get('city'),
        '[Почтовый индекс]':response.get('zip'),
        '[Ширина]':response.get('lat'),
        '[Долгота]':response.get('lon')
        }
        
        text = ''
        for k, v in data.items():
            print(str(k)+' : '+str(v))
            text += str(k)+' : '+str(v)+'\n'
        path = None
        if response.get("lat") != None and response.get('lon') != None:
            area = folium.Map(location = [response.get('lat'), response.get('lon')], zoom_start = 18)
            folium.Marker(location=[response.get('lat'), response.get('lon')], popup=str("Here it is!"), icon=folium.Icon(color = 'green')).add_to(area)
            area.save(str(response.get("query"))+'_'+str(response.get('city'))+'.html')
            print('Карта сохранена в папку скрипта!\n')
            path = str(response.get("query"))+'_'+str(response.get('city'))+'.html'
            
        else:
            pass
        return text, path
    except:
        print('Проверьте соединение и повторите запрос! Описание ошибки:\n')
        print(traceback.format_exc())
        
        
@bot.message_handler(commands = ['info'])
def infff(m):
    if m.from_user.id not in allow:
        return
    try:
        ip = m.text.split(' ')[1]
    except:
        bot.send_message(m.chat.id, 'Напишите команду в следующем формате:\n/info *ip*', parse_mode = 'markdown')
        return
    text, path = get_info(ip)  
    bot.send_message(m.chat.id, text)
    if path != None:
        try:
            p = os.path.abspath(path)
            uis_pdf = open(p, 'rb')
            bot.send_document(m.chat.id, uis_pdf)
            uis_pdf.close()
        except:
            print(traceback.format_exc())
        

