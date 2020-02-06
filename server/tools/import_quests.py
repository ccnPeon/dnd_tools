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

    with open('quests.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile)
        
        for item in data:
            item = dict(item)

        # Add document
            collection.insert_one({'name': item['name', 'data': item['data']})


            


if __name__ == '__main__':
    return_value = main()