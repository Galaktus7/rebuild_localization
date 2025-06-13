import requests
from bs4 import BeautifulSoup as bs
import traceback
import time

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "[", "]"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

API_TOKEN = "777672a1-0df9-47f2-9871-a02e72618765"

flag_converter = {
    "🇪🇺": 'B',
    "🇲🇴": 'G',
    "🇮🇲": 'R',
    "🇻🇦": 'Y',
    "⚱️":"F",
    "👹C":"F"
}

def create_player(name, flag):
    player = {
        "name":name,
        "flag":flag,
        "maxhp":0,
        "maxarmor":0,
        "strikes":0,
        "actual_strikes": 0,
        "do_damage":0,
        "receive_damage":0,
        "receive_strikes":0,
        "receive_actual_strikes":0,
        "do_damage_from_cactus":0,
        "receive_damage_from_cactus": 0,
        "misses":0,
        "evasions":0,
        "hits":0,
        "blocked_enemy_strikes":0,
        "enemy_blocked_my_strikes":0,
        "decreased_armor":0,
        "decreased_evasion":0,
        "decreased_attack":0,
        "healed":0,
        "total_heals":0,
        "receive_heal":0,
        "kills":0,
        "counter_attacks":0,
        "counter_attacks_damage":0,

        "crits":0,
        "receive_crits":0,
        "add_sword_attacks":0,
        "is_collision":False,

        "current_hp":-1,
        "must_be_hp":-1,
        "dead":False,
        "turns":0,
        "turns_me_attacked":0
    }
    return player

def get_selected_bold_part(row, number, return_type = "int"):
    number = number-1
    switch_number = number*2
    result = ""
    write = False
    switches = 0
    for ids in row:
        if write and ids != "*":
            result += ids

        if ids == "*":
            switches += 1
            if switches > switch_number:
                write = not write
            if switches == switch_number+2:
                if return_type == "int":
                    result = int(result)
                return result
    if return_type == "int":
        result = int(result)
    return result



def check_attack_effects(row, player, target):
    if " loses defence. " in row:
        x = row.split(" loses defence. ")[1]
        lost_def = int(x.split("Pdef ")[1])
        player["decreased_armor"] += lost_def

    if " loses balance. " in row:
        x = row.split(" loses balance. ")[1]
        lost_ev = int(x.split("Evasion ")[1])
        player["decreased_evasion"] += lost_ev

    if " loses focus. " in row:
        x = row.split(" loses focus. ")[1]
        lost_atk = int(x.split("Patk ")[1])
        player["decreased_attack"] += lost_atk

def get_winner(card):
    rows = card.split("<br/>")
    winner = None
    winners = 0
    for ids in rows:
        if " total, " in ids and " alive" in ids:
            remain = int(ids.split(" total, ")[1].split(" alive")[0])
            castle = flag_converter[ids[:2]]
            if remain != 0:
                winner = castle
                winners += 1
    if winners > 1:
        winner = None
    return winner

def get_participants(card):
    rows = card.split("<br/>")
    participants = {
        "total":{},
        "alive":{}
    }
    for ids in rows:
        if " total, " in ids and " alive" in ids:
            alive = int(ids.split(" total, ")[1].split(" alive")[0])
            castle = flag_converter[ids[:2]]
            amount = int(ids.split(" total, ")[0].split(" ")[-1])
            participants["total"][castle] = amount
            if alive > 0:
                participants["alive"][castle] = alive
    return participants

def get_loot(card):
    card = card.replace("<b>", "*").replace("</b>", "*")
    rows = card.split("<br/>")
    loot = []
    for ids in rows:
        if " looted: " in ids:
            name_and_flag = get_selected_bold_part(ids, 1, "str")
            flag = name_and_flag[:2]
            name = name_and_flag.split(flag)[1]
            if "[" in name and "]" in name:
                guild = name.split("[")[1].split("]")[0]
                name = name.split("]")[1]
            else:
                guild = None
            flag = flag_converter[flag]
            lootitem = get_selected_bold_part(ids, 2, "str")
            loot_object = {"player":{"username":name, "guild":guild, "flag":flag}, "loot":lootitem}
            loot.append(loot_object)
    return loot

def get_max_turns(battle_players, name):
    x = 0
    for ids in battle_players:
        player = battle_players[ids]
        if player["name"] != name and not player["is_collision"]:
            if player["turns"] > x:
                x = player["turns"]
    return x

def parse_full_battle_info(link, report_date, report_channel, battle_type):
    r = requests.get(link)
    soup = bs(r.content, "html.parser")
    cards = soup.find_all(class_="card")

    battle_players = {}
    battle_pos = None
    winner = None
    participants = {}
    loot = []
    i = 0
    last_player = None
    for ids in cards:
        if i == 0:
            battle_pos = str(ids).split("[")[1].split("]")[0]
            if "👹" in str(ids):
                t = str(ids)
                t = t.replace("<br/>", "\n").replace("<b>", "*").replace("</b>", "*").replace(
                    "<div class=\"card\">", "").replace("</div>", "").replace("<p>", "").replace("</p>", "")
                r = t.split("\n")[1]
                #print("r:",r)
                bossname = r.split("👹")[1].split(" [")[0]
                battle_type = bossname

        text = str(ids)
        if "end of fight. turns: " in text:
            continue
        text = text.replace("<br/>", "\n").replace("<b>", "*").replace("</b>", "*").replace(
            "<div class=\"card\">", "").replace("</div>", "").replace("<p>", "").replace("</p>", "")
        text = text[:len(text) - 1]
        text = text.split("\n", 1)[1]
        rows = text.split("\n")
        if i == 0:
            winner = get_winner(str(ids))
            participants = get_participants(str(ids))
            loot = get_loot(str(ids))

        if i == 0 or i == 1:
            i += 1
            continue
        i += 1

        name = get_selected_bold_part(rows[0], 1, "str")
        flag = flag_converter[rows[0].split("*")[0]]
        if name not in battle_players:
            battle_players[name] = create_player(name, flag)
        player = battle_players[name]
        player["turns"] += 1
        if player["dead"]:
            player["is_collision"] = True
        target = None
        for idss in rows:
            row = idss
            if row[:7] == "target:":
                targetname = get_selected_bold_part(row, 1, "str")
                targetflag = flag_converter[row.split("*")[0].split("target: ")[1]]
                if targetname not in battle_players:
                    battle_players[targetname] = create_player(targetname, targetflag)
                target = battle_players[targetname]
                target["turns_me_attacked"] += 1
                targethp = get_selected_bold_part(row, 2)
                if target["current_hp"] == -1:
                    target["current_hp"] = targethp
                    target["must_be_hp"] = targethp
                else:
                    target["current_hp"] = targethp
                    if target["current_hp"] < 0:
                        target["current_hp"] = 0
                    if target["must_be_hp"] < 0:
                        target["must_be_hp"] = 0
                    if target["current_hp"] != target["must_be_hp"]:
                        target["is_collision"] = True
                        #print("!!!(2)COLLISION FOUND: " + target["name"])
                        #print("current hp: "+str(target["current_hp"])+"\n"+"must_be_hp: "+str(target["must_be_hp"]))
                if target["maxhp"] < targethp:
                    target["maxhp"] = targethp
                strikes = get_selected_bold_part(row, 3)
                player["strikes"] += strikes
                target["receive_strikes"] += strikes

        row_count = 0
        for idss in rows:
            row = idss
            if row[:7] == "target:":

                continue
            if "🛡️The strike was blocked." in row:
                target["blocked_enemy_strikes"] += 1
                player["enemy_blocked_my_strikes"] += 1
                player["actual_strikes"] += 1
                target["receive_actual_strikes"] += 1
            if "strike!" in row[:15] or "Crushing Stun! " in row[:18] or "Rupture Strike!" in row[:18] or "Thunderbolt Shot!" in row[:20] or \
                    "Shield Attack!" in row[:17]:
                damage = get_selected_bold_part(row, 1)
                targetdef = get_selected_bold_part(row, 2)
                if target["maxarmor"] < targetdef:
                    target["maxarmor"] = targetdef
                player["do_damage"] += damage
                target["receive_damage"] += damage
                target["must_be_hp"] -= damage
                player["actual_strikes"] += 1
                target["receive_actual_strikes"] += 1
                player["hits"] += 1
                if "crit" in row[:7]:
                    player["crits"] += 1
                    target["receive_crits"] += 1
                if "➕" in row:
                    player["add_sword_attacks"] += 1
                check_attack_effects(row, player, target)

            if " bleeds for " in row and "→" in row:
                bleed_damage = get_selected_bold_part(row, 2)
                player["receive_damage"] += bleed_damage
                player["must_be_hp"] -= bleed_damage

            if " reflects the attack from " in row:
                reflector = target
                attacker = player
                reflected_damage = get_selected_bold_part(row, 2)
                reflector["do_damage"] += reflected_damage
                attacker["receive_damage"] += reflected_damage
                attacker["must_be_hp"] -= reflected_damage
                reflector["do_damage_from_cactus"] += reflected_damage
                attacker["receive_damage_from_cactus"] += reflected_damage
                attacker_def = get_selected_bold_part(row, 3)
                if attacker["maxarmor"] < attacker_def:
                    attacker["maxarmor"] = attacker_def
            if " HP left: " in row:
                victim = get_selected_bold_part(row, 1, "str")
                hp = get_selected_bold_part(row, 2)
                if victim == player["name"]:
                    if player["maxhp"] < hp:
                        player["maxhp"] = hp
                elif victim == target["name"]:
                    if target["maxhp"] < hp:
                        target["maxhp"] = hp
                if hp <= 0:
                    if victim == player["name"]:
                        target["kills"] += 1
                        player["dead"] = True
                    elif victim == target["name"]:
                        player["kills"] += 1
                        target["dead"] = True

            if ", restoring " in row:
                healtargetname = get_selected_bold_part(row, 2, "str")
                if healtargetname not in battle_players:
                    healflag = player["flag"]
                    battle_players[healtargetname] = create_player(healtargetname, healflag)
                healtarget = battle_players[healtargetname]
                healamount = get_selected_bold_part(row, 3)
                player["healed"] += healamount
                player["total_heals"] += 1
                healtarget["receive_heal"] += healamount
                healtarget["must_be_hp"] += healamount
            if "miss!" in row[:8]:
                player["actual_strikes"] += 1
                player["misses"] += 1
                target["evasions"] += 1
                target["receive_actual_strikes"] += 1
                if "➕" in row:
                    player["add_sword_attacks"] += 1
                check_attack_effects(row, player, target)
            if " counter-attacking " in row:
                target["strikes"] += 1
                player["receive_strikes"] += 1
                target["actual_strikes"] += 1
                target["counter_attacks"] += 1
                player["turns_me_attacked"] += 1
                player["receive_actual_strikes"] += 1

                if "miss!" not in row:
                    if "crit strike!" in row:
                        target["crits"] += 1
                        player["receive_crits"] += 1

                    if "🛡️The strike was blocked." not in row:
                        damage = get_selected_bold_part(row, 2)
                        player["receive_damage"] += damage

                        player["must_be_hp"] -= damage
                        target["do_damage"] += damage
                        target["counter_attacks_damage"] += damage
                        target["hits"] += 1

                    else:
                        player["blocked_enemy_strikes"] += 1
                        target["enemy_blocked_my_strikes"] += 1

                else:
                    target["misses"] += 1
                    player["evasions"] += 1
                check_attack_effects(row, target, player)

            row_count += 1

    new_battle_players = {}
    for ids in battle_players:
        if "[" in ids and "]" in ids:
            guild = ids.split("[")[1].split("]")[0]
            name = ids.split("]")[1]
        else:
            name = ids
            guild = None
        if guild != None:
            a = "&"+str(guild)
        else:
            a = ""
        playercode = name+a
        new_battle_players[playercode] = battle_players[ids]
        new_battle_players[playercode]["player"] = name
        new_battle_players[playercode]["guild"] = guild

        del new_battle_players[playercode]["current_hp"]
        del new_battle_players[playercode]["must_be_hp"]
        del new_battle_players[playercode]["dead"]
        del new_battle_players[playercode]["name"]
        for idss in new_battle_players[playercode]:
            if new_battle_players[playercode][idss] is 0:
                new_battle_players[playercode][idss] = None
    final_dict = {"player_data":new_battle_players,
                  "report_date":report_date,
                  "regional_channel":report_channel,
                  "battle_position":battle_pos,
                  "report_link":link,
                  "winner":winner,
                  "participants":participants,
                  "battle_type":battle_type,
                  "loot":loot,
                  "token":API_TOKEN}
    return final_dict


#x = parse_full_battle_info("https://api.chatwars.me/webview/battle/1a7ff02652e64d29bcc44ab0a39a15bb", time.time(), True, "Boss battle")
#print(x)

#import json
#with open('battle_log.json', 'w') as f:
#    json.dump(x, f)
