from flask_cors import CORS
from flask import Flask, request
import csv
from json import dumps
from script import *

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/": {"origins": ""}})


@app.route('/indices', methods=['GET'])
def indices():
    with open('indices.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        data = []
        for x in spamreader:
            data.append({
                "id": x[0],
                "nome": x[1],
                "fechamento": x[2]
            })
    return dumps(data, indent=4)


@app.route('/cryptos', methods=['GET'])
def cryptos():
    with open('cryptos.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        data = []
        for x in spamreader:
            data.append({
                "id": x[0],
                "nome": x[1],
                "fechamento": x[2],
            })
    return dumps(data, indent=4)


@app.route('/currencies', methods=['GET'])
def currencies():
    with open('currencies.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        data = []
        for x in spamreader:
            data.append({
                "id": x[0],
                "nome": x[1],
                "fechamento": x[2],
            })
    return dumps(data, indent=4)


@app.route('/json', methods=['POST'])
def json():
    request_data = request.get_json()

    result = []
    if request_data:
        if 'indices' in request_data:
            if (type(request_data['indices']) == list) and (len(request_data['indices']) > 0):
                indices_data = request_data['indices']

        if 'crypto' in request_data:
            if (type(request_data['crypto']) == list) and (len(request_data['crypto']) > 0):
                crypto_data = request_data['crypto']
        if 'currencies' in request_data:
            if (type(request_data['currencies']) == list) and (len(request_data['currencies']) > 0):
                currencies_data = request_data['currencies']

        for x in range(len(indices_data)):
            result.append(indices_data[0+x])
        for i in range(len(crypto_data)):
            result.append(crypto_data[0+i])
        for k in range(len(currencies_data)):
            result.append(currencies_data[0+k])
        with open('input.csv', 'w', encoding='UTF8') as csvfile:
            spamwriter = csv.writer(
                csvfile, delimiter=' ', lineterminator='\n')
            for o in range(len(result)):
                spamwriter.writerow([result[o]])
        lendo_ativos()

    return '''
           The indices value is: {}
           The crypto value is: {}
           The currencies value is: {}          
            '''.format(indices_data, crypto_data, currencies_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)