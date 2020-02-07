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

    def get_tools(self, argument):
        return_info = '```\n'
        if argument in self.db.collection_names():
            current_collection = self.db[argument]
            collection_name = argument
        else:
            return 'Data not found.'
        collection_name_parsed = collection_name.replace('tools.', '').split('_')
        return_info += '============================================{0}============================================*\n'.format(((collection_name_parsed[0].capitalize() + ' ' + collection_name_parsed[1].capitalize()) if len(collection_name_parsed) == 2 else collection_name_parsed[0].capitalize()))
        name_column = 'Name'.center(50, ' ')
        price_column = 'Price'.center(50, ' ')
        weight_column = 'Weight'.center(50, ' ')
        return_info += '%s|%s|%s\n' % (name_column, price_column, weight_column)
        for document in current_collection.find({}):
            return_info += document['name'].ljust(50, ' ')[:51] + '|' + document['price'].center(50, ' ')[:51] + '|' \
                           + document['weight'].center(50, ' ')[:51] + '\n'
        return_info += '```'
        return return_info

    def get_tool_options(self):
        return_info = ''
        return_info += '*=================================Tool Choices=================================*\n'
        for item in self.db.collection_names():
            if 'tools.' in item:
                return_info += item.replace('tools.', '') + '\n'
            else:
                pass
        return return_info


    def get_weapon_options(self):
        return_info = ''
        return_info += '=================================Weapon Choices=================================\n'
        for item in self.db.collection_names():
            if 'weapons.' in item:
                return_info += item.replace('weapons.', '') + '\n'
            else:
                pass
        return return_info


    def get_weapons(self, argument):
        return_info = '```\n'
        if argument in self.db.collection_names():
            current_collection = self.db[argument]
            collection_name = argument
        else:
            return 'Data not found.'
        collection_name_parsed = collection_name.replace('weapons.', '').split('_')
        return_info += '============================================{0}============================================\n'.format(((collection_name_parsed[0].capitalize() + ' ' + collection_name_parsed[1].capitalize()) if len(collection_name_parsed) == 2 else collection_name_parsed[0].capitalize()))
        name_column = 'Name'.center(25, ' ')
        price_column = 'Price'.center(25, ' ')
        damage_column = 'Damage'.center(25, ' ')
        weight_column = 'Weight'.center(25, ' ')
        properties_column = 'Properties'.center(25, ' ')
        return_info += '%s|%s|%s|%s|%s\n' % (name_column,price_column,damage_column,weight_column,properties_column)
        for document in current_collection.find({}):
            return_info += document['name'].ljust(25, ' ')[:26] + '|' + document['price'].center(25, ' ')[:26] + '|' \
                + document['damage'].center(25, ' ')[:26] + '|' +  document['weight'].center(25, ' ')[:26] + '|' \
                + document['properties'].center(25, ' ',) +  '\n'
        return_info += '```'
        return return_info

    def get_armor_options(self):
        return_info = '```\n'
        return_info += '=================================Armor Choices=================================\n'
        for item in self.db.collection_names():
            if 'armor.' in item:
                return_info += item.replace('armor.', '') + '\n'
            else:
                pass
        return_info += '```'
        return return_info


    def get_armor(self, argument):
        return_info = '```\n'
        if argument in self.db.collection_names():
            current_collection = self.db[argument]
            collection_name = argument
        else:
            return 'Data not found.'
        collection_name_parsed = collection_name.replace('armor.', '').split('_')
        return_info += ('=' * 25) + '{0}'.format(((collection_name_parsed[0].capitalize() + ' ' + collection_name_parsed[1].capitalize()) if len(collection_name_parsed) == 2 else collection_name_parsed[0].capitalize())) + ('=' * 25) + '\n'
        name_column = 'Name'.center(25, ' ')
        price_column = 'Price'.center(25, ' ')
        weight_column = 'Weight'.center(25, ' ')
        armor_class_column = 'Armor Class'.center(25, ' ')
        stealth_column = 'stealth'.center(25, ' ')
        strength_column = 'strength'.center(25, ' ')

        return_info += '%s|%s|%s|%s|%s|%s\n' % (name_column,price_column,armor_class_column,weight_column,stealth_column,strength_column)
        for document in current_collection.find({}):
            return_info += document['name'].ljust(25, ' ')[:26] + '|' + document['price'].center(25, ' ')[:26] + '|' \
                + document['weight'].center(25, ' ')[:26] + '|' + document['armor_class'].center(25, ' ') + '|' \
                + document['stealth'].center(25, ' ')[:26]  + '|' \
                + document['strength'].center(25, ' ',)[:26] +  '\n'
        return_info += '```'
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