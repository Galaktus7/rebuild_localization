import random

first_part = ["Бульба", "Иви", "Чар", "Варт", "Бласт", "Кате", "Мета", "Баттер", "Хуп", "Вулк", "Ивел", "Зер", "Ной", "Ава", "Флор", "Терра",
              "Глай", "Лиф", "Тоге", "Крог", "Драп", "Гиппо", "Рио", "Манч", "Брон", "Чин", "Глей"]

second_part = ["рор", "джес", "нот", "дин", "дус", "кион", "аби", "урк", "мет", "тик", "рус", "пент", "энг", "инг", "летт", "клус", "зис", "ран",
               "чан", "чон", "цел", "тим", "дон", "тот", "дуф", "виг", "кант"]

first_part = ["Татз", "Гон", "Греб", "Урн", "Краг", "Рот", "Огг", "Дагр", "Лои", "Були", "Тарк", "Кром", "Вако", "Тови", "Дарм", "Варз", "Аль",
              "Кро", "Дуб", "Ниг", "Кер", "Гогз", "Мок", "Веку", "Гат", "Тудна", "Оли", "Хек", "Бул", "Мок", "Урф", "Рог"]

second_part = ["лод", "рос", "раг", "гал", "лаг", "тук", "фек", "обо", "токк", "руг", "дул", "ра", "ака", "она", "гур", "наг", "ими",
               "рим", "виа", "оун", "нер", "ната", "наха", "нал", "ран", "рин", "ула", "зог",

               "рор", "джес", "нот", "дин", "дус", "кион", "аби", "урк", "мет", "тик", "рус", "пент", "энг", "инг",
               "летт", "клус", "зис", "ран",
               "чан", "чон", "цел", "тим", "дон", "тот", "дуф", "виг", "кант"
               ]

skills = ['sniper', 'shieldgen', 'medic', 'dvuzhil', 'zombie',
          'bicepc', 'pyromancer', 'sadist', 'berserk', 'zapas', 'visor', 'protivogaz', 'narkoman',
         'vor', 'ritualist', 'navod', 'oruzh', 'necromant', 'incvizitor', 'pyrotech', 'cherep', 'alchemist',
         'ninja', 'multicast', 'lastchance', 'invoker', 'inzhener']

def namegenerator():
    return random.choice(first_part)+random.choice(second_part)

def randomskills(daytime = 'night'):
    skilllist_morning = ['zombie', 'zapas']
    skilllist_day = []
    skilllist_evening = []
    skillist_night = []
    if daytime == 'morning':
        final_skills = skilllist_morning
    elif daytime == 'day':
        final_skills = skilllist_day
    elif daytime == 'evening':
        final_skills = skilllist_evening
    elif daytime == 'night':
        final_skills = []
        for ids in skilllist_evening:
            if ids not in final_skills:
                final_skills.append(ids)
        for ids in skilllist_day:
            if ids not in final_skills:
                final_skills.append(ids)
        for ids in skilllist_morning:
            if ids not in final_skills:
                final_skills.append(ids)

def randomdmglimit(daytime = 'night'):
    return random.randint(3, 9)

def randomdmhp(daytime = 'night'):
    return random.randint(3, 6)

#plist = []

#while len(plist) < 10:
#    plist.append(random.choice(first_part)+random.choice(second_part))

#print(plist)


