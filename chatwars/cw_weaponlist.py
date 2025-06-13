class Weapon(object):
    def __init__(self):
        self.id = None
        self.energycost = 2
        self.cubes = 2
        self.dmgbonus = 0
        self.name = 'None'
        self.ranged = False
        self.accuracybonus = 0
        self.lvl = 1
        self.classic = False
        self.modification = 0


class Pistol_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.lvl = 1
        
class Pistol_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 3
        self.lvl = 2
        
class Pistol_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 3
        self.accuracybonus = 3
        self.energycost = 3
        self.lvl = 3

class Pistol_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 121
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 4
        self.accuracybonus = 3
        self.energycost = 3
        self.lvl = 4
        self.modification = 1

class Pistol_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 122
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 3
        self.accuracybonus = 3
        self.energycost = 2
        self.lvl = 4
        self.modification = 2
        
class Fist_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.name = 'Кулаки'
        self.accuracybonus = 2
        self.cubes = 2
        self.lvl = 1
        
class ShortSword_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 5
        self.name = 'Короткий меч'
        self.accuracybonus = 1
        self.cubes = 3
        self.lvl = 1
        
class ShortSword_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 6
        self.name = 'Короткий меч'
        self.accuracybonus = 2
        self.cubes = 3
        self.lvl = 2
        
class ShortSword_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 7
        self.name = 'Короткий меч'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 3

class ShortSword_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 123
        self.name = 'Короткий меч'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.modification = 1

class ShortSword_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 124
        self.name = 'Короткий меч'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.ranged = True
        self.lvl = 4
        self.modification = 2
        
class Revolver_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 8
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 0
        self.energycost = 4
        self.accuracybonus = 0
        self.lvl = 1
        
class Revolver_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 9
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 0
        self.energycost = 3
        self.accuracybonus = 1
        self.lvl = 2
        
class Revolver_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 10
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 1
        self.energycost = 3
        self.accuracybonus = 1
        self.lvl = 3

class Revolver_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 79
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 3
        self.energycost = 4
        self.accuracybonus = 0
        self.lvl = 4
        self.modification = 1 #

class Revolver_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 80
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 1
        self.energycost = 2
        self.accuracybonus = 3
        self.lvl = 4
        self.modification = 2 #


class Baseball_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 11
        self.name = 'Бита'
        self.accuracybonus = 1
        self.cubes = 3
        self.lvl = 1
        
class Baseball_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 12
        self.name = 'Бита'
        self.accuracybonus = 2
        self.cubes = 3
        self.lvl = 2
        
class Baseball_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 13
        self.name = 'Бита'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 3

class Baseball_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 81
        self.name = 'Бита'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4 # Оглушает с шансом 50%
        self.modification = 1

class Baseball_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 82
        self.name = 'Бита'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4 #Оглушает на 2 хода с тем же шансом
        self.modification = 2

class Knife_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 14
        self.name = 'Нож'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1

class Knife_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 15
        self.name = 'Нож'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2

class Knife_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 16
        self.name = 'Нож'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3

class Knife_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 83
        self.name = 'Нож'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4 # Кровотечение срабатывает в тот же ход
        self.modification = 1

class Knife_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 84
        self.name = 'Нож'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4 # Кровотечение любого соперника восстанавливает ХП вам
        self.modification = 2

class Obrez_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 17
        self.name = 'Обрез'
        self.accuracybonus = 0
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 3

class Obrez_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 18
        self.name = 'Обрез'
        self.accuracybonus = 0
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = True
        self.energycost = 3

class Obrez_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 19
        self.name = 'Обрез'
        self.accuracybonus = 1
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = True
        self.energycost = 3

class Obrez_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 85
        self.name = 'Обрез'
        self.accuracybonus = 1
        self.cubes = 5
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 2
        self.modification = 1

class Obrez_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 86
        self.name = 'Обрез'
        self.accuracybonus = 1
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 3 #Выстрел вызывает кровотечение с шансом 75%
        self.modification = 2

class Torch_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 20
        self.name = 'Факел'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1

class Torch_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 21
        self.name = 'Факел'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2

class Torch_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 22
        self.name = 'Факел'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3

class Torch_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 87
        self.name = 'Факел'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4 #Поджигает на 3
        self.modification = 1

class Torch_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 88
        self.name = 'Факел'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4 #Поджигает себя на 2, а соперника - на 5
        self.modification = 2

class Flamethrower_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 23
        self.name = 'Огнемет'
        self.accuracybonus = 1
        self.cubes = 2
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 4

class Flamethrower_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 24
        self.name = 'Огнемет'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = True
        self.energycost = 4

class Flamethrower_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 25
        self.name = 'Огнемет'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = True
        self.energycost = 3

class Flamethrower_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 89
        self.name = 'Огнемет'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 2
        self.lvl = 4
        self.ranged = True
        self.energycost = 3
        self.modification = 1

class Flamethrower_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 90
        self.name = 'Огнемет'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 1 #поджигает на 2 но не наносит урон
        self.modification = 2


class Rifle_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 26
        self.name = 'Снайперская винтовка'
        self.accuracybonus = -4
        self.cubes = 1
        self.dmgbonus = 6
        self.lvl = 1
        self.ranged = True
        self.energycost = 5

class Rifle_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 27
        self.name = 'Снайперская винтовка'
        self.accuracybonus = -4
        self.cubes = 1
        self.dmgbonus = 8
        self.lvl = 2
        self.ranged = True
        self.energycost = 5

class Rifle_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 28
        self.name = 'Снайперская винтовка'
        self.accuracybonus = -3
        self.cubes = 1
        self.dmgbonus = 10
        self.lvl = 3
        self.ranged = True
        self.energycost = 5

class Rifle_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 91
        self.name = 'Снайперская винтовка'
        self.accuracybonus = -3
        self.cubes = 1
        self.dmgbonus = 10
        self.lvl = 4
        self.ranged = True
        self.energycost = 5  #При атаке 60% шанс сначала прицелиться а потом атаковать
        self.modification = 1

class Rifle_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 92
        self.name = 'Снайперская винтовка'
        self.accuracybonus = -3
        self.cubes = 1
        self.dmgbonus = 10
        self.lvl = 4
        self.ranged = True
        self.energycost = 5  #При промахе пуля попадает в другого случайного соперника
        self.modification = 2

class Axe_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 29
        self.name = 'Топор'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Axe_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 30
        self.name = 'Топор'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Axe_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 31
        self.name = 'Топор'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Axe_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 93
        self.name = 'Топор'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2  # Калечит на 4
        self.modification = 1

class Axe_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 94
        self.name = 'Топор'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 2
        self.lvl = 4
        self.ranged = False
        self.energycost = 2  #
        self.modification = 2

class Bulava_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 32
        self.name = 'Булава'
        self.accuracybonus = 1
        self.cubes = 2
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Bulava_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 33
        self.name = 'Булава'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Bulava_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 34
        self.name = 'Булава'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Bulava_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 95
        self.name = 'Булава'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # каждые 3 хода постоянный бонус к урону увеличивается на 1
        self.modification = 1

class Bulava_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 96
        self.name = 'Булава'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 5 # Бонус к урону за атаки подряд увеличивается на 4
        self.modification = 2

class Kastet_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 35
        self.name = 'Кастет'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Kastet_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 36
        self.name = 'Кастет'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Kastet_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 37
        self.name = 'Кастет'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Kastet_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 97
        self.name = 'Кастет'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #Снимает 1 энергии за каждый удар
        self.modification = 1

class Kastet_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 98
        self.name = 'Кастет'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 2
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #
        self.modification = 2

class Kuvalda_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 38
        self.name = 'Кувалда'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Kuvalda_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 39
        self.name = 'Кувалда'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Kuvalda_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 40
        self.name = 'Кувалда'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Kuvalda_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 98
        self.name = 'Кувалда'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #Наносит 2 (3) урона за единицу отсутствующей энергии
        self.modification = 1

class Kuvalda_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 99
        self.name = 'Кувалда'
        self.accuracybonus = 2
        self.cubes = 4
        self.dmgbonus = 2
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # У сокрушения нет перезарядки
        self.modification = 2

class Chain_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 41
        self.name = 'Цепь'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Chain_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 42
        self.name = 'Цепь'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Chain_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 43
        self.name = 'Цепь'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Chain_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 100
        self.name = 'Цепь'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #100% выбивает оружие спец.атакой, -1 ход перезарядки спец.атаки
        self.modification = 1

class Chain_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 101
        self.name = 'Цепь'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #с шансом 40% выбивает оружие обычной атакой
        self.modification = 2

class Spear_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 44
        self.name = 'Копье'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Spear_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 45
        self.name = 'Копье'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Spear_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 46
        self.name = 'Копье'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Spear_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 102
        self.name = 'Копье'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #Контратака срабатывает пассивно на 1 атакующую цель раз в 10 ходов
        self.modification = 1

class Spear_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 103
        self.name = 'Копье'
        self.accuracybonus = 4
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #
        self.modification = 2

class Saber_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 47
        self.name = 'Сабля'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Saber_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 48
        self.name = 'Сабля'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Saber_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 49
        self.name = 'Сабля'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Saber_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 104
        self.name = 'Сабля'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 1 #
        self.modification = 1

class Saber_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 105
        self.name = 'Сабля'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Успешно парируя цель, вы восстанавливаете всю энергию. Парирование накладывает на вас щит.
        self.modification = 2

class Bow_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 50
        self.name = 'Лук'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 3

class Bow_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 51
        self.name = 'Лук'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = True
        self.energycost = 3

class Bow_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 52
        self.name = 'Лук'
        self.accuracybonus = 2
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = True
        self.energycost = 3

class Bow_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 106
        self.name = 'Лук'
        self.accuracybonus = 2
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 3 # Поджигает цель на 6
        self.modification = 1

class Bow_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 107
        self.name = 'Лук'
        self.accuracybonus = 2
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 2 # Поджигает цель при обычной атаке с шансом 40%
        self.modification = 2

class Claws_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 53
        self.name = 'Стальные когти'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Claws_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 54
        self.name = 'Стальные когти'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Claws_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 55
        self.name = 'Стальные когти'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Claws_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 108
        self.name = 'Стальные когти'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Шанс 25% нанести удвоенный урон
        self.modification = 1

class Claws_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 109
        self.name = 'Стальные когти'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # +2 макс. урону к режиму когтя
        self.modification = 2

class Saw_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 56
        self.name = 'Пиломет'
        self.accuracybonus = 2
        self.cubes = 2
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 3

class Saw_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 57
        self.name = 'Пиломет'
        self.accuracybonus = 3
        self.cubes = 2
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = True
        self.energycost = 3

class Saw_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 58
        self.name = 'Пиломет'
        self.accuracybonus = 3
        self.cubes = 2
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = True
        self.energycost = 3

class Saw_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 109
        self.name = 'Пиломет'
        self.accuracybonus = 3
        self.cubes = 2
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 3 # ранит на 3-4
        self.modification = 1

class Saw_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 110
        self.name = 'Пиломет'
        self.accuracybonus = 4
        self.cubes = 2
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = True
        self.energycost = 2 #
        self.modification = 2

class Police_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 59
        self.name = 'Полицейская дубинка'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Police_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 60
        self.name = 'Полицейская дубинка'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Police_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 61
        self.name = 'Полицейская дубинка'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Police_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 111
        self.name = 'Полицейская дубинка'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 2
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 #
        self.modification = 1

class Police_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 112
        self.name = 'Полицейская дубинка'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Если у соперника после атаки осталось 0 энергии (но перед этим энергия была) - оглушает цель. Сжигает 1-2 энергии
        self.modification = 2

class Shurikens_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 62
        self.name = 'Сюрикены'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 2

class Shurikens_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 63
        self.name = 'Сюрикены'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = True
        self.energycost = 2

class Shurikens_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 64
        self.name = 'Сюрикены'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = True
        self.energycost = 2

class Shurikens_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 113
        self.name = 'Сюрикены'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = True
        self.energycost = 2 # урон с одного броска 3
        self.modification = 1

class Shurikens_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 114
        self.name = 'Сюрикены'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = True
        self.energycost = 2 # Бесконечный запас сюрикенов
        self.modification = 2

class Molot_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 65
        self.name = 'Молот'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Molot_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 66
        self.name = 'Молот'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Molot_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 67
        self.name = 'Молот'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Molot_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 115
        self.name = 'Молот'
        self.accuracybonus = 3
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # за каждые 2 отсутствующие единицы энергии получает +3 к урону
        self.modification = 1

class Molot_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 116
        self.name = 'Молот'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # У особой способности нет времени перезарядки
        self.modification = 2

class Shest_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 68
        self.name = 'Шест'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2

class Shest_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 69
        self.name = 'Шест'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Shest_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 70
        self.name = 'Шест'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Shest_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 117
        self.name = 'Шест'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Обычная атака сбивает с ног с шансом 40%
        self.modification = 1

class Shest_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 118
        self.name = 'Шест'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 1
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Сбитие с ног оглушает
        self.modification = 2

class Tesak_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 71
        self.name = 'Тесак'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 3

class Tesak_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 72
        self.name = 'Тесак'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 2
        self.ranged = False
        self.energycost = 2

class Tesak_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 73
        self.name = 'Тесак'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 2

class Tesak_4_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 119
        self.name = 'Тесак'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Первое попадание имеет бонус к урону 10, затем он понижается до 4. Потом начинается обычное понижение по единице
        self.modification = 1

class Tesak_4_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 120
        self.name = 'Тесак'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 4
        self.ranged = False
        self.energycost = 2 # Первый удар наносит урон сквозь уворот, броню и любые щиты
        self.modification = 2

class SkeleSword(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 74
        self.name = 'Меч'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = False
        self.energycost = 2


class DarkDemonWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 75
        self.name = 'Когти демона тьмы'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 3
        self.ranged = False
        self.energycost = 3


class Crossbow_1(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 76
        self.name = 'Арбалет'
        self.accuracybonus = 1
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 3

class Crossbow_2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 77
        self.name = 'Арбалет'
        self.accuracybonus = 2
        self.cubes = 3
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 3

class Crossbow_3(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 78
        self.name = 'Арбалет'
        self.accuracybonus = 2
        self.cubes = 4
        self.dmgbonus = 0
        self.lvl = 1
        self.ranged = True
        self.energycost = 3
