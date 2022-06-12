# import main Flask class and request object
from flask import Flask, request,jsonify
import csv

# create the Flask app
app = Flask(__name__)


@app.route('/indices', methods=['GET'])
def form_example():
    with open('indices.csv', encoding='UTF8', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            data = []
            for x in spamreader:
                data.append({
                    "nome": x[0],
                    "fechamento": x[1],
                })
    return jsonify(data) 

@app.route('/crypto', methods=['GET'])
def crypto():
    with open('crypto.csv', encoding='UTF8', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            data = []
            for x in spamreader:
                data.append({
                    "nome": x[0],
                    "fechamento": x[1],
                })
    return jsonify(data)

@app.route('/currencies', methods=['GET'])
def currencies():
    with open('currencies.csv', encoding='UTF8', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ')
            data = []
            for x in spamreader:
                data.append({
                    "nome": x[0],
                    "fechamento": x[1],
                })
    return jsonify(data)

@app.route('/json', methods=['POST'])
def json():
    request_data = request.get_json()

    result = []
    if request_data:
        if 'indices' in request_data:
            if (type(request_data['indices']) == list) and (len(request_data['indices']) > 0):
                indices = request_data['indices']

        if 'crypto' in request_data:
            if (type(request_data['crypto']) == list) and (len(request_data['crypto']) > 0):
                crypto = request_data['crypto']
        if 'currencies' in request_data:
            if (type(request_data['currencies']) == list) and (len(request_data['currencies']) > 0):
                currencies = request_data['currencies']


        for x in range(len(indices)):
            result.append(indices[0+x])
        for i in range(len(crypto)):
            result.append(crypto[0+i])
        for k in range(len(currencies)):
            result.append(currencies[0+k])
        with open('input.csv', 'w',encoding='UTF8') as csvfile:
                spamwriter = csv.writer(csvfile,delimiter=' ',lineterminator='\n')
                for o in range(len(result)):
                    spamwriter.writerow([result[o]])

            
    return '''
           The indices value is: {}
           The crypto value is: {}
           The currencies value is: {}          
'''.format(indices, crypto, currencies)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)