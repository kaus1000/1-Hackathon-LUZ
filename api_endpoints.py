from flask import Flask
from flask_restful import Resource, Api,reqparse
import pandas as pd
import csv

app = Flask(__name__)
api = Api(app)


class Indices(Resource):
    def get(self):
        with open('indices.csv', encoding='UTF8', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            data = []
            for x in spamreader:
                data.append({
                    "nome": x[0],
                    "fechamento": x[1],
                })

        return {'data': data}, 200  # return data and 200 OK code
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        # read our CSV
        data = pd.read_csv('users.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200  # return data with 200 OK


class Crypto(Resource):
     def get(self):
        with open('crypto.csv', encoding='UTF8', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ')
                data = []
                for x in spamreader:
                    data.append({
                        "nome": x[0],
                        "fechamento": x[1],
                    })
                
        return {'data': data}, 200  # return data and 200 OK code
    
    
class Currencies(Resource):
     def get(self):
        with open('Currencies.csv', encoding='UTF8', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ')
                data = []
                for x in spamreader:
                    data.append({
                        "nome":x[0],
                        "fechamento":x[1],
                    })
                    
        return {'data': data}, 200  # return data and 200 OK code



    
api.add_resource(Indices, '/Indices') 
api.add_resource(Crypto, '/Crypto')  
api.add_resource(Currencies, '/Currencies')  


if __name__ == '__main__':
    app.run()  # run our Flask app