class Weapon(object):
    def __init__(self):
        self.id = None
        self.energycost = 2
        self.cubes = 2
        self.dmgbonus = 0
        self.name = 'None'
        self.ranged = False
        self.accuracybonus = 0
        self.classic = False
        self.modification = 0
        self.lvl = 0


class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 3
        self.accuracybonus = 3
        self.energycost = 3

class Pistol_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1001
        self.name = 'Пистолет'
        self.ranged = True
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.classic = True


class Revolver(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 6
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 0
        self.energycost = 3
        self.accuracybonus = 2

class Revolver_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1006
        self.name = 'Револьвер'
        self.ranged = True
        self.cubes = 3
        self.dmgbonus = 0
        self.energycost = 3
        self.accuracybonus = 1
        self.classic = True


class Baseball(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.name = 'Бита'
        self.accuracybonus = 2
        self.cubes = 3

class Baseball_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1002
        self.name = 'Бита'
        self.accuracybonus = 2
        self.cubes = 3
        self.classic = True


class Obrez(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.name = 'Обрез'
        self.energycost = 3
        self.accuracybonus = 0
        self.cubes = 4
        self.ranged = True

class Obrez_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1004
        self.name = 'Обрез'
        self.energycost = 3
        self.accuracybonus = 0
        self.cubes = 4
        self.ranged = True
        self.classic = True


class Drobovik(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 5
        self.name = 'Дробовик'
        self.energycost = 4
        self.dmgbonus = 1
        self.cubes = 6
        self.ranged = True
        self.accuracybonus = -2

class Drobovik_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1005
        self.name = 'Дробовик'
        self.energycost = 4
        self.dmgbonus = 1
        self.cubes = 6
        self.ranged = True
        self.accuracybonus = -2
        self.classic = True


class Knife(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.name = 'Нож'
        self.accuracybonus = 2
        self.cubes = 3

class Knife_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1003
        self.name = 'Нож'
        self.accuracybonus = 2
        self.cubes = 3
        self.classic = True


class Torch(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 7
        self.name = 'Факел'
        self.accuracybonus = 2
        self.cubes = 3

class Torch_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1007
        self.name = 'Факел'
        self.accuracybonus = 2
        self.cubes = 3
        self.classic = True

class Flamethrower(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 8
        self.name = 'Огнемет'
        self.ranged = True
        self.energycost = 3
        self.cubes = 2
        self.accuracybonus = 2


class Flamethrower_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1008
        self.name = 'Огнемет'
        self.ranged = True
        self.energycost = 3
        self.cubes = 2
        self.accuracybonus = 2
        self.classic = True

class PenisDubina(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 9
        self.name = 'Пенис-дубина'
        self.energycost = 5
        self.cubes = 2
        self.dmgbonus = 4
        self.accuracybonus = 0


class Fist(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 10
        self.name = 'Кулаки'
        self.accuracybonus = 4
        self.cubes = 1

class Fist_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1010
        self.name = 'Кулаки'
        self.accuracybonus = 4
        self.cubes = 1
        self.classic = True


class Rifle(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 11
        self.name = 'Снайперская винтовка'
        self.ranged = True
        self.cubes = 1
        self.accuracybonus = -4
        self.energycost = 5
        self.dmgbonus = 7

class Rifle_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1011
        self.name = 'Снайперская винтовка'
        self.ranged = True
        self.cubes = 1
        self.accuracybonus = -4
        self.energycost = 5
        self.dmgbonus = 7
        self.classic = True


class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 12
        self.name = 'Топор'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Axe_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1012
        self.name = 'Топор'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Bulava(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 13
        self.name = 'Булава'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Bulava_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1013
        self.name = 'Булава'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Kastet(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 14
        self.name = 'Кастет'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Kastet_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1014
        self.name = 'Кастет'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Kuvalda(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 15
        self.name = 'Кувалда'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Kuvalda_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1015
        self.name = 'Кувалда'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Chain(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 16
        self.name = 'Цепь'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Chain_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1016
        self.name = 'Цепь'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Narsil(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 17
        self.name = 'Копье Нарсил'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Narsil_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1017
        self.name = 'Копье Нарсил'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Spear(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 18
        self.name = 'Копье'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Spear_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1018
        self.name = 'Копье'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class BowAsgard(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 19
        self.name = 'Лук Асгард'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 1
        self.dmgbonus = 0
        self.ranged = True


class Bite(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 20
        self.name = 'Укус зомби'
        self.cubes = 3
        self.accuracybonus = 0
        self.energycost = 0
        self.dmgbonus = 0


class Katana(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 21
        self.name = 'Катана'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Saber(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 22
        self.name = 'Сабля'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Granatomet(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 23
        self.name = 'Гранатомет'
        self.cubes = 4
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class Bow(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 24
        self.name = 'Лук'
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class Non(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 25
        self.name = 'None'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Claws(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 26
        self.name = 'Стальные когти'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Electro(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 27
        self.name = 'Электрошокер'
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class Saw(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 28
        self.name = 'Пиломет'
        self.cubes = 2
        self.accuracybonus = 3
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class Police(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 29
        self.name = 'Полицейская дубинка'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0

class Police_classic(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 1029
        self.name = 'Полицейская дубинка'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.classic = True


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 30
        self.name = 'Меч'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 5
        self.dmgbonus = 0


class Rock(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 31
        self.name = 'Камень'
        self.cubes = 100
        self.accuracybonus = 100
        self.energycost = 0
        self.dmgbonus = -100
        self.ranged = True


class Water(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 32
        self.name = 'Водомет'
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class Shurikens(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 33
        self.name = 'Сюрикены'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.ranged = True


class SkeletonKingSword(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 34
        self.name = 'Меч короля'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class VampireBite(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 35
        self.name = 'Клыки вампира'
        self.cubes = 4
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class DemonlordEye(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 36
        self.name = 'Глаз демона'
        self.cubes = 2
        self.accuracybonus = 3
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class Horn(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 37
        self.name = 'Рог'
        self.cubes = 3
        self.accuracybonus = 4
        self.energycost = 1
        self.dmgbonus = 0


class Shield(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 38
        self.name = 'Щит'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Molot(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 39
        self.name = 'Молот'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Sword2(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 40
        self.name = 'Меч '
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class FireSword(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 41
        self.name = 'Пылающий клинок'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class Treant_hand(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 42
        self.name = 'Рука трента'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class LightSword(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 43
        self.name = 'Меч Света'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class VirusHit(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 44
        self.name = 'Конечность вируса'
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 0
        self.ranged = True
        self.dmgbonus = 1


class Shest(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 45
        self.name = 'Шест'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class WeakSkeleSword(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 46
        self.name = 'Меч дряхлого скелета'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0


class GhoulTeeth(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 47
        self.name = 'Зубы вурдалака'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 1


class NecromantStaff(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 48
        self.name = 'Посох некроманта'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.ranged = True


class MadSkeleWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 49
        self.name = 'Мраморная колонна'
        self.cubes = 15
        self.accuracybonus = 15
        self.energycost = 5
        self.dmgbonus = 0


class NecromantStaff_players(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 50
        self.name = 'Посох Некроманта'
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True


class MachineGun(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 51
        self.name = "Пулемет"
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 100
        self.dmgbonus = 0
        self.ranged = True

class DuelRapier(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 52
        self.name = "Дуэльная рапира"
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.ranged = False

class MagicStaff(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 53
        self.name = "Волшебный посох"
        self.cubes = 1
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True

class OgreGrenadeLauncher(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 54
        self.name = "Гранатомет огра"
        self.cubes = 4
        self.accuracybonus = 0
        self.energycost = 5
        self.dmgbonus = 5
        self.ranged = False

class Yatagan(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 55
        self.name = "Ятаган"
        self.cubes = 3
        self.accuracybonus = 0
        self.energycost = 2
        self.dmgbonus = 1
        self.ranged = False

class DarkRatWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 56
        self.name = "Частица тьмы"
        self.cubes = 3
        self.accuracybonus = 1000000
        self.energycost = 0
        self.dmgbonus = 0
        self.ranged = True

class AmalgamaFirstWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 57
        self.name = "Огромный тесак"
        self.cubes = 1
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 9
        self.ranged = True

class AmalgamaSecondWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 58
        self.name = "Теневая пушка"
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 5
        self.dmgbonus = 0
        self.ranged = True

class AmalgamaThirdWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 59
        self.name = "Пасть собаки"
        self.cubes = 4
        self.accuracybonus = 3
        self.energycost = 0
        self.dmgbonus = 1
        self.ranged = True

class AmalgamaNoneWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 60
        self.name = "Отсутствует"
        self.cubes = 100
        self.accuracybonus = 100
        self.energycost = 0
        self.dmgbonus = 100
        self.ranged = True

class Tesak(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 61
        self.name = "Тесак"
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 2
        self.dmgbonus = 0
        self.ranged = False

class Staff(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 62
        self.name = 'Посох'
        self.accuracybonus = 2
        self.cubes = 2

class DarknessWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 63
        self.name = 'Неизвестно'
        self.accuracybonus = 2
        self.cubes = 4
        
class FrozenBow(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 64
        self.name = 'Морозный лук'
        self.cubes = 3
        self.accuracybonus = 1
        self.energycost = 3
        self.dmgbonus = 0
        self.ranged = True

class OnePunch(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 65
        self.name = 'One punch'
        self.cubes = 3
        self.accuracybonus = 2
        self.energycost = 999999
        self.dmgbonus = 9999999
        self.ranged = False

class Flamethrower_narsil(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 66
        self.name = 'Огнемет Нарсил'
        self.ranged = True
        self.energycost = 3
        self.cubes = 2
        self.accuracybonus = 2

class ImpSpear(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 67
        self.name = 'Трезубец'
        self.ranged = False
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 2

class MagmawormClaws(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 68
        self.name = 'Клыки червя'
        self.ranged = False
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 2

class LuciferBlade(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 69
        self.name = 'Пылающий клинок'
        self.ranged = False
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 3


class Crossbow(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 70
        self.name = 'Арбалет'
        self.ranged = True
        self.energycost = 3
        self.cubes = 3
        self.accuracybonus = 2

class SnowmanWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 71
        self.name = 'Снеговая пушка'
        self.ranged = True
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 2

class Buckshot(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 72
        self.name = 'Ружье'
        self.ranged = True
        self.energycost = 0
        self.cubes = 1
        self.accuracybonus = 10000

class EyedemonWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 73
        self.name = 'Щупальца'
        self.ranged = False
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 2

class AlastorRod(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 74
        self.name = 'Демоническая сила'
        self.ranged = True
        self.energycost = 0
        self.cubes = 3
        self.accuracybonus = 2

class DragonClaws(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 75
        self.name = 'Когти дракона'
        self.ranged = False
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 2

class Yatagan(Weapon):
    def __init__(self):
        super().__init__()
        self.id = 76
        self.name = 'Ятаган'
        self.ranged = False
        self.energycost = 2
        self.cubes = 3
        self.accuracybonus = 2
