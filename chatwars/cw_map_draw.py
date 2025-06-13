from PIL import Image, ImageDraw
import telebot
import requests
import traceback

token = "5376192961:AAEi7EAmanumoz87apkE0XB15eEq13cZv0g"
bot = telebot.TeleBot(token)

map_coords = {}
player_positions = {}
player_moves = {}
banned_coords = {}

analysis_mode = {}


@bot.message_handler(content_types="photo")
def photoss(m):
    if m.from_user.id not in analysis_mode:
        analysis_mode[m.from_user.id] = "Режим-2"
    bot.send_message(m.chat.id, "Начало записи. Пожалуйста, подождите, и не отправляйте боту новых сообщений во избежание неточностей.")
    photopath = bot.get_file(m.photo[-1].file_id)
    photo = requests.get('https://api.telegram.org/file/bot' + token + '/' + photopath.file_path).content
    with open("cwmap.jpeg", "wb+") as file:
        file.write(photo)
    im = Image.open("cwmap.jpeg")
    draw = ImageDraw.Draw(im)
    pixels = im.load()
    print(pixels)
    x, y = im.size  # ширина (x) и высота (y) изображения
    white_pix = 0
    another_pix = 0
    #newimage = Image.new("RGBA", (x+50, y+50), (0, 0, 0, 0))
    #draw = ImageDraw.Draw(newimage)

    if m.forward_from == None:
        return
    if analysis_mode[m.from_user.id] == "Режим-1":    # ORIGINAL BOT
        starts_x = 2
        starts_y = 2
        difference_x = 5
        difference_y = 5
        diss = 1
        diss_step = 30
    else:     # ELITE BOT
        starts_x = 2
        starts_y = 2
        difference_x = 5
        difference_y = 5
        diss = 1
        diss_step = 5000
    player_positions[m.from_user.id] = []
    player_moves[m.from_user.id] = []
    banned_coords[m.from_user.id] = []
    curx = starts_x
    cyclesX = 0
    map_coords[m.from_user.id] = {}
    while curx < x:
        cyclesY = 0
        cury = starts_y
        while cury < y:
            color = pixels[curx, cury]  # содержит кортеж из нескольких значений цвета, в зависимости от формата изображения
            curdot = "?"
            if pixels[curx, cury][0] > 180 and pixels[curx, cury][1] > 180 and pixels[curx, cury][2] > 180:  # pixels[i, j][q] > 240  # для оттенков
                curdot = "corridor"     # WHITE DOT
            if pixels[curx, cury][0] < 50 and pixels[curx, cury][1] < 50 and pixels[curx, cury][2] < 50:  # pixels[i, j][q] > 240  # для оттенков
                curdot = "wall"         #BLACK DOT
            if pixels[curx, cury][0] < 110 and pixels[curx, cury][1] >= 9 and pixels[curx, cury][1] <= 120 and pixels[curx, cury][2] >= 160:
                curdot = "flag"    ####BLUE DOT
            elif pixels[curx, cury][0] >= 61 and pixels[curx, cury][0] <= 225 and pixels[curx, cury][1] <= 158 and pixels[curx, cury][2] >= 77:
                curdot = "monster"    ####PURPLE DOT
            if pixels[curx, cury][0] >= 105 and pixels[curx, cury][1] >= 76 and pixels[curx, cury][1] <= 195 and pixels[curx, cury][2] <= 110:
                curdot = "camp"    ####ORANGE DOT
            if pixels[curx, cury][0] >= 5 and pixels[curx, cury][0] <= 154 and pixels[curx, cury][1] >= 61 and pixels[curx, cury][1] <= 255 and pixels[curx, cury][2] <= 150:
                curdot = "fountain"    ####GREEN DOT
            if pixels[curx, cury][0] >= 69 and pixels[curx, cury][1] <= 125 and pixels[curx, cury][2] <= 125:
                curdot = "boss"    ####RED DOT


            map_coords[m.from_user.id][str(cyclesX)+'_'+str(cyclesY)] = {'комната':curdot}
            fillcolor = "red"
            if curdot == "corridor":
                fillcolor = "pink"
            if curdot == "wall":
                fillcolor = "green"
            if curdot == "flag":
                fillcolor = "orange"
            if curdot == "camp":
                fillcolor = "purple"
            if curdot == "fountain":
                fillcolor = "yellow"
            if curdot == "monster":
                fillcolor = "black"
            if curdot == "boss":
                fillcolor = "blue"
            if curdot == "?":
                fillcolor = "red"
                #print(pixels[curx, cury][0])
                #print(pixels[curx, cury][1])
                #print(pixels[curx, cury][2])
                #print(cycles)
                #return
            #draw.ellipse((curx, cury, curx+1, cury+1), fill=fillcolor, outline=fillcolor)
            draw.point((curx, cury), fill=fillcolor)

            cury += difference_y
            cyclesY += 1
            if cyclesY % diss_step == 0:
                cury -= 1

        curx += difference_x
        cyclesX += 1
        if cyclesX % diss_step == 0:
            curx -= diss

    #draw.ellipse((8, 7, 9, 8), fill="red", outline="red")
    im.save('Test'+str(m.from_user.id)+'.png', "PNG")
    for ids in map_coords[m.from_user.id]:
        coord = map_coords[m.from_user.id][ids]
        coord_x = int(ids.split('_')[0])
        coord_y = int(ids.split('_')[1])
        try:
            coord['север'] = map_coords[m.from_user.id][str(coord_x)+'_'+str(coord_y-1)]['комната']
        except:
            coord['север'] = "wall"
        try:
            coord['юг'] = map_coords[m.from_user.id][str(coord_x) + '_' + str(coord_y + 1)]['комната']
        except:
            coord['юг'] = "wall"
        try:
            coord['запад'] = map_coords[m.from_user.id][str(coord_x-1) + '_' + str(coord_y)]['комната']
        except:
            coord['запад'] = "wall"
        try:
            coord['восток'] = map_coords[m.from_user.id][str(coord_x+1) + '_' + str(coord_y)]['комната']
        except:
            coord['восток'] = "wall"


    try:
        with open('Test'+str(m.from_user.id)+'.png', "rb") as file:
            #f = file.read()
            bot.send_document(m.chat.id, document=file)
        #bot.send_photo(m.chat.id, open('Test'+str(m.from_user.id)+'.png', 'rb'));
        bot.send_message(m.chat.id, 'Конец записи. Карта сохранена. Теперь отправьте мне информацию о текущей точке от чатварс бота.')
        bot.send_message(441399484, m.from_user.first_name+" записал карту.")
    except:
        print(traceback.format_exc())

@bot.message_handler(commands = ['start'])
def starttt(m):
    bot.send_message(m.chat.id, "Для начала отправьте мне карту подземелья. Затем отправляйте мне сообщения в таком порядке:\n"+
                     "1. Информация о позиции (Остановившись, ты увидел...)\n2. Информация о том, куда вы сдвинули персонажа после того как оказались "+
                     "на позиции (North/West/South/East)\n"+
                     "3. Повторять пункты 1 и 2 пока бот не скажет, что осталась всего одна возможная позиция.")

@bot.message_handler(commands = ['mode'])
def analysis_mode_swwwwww(m):
    if m.from_user.id not in analysis_mode:
        analysis_mode[m.from_user.id] = "Режим-1"
    if analysis_mode[m.from_user.id] == "Режим-1":
        analysis_mode[m.from_user.id] = "Режим-2"
        bot.send_message(m.chat.id, "Режим анализа лабиринта изменён на \"Режим-2\"! Попробуйте снова загрузить в бота карту.")
        return
    if analysis_mode[m.from_user.id] == "Режим-2":
        analysis_mode[m.from_user.id] = "Режим-1"
        bot.send_message(m.chat.id, "Режим анализа лабиринта изменён на \"Режим-1\"! Попробуйте снова загрузить в бота карту.")
        return

@bot.message_handler(commands = ['sendm'])
def sendtoall(m):
    if m.from_user.id != 441399484:
        return
    sent = 0
    notsent = 0
    for ids in map_coords:
        try:
            bot.send_message(ids, m.text.split("/sendm ")[1])
            sent += 1
        except:
            notsent += 1
    bot.send_message(m.chat.id, "Отправлено: "+str(sent)+'/'+str(notsent+sent))

@bot.message_handler(content_types = ['text'])
def textss(m):
    print(m.text)
    if "North" in m.text:
        try:
            player_moves[m.from_user.id].append("вверх")
        except:
            player_moves[m.from_user.id] = ["вверх"]
        bot.send_message(m.chat.id, 'Записано передвижение. Отправьте мне новую информацию о текущей точке.')
        return

    if "West" in m.text:
        try:
            player_moves[m.from_user.id].append("влево")
        except:
            player_moves[m.from_user.id] = ["влево"]
        bot.send_message(m.chat.id, 'Записано передвижение. Отправьте мне новую информацию о текущей точке.')
        return

    if "East" in m.text:
        try:
            player_moves[m.from_user.id].append("вправо")
        except:
            player_moves[m.from_user.id] = ["вправо"]
        bot.send_message(m.chat.id, 'Записано передвижение. Отправьте мне новую информацию о текущей точке.')
        return

    if "South" in m.text:
        try:
            player_moves[m.from_user.id].append("вниз")
        except:
            player_moves[m.from_user.id] = ["вниз"]
        bot.send_message(m.chat.id, 'Записано передвижение. Отправьте мне новую информацию о текущей точке.')
        return

    if m.from_user.id not in analysis_mode:
        analysis_mode[m.from_user.id] = "Режим-2"

    try:
        if analysis_mode[m.from_user.id] == "Режим-1":    # ORIGINAL BOT
            starts_x = 2
            starts_y = 2
            difference_x = 5
            difference_y = 5
            diss = 1
            diss_step = 30
        else:     # ELITE BOT
            starts_x = 2
            starts_y = 2
            difference_x = 5
            difference_y = 5
            diss = 1
            diss_step = 5000
    except:
        starts_x = 2
        starts_y = 2
        difference_x = 5
        difference_y = 5
        diss = 1
        diss_step = 30
    if "🗺Остановившись, ты увидел " in m.text:
        bot.send_message(m.chat.id, "Начало записи. Пожалуйста, подождите, и не отправляйте боту новых сообщений во избежание неточностей.")
        alltexts = m.text.split('\n')
        if "пустой коридор, ничего интересного" in alltexts[0]:
            curloc = "corridor"
        if "примечательное место" in alltexts[0]:
            curloc = "flag"
        if "костер, ты можешь тут немного отдохнуть" in alltexts[0]:
            curloc = "camp"
        if "волшебный фонтан" in alltexts[0]:
            curloc = "fountain"
        if "комната со старым сундуком" in alltexts[0]:
            curloc = "fountain"
        if "комната с монстром" in alltexts[0]:
            curloc = "monster"
        try:
            allpos = player_positions[m.from_user.id]
        except:
            allpos = []
            player_positions[m.from_user.id] = []
        try:
            allmoves = player_moves[m.from_user.id]
        except:
            allmoves = []
            player_moves[m.from_user.id] = []
        addx = 0
        addy = 0
        if len(allmoves) > 0:
            for ids in allmoves:
                if ids == "вверх":
                    addy -= 1
                if ids == "вниз":
                    addy += 1
                if ids == "вправо":
                    addx += 1
                if ids == "влево":
                    addx -= 1

        directs_info = {
            "комната":curloc,
            "север":"wall",
            "юг":"wall",
            "запад": "wall",
            "восток": "wall",
            "список_позиций":allpos,
            "список_движений":allmoves,
            "доп_x":addx,
            "доп_y":addy
        }
        current_directs_info = []
        current_directs_info.append(directs_info)
        for ids in player_positions[m.from_user.id]:
            current_directs_info.append(ids)

        locs_index = 3
        while alltexts[locs_index] != "":
            direct = "?"
            if "На севере:" in alltexts[locs_index]:
                direct = "север"
            if "На юге:" in alltexts[locs_index]:
                direct = "юг"
            if "На западе:" in alltexts[locs_index]:
                direct = "запад"
            if "На востоке:" in alltexts[locs_index]:
                direct = "восток"
            print(alltexts[locs_index].split(': '))
            what = alltexts[locs_index].split(': ')[1]
            object = "?"
            if "пустой коридор, ничего интересного" in what:
                object = "corridor"
            if "примечательное место" in what:
                object = "flag"
            if "костер, ты можешь тут немного отдохнуть" in what:
                object = "camp"
            if "волшебный фонтан" in what:
                object = "fountain"
            if "комната со старым сундуком" in what:
                object = "fountain"
            if "комната с монстром" in what:
                object = "monster"
            directs_info[direct] = object
            locs_index += 1
        try:
            player_positions[m.from_user.id].append(directs_info)
        except:
            player_positions[m.from_user.id] = [directs_info]
        potential_coords = []
        for ids in map_coords[m.from_user.id]:
            loc = map_coords[m.from_user.id][ids]
            need_access = len(current_directs_info)
            cur_access = 0
            #print(current_directs_info)
            try:
                banned_coords[m.from_user.id][0]
            except:
                banned_coords[m.from_user.id] = []
            if ids not in banned_coords[m.from_user.id]:
                for idss in current_directs_info:
                    old_x = int(ids.split('_')[0])
                    old_y = int(ids.split('_')[1])
                    newloc_x = int(idss['доп_x'])+old_x
                    newloc_y = int(idss['доп_y'])+old_y
                    try:
                        newloc = map_coords[m.from_user.id][str(newloc_x)+'_'+str(newloc_y)]
                        if newloc["комната"] == idss["комната"]:
                            #print(newloc)
                            #print("1")
                            if newloc["север"] == idss["север"] and newloc["юг"] == idss["юг"] and \
                            newloc["запад"] == idss["запад"] and newloc["восток"] == idss["восток"]:
                                cur_access += 1
                    except:
                        pass
                if cur_access == need_access:
                    potential_coords.append(ids)
                    print("2")
                else:
                    try:
                        banned_coords[m.from_user.id].append(ids)
                    except:
                        banned_coords[m.from_user.id] = [ids]
        print("Ваши потенциальные координаты:\n"+str(potential_coords))
        print(len(potential_coords))
        im = Image.open('Test'+str(m.from_user.id)+'.png')
        draw = ImageDraw.Draw(im)
        pixels = im.load()
        for ids in potential_coords:
            pot_x = int(ids.split('_')[0])
            pot_y = int(ids.split('_')[1])
            dot_x = starts_x
            cycles = 0
            while pot_x > 0:
                dot_x += difference_x
                pot_x -= 1
                cycles += 1
                if cycles % diss_step == 0:
                    dot_x -= 1
            dot_y = starts_y
            cycles = 0
            while pot_y > 0:
                dot_y += difference_y
                pot_y -= 1
                cycles += 1
                if cycles % diss_step == 0:
                    dot_y -= 1

            draw.point((dot_x, dot_y), fill="red")
            draw.line([(0, 0), (dot_x, dot_y)], fill="red", width=1)
        im.save('Test' + str(m.from_user.id) + '_playercoords.png', "PNG")
        bot.send_message(m.chat.id, "Конец записи. Количество возможных координат: "+str(len(potential_coords))+"\n"+\
                         "Теперь отправьте мне ваше следующее передвижение (North/West/South/East).\n\n❗️Бот указывает линиями на те точки, которые предположительно считает стартовыми,"+\
                         " а не на те, на которых персонаж находится после всех перемещений.")
        if len(potential_coords) == 0:
            bot.send_message(m.chat.id, "Если бот выдал ноль возможных маршрутов - значит, отрисовка карты из чатварс выполнена по другому алгоритму. Чтобы "+\
                             "бот корректно считал именно эту карту - измените режим анализа (команда /mode) и загрузите карту и список действий заново.")
        bot.send_message(441399484, m.from_user.first_name + " получил количество возможных передвижений ("+str(len(potential_coords))+").")
        with open('Test' + str(m.from_user.id) + '_playercoords.png', "rb") as file:
            #f = file.read()
            bot.send_document(m.chat.id, document=file)
        #bot.send_photo(m.chat.id, open('Test' + str(m.from_user.id) + '_playercoords.png', 'rb'));
        #bot.send_message(m.chat.id, curloc)
