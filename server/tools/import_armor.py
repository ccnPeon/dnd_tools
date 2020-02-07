from pymongo import MongoClient
import csv


###########Global Variables############
server = 'mongodb'
port = '27017'
username = 'bg'
password = 'BrandonGreer1234$'
database = 'dnd'

def main():
    connection = MongoClient(server,username=username,password=password,authSource=database)
    
    db = connection[database]
    collections = db.list_collection_names()

    with open('armor.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile)
        
        for item in data:
            item = dict(item)

        # Add document
            if item['name'] and item['category']:
                collection = db['armor.'+item['category']]           
                if item['stealth'] == '':
                    item['stealth'] = 'N/A'
                if item['strength'] == '':
                    item['strength'] = 'N/A'
                if item['weight'] == '-':
                    item['weight'] = 0
                collection.insert_one({'name': item['name'], 'price': item['price'],
                    'armor_class': item['ac'], 'weight': item['weight'],
                    'stealth': item['stealth'], 'strength': item['strength']})


            


if __name__ == '__main__':
    return_value = main()