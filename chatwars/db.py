from pymongo import MongoClient
from constants import castlelist


class CWDatabase:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = client.veganwars_rebuild

        self.users = self.db.veganochatwarsusers
        self.castles = self.db.veganochatwarscastles
        self.auction = self.db.cwauction
        self.resourceauc = self.db.resourceauc
        self.last_battle = self.db.lastcastlebattletime
        self.troll = self.db.troll

        self.initialize_data()

    def initialize_data(self):
        if not self.last_battle.find_one({}):
            self.last_battle.insert_one({'time': 0})

        if not self.castles.find_one({}):
            commit = {castle: {'score': 0, 'name': castle, 'loosestreak': 0} for castle in castlelist}
            self.castles.insert_one(commit)

    def get_user(self, user_id: int):
        return self.users.find_one({'id': user_id})

    def clean_for_battle(self):
        self.users.update_many({}, {'$set': {'changebattlegold': 0,
                                             'changebattleres': {},
                                             'changebattleexp': 0}
                                    })

    def earn_battle_exp(self, user_id: int, count: int):
        self.users.update_one({'id': user_id}, {'$inc': {'exp': count, 'changebattleexp': count}})