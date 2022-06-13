from flask_cors import CORS,cross_origin
from flask import Flask, request,jsonify
import csv
from json import dumps
from script import *

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

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



@app.route('/todos', methods=['GET'])
def todos():
    data_all=[]
    i=0
    with open('indices.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')

        for x in spamreader:
            data_all.append({
                "id": x[0],
                "tipo": "indice",
                "nome": x[1],
                "fechamento": x[2],
            })
            i = 1+i
    with open('cryptos.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')

        for x in spamreader:
            data_all.append({
                "id": i,
                "tipo": "crypto",
                "nome": x[1],
                "fechamento": x[2],
            })
            i = 1+i
    with open('currencies.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')

        for x in spamreader:
            data_all.append({
                "id": i,
                "tipo": "currencies",
                "nome": x[1],
                "fechamento": x[2],
            })
            i = 1+i
    return dumps(data_all, indent=4)


@app.route('/json', methods=['POST'])
@cross_origin(supports_credentials=True)
def json():
    request_data = request.get_json()

    result = []
    if request_data:
        if 'indices' in request_data:
            if (type(request_data['indices']) == list) and (len(request_data['indices']) > 0):
                indices_data = request_data['indices']
                for x in range(len(indices_data)):
                    result.append(indices_data[0+x])

        if 'crypto' in request_data:
            if (type(request_data['crypto']) == list) and (len(request_data['crypto']) > 0):
                crypto_data = request_data['crypto']
                for i in range(len(crypto_data)):
                    result.append(crypto_data[0+i])
        if 'currencies' in request_data:
            if (type(request_data['currencies']) == list) and (len(request_data['currencies']) > 0):
                currencies_data = request_data['currencies']
                for k in range(len(currencies_data)):
                    result.append(currencies_data[0+k])

        
       
        
        with open('input.csv', 'w', encoding='UTF8') as csvfile:
            spamwriter = csv.writer(
                csvfile, delimiter=' ', lineterminator='\n')
            for o in range(len(result)):
                spamwriter.writerow([result[o]])
        lendo_ativos()

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)