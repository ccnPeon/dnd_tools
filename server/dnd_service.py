from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from include.dnd_liason import DNDLiason
import re

app = Flask(__name__)
api = Api(app)
liason = DNDLiason()

class GetAllItems(Resource):
    def post(self):
        received_data = request.get_data().decode("utf-8")
        parse_data = re.search('dndtools+.*&', received_data).group(0)[9:-1]
        split_data = parse_data.split('+')
        print(split_data)
        if len(split_data) == 1:
            if split_data[0] == 'items':
                return_data = {'text': liason.get_item_options()}
                return return_data, 201

            elif split_data[0] == 'tools':
                return_data = {'text': liason.get_tool_options()}
                return return_data, 201

            elif split_data[0] == 'weapons':
                return_data = {'text': liason.get_weapon_options()}
                return return_data, 201
            
            elif split_data[0] == 'armor':
                return_data = {'text': liason.get_armor_options()}
                return return_data, 201

            elif split_data[0] == 'quests':
                return_data = {'text': liason.get_quest_options() }
                return return_data

        if len(split_data) == 2:
            if split_data[0] == 'items':
                request_argument = 'items.%s' % split_data[1]
                return_data = {'text': liason.get_items(request_argument)}
                return return_data, 201

            elif split_data[0] == 'tools':
                request_argument = 'tools.%s' % split_data[1]
                return_data = {'text': liason.get_tools(request_argument)}
                return return_data, 201

            elif split_data[0] == 'weapons':
                request_argument = 'weapons.%s' % split_data[1]
                return_data = {'text': liason.get_weapons(request_argument)}
                return return_data, 201

            elif split_data[0] == 'armor':
                request_argument = 'armor.%s' % split_data[1]
                return_data = {'text': liason.get_armor(request_argument)}
                return return_data, 201
            
            elif split_data[0] == 'quests':
                request_argument = split_data[1]
                return_data = {'text': liason.get_quest(request_argument)}
                return return_data, 201
        
        else:
            return_data = {'text': 'Data not found.'}
            return return_data

api.add_resource(GetAllItems, '/get/items/all')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)