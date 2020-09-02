import pymongo
import json
import os
import sys


class Database(object):
    URI = "mongodb+srv://{}:{}@cluster0.sfoyz.mongodb.net/<dbname>?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        # retrieve login info
        f = open(os.path.join(sys.path[0], 'db_config.json'))
        config = json.load(f)
        user = config['user']
        password = config['password']
        f.close

        db = 'pricing'
        Database.URI = "mongodb+srv://{}:{}@cluster0.sfoyz.mongodb.net/{}?retryWrites=true&w=majority".format(
            user, password, db)

        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[db]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
