from pymongo import MongoClient
from .connection_info import ConnectionInfo
    
class DNDLiason():
    def __init__(self):
        self.connection = MongoClient(
            host='{0}:{1}'.format(ConnectionInfo().get_server(),ConnectionInfo().get_port()),
            username=ConnectionInfo().get_username(),
            password=ConnectionInfo().get_password(),
            authSource=ConnectionInfo().get_database()
            )

        self.db = self.connection[ConnectionInfo().get_database()]
    
    def get_items(self, argument):
        return_info = ''
        if argument in self.db.collection_names():
            current_collection = self.db[argument]
            collection_name = argument
        else:
            return 'Data not found.'
        collection_name_parsed = collection_name.replace('items.', '').split('_')
        return_info += '*======================================={0}=======================================*\n'.format(((collection_name_parsed[0].capitalize() + ' ' + collection_name_parsed[1].capitalize()) if len(collection_name_parsed) == 2 else collection_name_parsed[0].capitalize()))
        name_column = '                    Name                    '
        price_column = '                    Price                    '
        weight_column = '                    Weight                    '
        return_info += '%s|%s|%s\n' % (name_column,price_column,weight_column)
        for document in current_collection.find({}):
            return_info += document['name'] + (' '*((len(name_column) - len(document['name']) - 2) * 2)) \
                + document['price'] + (' '*((len(price_column) - len(document['price']) - 2) * 2)) \
                + str(document['weight']) + '\n'
        return return_info

    def get_item_options(self):
        return_info = ''
        return_info += '*=================================Item Choices=================================*\n'
        for item in self.db.collection_names():
            if 'items.' in item:
                return_info += item.replace('items.', '') + '\n'
            else:
                pass
        return return_info


    def get_weapon_options(self):
        return_info = ''
        return_info += '*=================================Weapon Choices=================================*\n'
        for item in self.db.collection_names():
            if 'weapons.' in item:
                return_info += item.replace('weapons.', '') + '\n'
            else:
                pass
        return return_info


    def get_weapons(self, argument):
        return_info = ''
        if argument in self.db.collection_names():
            current_collection = self.db[argument]
            collection_name = argument
        else:
            return 'Data not found.'
        collection_name_parsed = collection_name.replace('weapons.', '').split('_')
        return_info += '*======================================={0}=======================================*\n'.format(((collection_name_parsed[0].capitalize() + ' ' + collection_name_parsed[1].capitalize()) if len(collection_name_parsed) == 2 else collection_name_parsed[0].capitalize()))
        name_column = '            Name            '
        price_column = '            Price            '
        damage_column = '          Damage          '
        weight_column = '        Weight        '
        properties_column = '            Properties       '

        return_info += '%s|%s|%s|%s|%s\n' % (name_column,price_column,damage_column,weight_column,properties_column)
        for document in current_collection.find({}):
            return_info += document['name'] + (' '*((len(name_column) - len(document['name']) - 6) * 2)) \
                + document['price'] + (' '*((len(price_column) - len(document['price']) - 12) * 2)) \
                + document['damage'] + (' '*((len(damage_column) - len(document['damage']) - 15) * 2)) \
                + str(document['weight']) + (' '*((len(price_column) - len(str(document['weight'])) - 15) * 2)) \
                + document['properties'] + '\n'
        return return_info

    def get_quest_options(self):
        return_info = ''
        return_info += '*=================================Quest Choices=================================*\n'
        collection = self.db['quests']
        for quest in collection.find({}):
            return_info += quest['name'].lower().replace(' ', '_') + '\n'
        return return_info

    def get_quest(self, argument):
        return_info = ''
        collection = self.db['quests']
        for quest in collection.find({}):
            if quest['name'] == argument.replace('_', ' ').title(): 
                return_info += '*=================================%s=================================*\n' % quest['name']
                return_info += quest['data']
                return return_info

        return 'Data not found.'