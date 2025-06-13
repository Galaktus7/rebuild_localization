
import parser.parse_log_statistic

from pyrogram import Client
import traceback
import requests
import time
import json
import threading

from pyrogram.enums import MessageEntityType

api_hash = 'eb2132dac2bbaadd0b4a1392ecb5a54d'
api_id = '28011569'
userbot = Client("logreader", api_id, api_hash)
from parser.parse_log_statistic import API_TOKEN

def send_data(players):
    #print(players)
    #data = {
    #    "token": API_TOKEN,
    #    "data": players,
    #}
    data = players
    request = requests.Request(
        method='POST',
        url='https://cw5map.fun/api/update_battle_data',
        json=data
    )
    prepped = request.prepare()

    with requests.Session() as session:
        resp = session.send(
            prepped,
            verify=False,
        )
        print(resp.text)


@userbot.on_message()
def msgsssss(userbot, m):
    
    try:
        if m.from_user != None:
            if m.from_user.id == 441399484:
                if m.text.lower() in ["ping", "/ping"]:
                    userbot.send_message("@Loshadkin", "Pong")
        if m.chat.id == -1002222583802 or m.chat.id == -1002029334370 or m.from_user.id == 441399484:
            if m.chat.id == -1002222583802:
                report_channel = True
                battle_type = "Regional Battle"
            elif m.chat.id == -1002029334370:
                report_channel = False
                battle_type = "Skirmish Battle"
            else:
                if m.forward_from_chat != None:
                     if m.forward_from_chat.id == -1002222583802:
                        report_channel = True
                        battle_type = "Regional Battle"
                     else:
                        report_channel = False
                        battle_type = "Skirmish Battle"
                else:
                    userbot.send_message("@Loshadkin", "Пришлите форвард с канала!")
                    return

            if m.entities != None:
                for ids in m.entities:
                    if ids.type == MessageEntityType.TEXT_LINK:
                        #print(ids.url)
                        try:
                            if m.forward_from_chat == None:
                                report_date = m.date.timestamp()
                            else:
                                report_date = m.forward_date.timestamp()
                            battle_players = parser.parse_log_statistic.parse_full_battle_info(ids.url, report_date, report_channel, battle_type)
                            #print(battle_players)
                            #with open('battle_log.json', 'w') as f:
                            #    json.dump(battle_players, f)
                            send_data(battle_players)
                            if m.chat.id == 441399484:
                                userbot.send_message("@Loshadkin", "Data sent successfully.")
                                try:
                                    userbot.send_message("@Loshadkin", str(battle_players))
                                except:
                                    userbot.send_message("@Loshadkin", "Too long message.")

                        except:
                            print(traceback.format_exc())
                            userbot.send_message("@Loshadkin", traceback.format_exc())
    except:
        userbot.send_message("@Loshadkin", traceback.format_exc())

print("7777")

def test():
    try:
        userbot.send_message("@Loshadkin", "Bot started!")
    except:
        print(traceback.format_exc())

threading.Timer(4, test, args = []).start()

def start_parser():
    userbot.run()



