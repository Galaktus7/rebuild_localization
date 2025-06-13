def createcastle(castle):
    return {
        castle: {
            'name': castle,
            'defers': {},
            'attackers': {},
            'saved': True,
            'score': 0
        }
    }

def castle_to_emoji(x):
    if x == 'rat':
        return '🐭'
    if x == 'darkcastle':
        return '👁'
    if x == 'necromant':
        return '🖤'
    if x == 'explosion':
        return '💮'
    return 'None'
    
def castle_to_name(x):
    if x == 'rat':
        return "🐭Крысиный замок"
    if x == 'darkcastle':
        return "👁Замок тьмы"
    if x == 'necromant':
        return "🖤Замок некроманта"
    if x == 'explosion':
        return "💮Замок магии взрывов"
    return None
    
def emoji_to_castle(x):
    if x == '🐭':
        return 'rat'
    if x == '👁':
        return 'darkcastle'
    if x == '🖤':
        return 'necromant'
    if x == '💮':
        return 'explosion'
    
def name_to_castle(x):
    if x == "🐭Крысиный замок":
        return 'rat'
    if x == "👁Замок тьмы":
        return 'darkcastle'
    if x == "🖤Замок некроманта":
        return 'necromant'
    if x == "💮Замок магии взрывов":
        return 'explosion'