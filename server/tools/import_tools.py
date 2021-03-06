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

    with open('tools.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile)
        
        for item in data:
            item = dict(item)

        # Add document
            if item['name'] and item['category']:
                collection = db['tools.'+item['category']]           
                if item['weight'] == '-':
                    item['weight'] = 0
                collection.insert_one({'name': item['name'], 'price': item['price'],
                    'weight': item['weight']})


            


if __name__ == '__main__':
    return_value = main()