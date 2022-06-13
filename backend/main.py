
from requests_html import HTMLSession
import csv
from json import dumps
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/": {"origins": ""}})

def extrair(url):
    site = "https://br.investing.com/"
    if "crypto" in url:
        url = site + url + "/historical-data"
    if "currencies" in url:
        url = site + url + "-historical-data"

    if "indices" in url:
        url = site + url + "-historical-data"
    session = HTMLSession()

    resp = session.get(url)

    if "indices" in url:
        indices_tags = resp.html.find("#curr_table")
        indices_table = [tag.text for tag in indices_tags]
        json_string = dumps(indices_table)
        fechamento_indice = json_string[81:89]
        if json_string[89] == "\\":
            fechamento_indice = json_string[81:89]
        elif json_string[88] == "\\":
            fechamento_indice = json_string[81:88]
        elif json_string[87] == "\\":
            fechamento_indice = json_string[81:87]
        elif json_string[86] == "\\":
            fechamento_indice = json_string[81:86]

        return fechamento_indice

    if "crypto" in url:
        cryptos_tags = resp.html.find("#curr_table")
        cryptos_table = [tag.text for tag in cryptos_tags]
        json_string = dumps(cryptos_table)
        fechamento_crypto = json_string[81:89]
        if json_string[89] == "\\":
            fechamento_crypto = json_string[81:89]
        elif json_string[88] == "\\":
            fechamento_crypto = json_string[81:88]
        elif json_string[87] == "\\":
            fechamento_crypto = json_string[81:87]
        elif json_string[86] == "\\":
            fechamento_crypto = json_string[81:86]

        return fechamento_crypto

    if "currencies" in url:
        currencies_tags = resp.html.find("#curr_table")
        currencies_table = [tag.text for tag in currencies_tags]
        json_string = dumps(currencies_table)
        fechamento_currencies = json_string[75:81]

        return fechamento_currencies

def lendo_ativos():
    global indices_dados, cryptos_dados, currencies_dados
    with open('input.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        lista = []
        for row in spamreader:
            ativos = ', '.join(row)
            lista.append(ativos)

    indices_dados = list(filter(lambda x: "indices" in x, lista))
    cryptos_dados = list(filter(lambda x: "crypto" in x, lista))
    currencies_dados = list(filter(lambda x: "currencies" in x, lista))
    enviar_indice()
    enviar_crypto()
    enviar_currencies()

def enviar_indice():
    i = 0
    id = 0
    with open('indices.csv', 'w', encoding='UTF8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', lineterminator='\n')

        for x in range(len(indices_dados)):
            for k in indices_dados:
                resultado = []
                id = i
                resultado.append(id)
                indices_nome = k[8:]
                resultado.append(indices_nome)
                try:
                    indices_result = extrair(indices_dados[x+i])
                    i = 1+i
                except:
                    break

                resultado.append(indices_result)
                spamwriter.writerows([resultado])


def enviar_crypto():
    i = 0
    id = 0
    with open('cryptos.csv', 'w', encoding='UTF8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
        for x in range(len(cryptos_dados)):
            for k in cryptos_dados:
                resultado = []
                id = i
                resultado.append(id)
                cryptos_nome = k[7:]
                resultado.append(cryptos_nome)

                try:
                    crypto_result = extrair(cryptos_dados[x+i])
                    i = 1+i
                except:
                    break

                resultado.append(crypto_result)
                spamwriter.writerows([resultado])


def enviar_currencies():
    i = 0
    id = 0
    with open('currencies.csv', 'w', encoding='UTF8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
        for x in range(len(currencies_dados)):
            for k in currencies_dados:
                resultado = []
                id = i
                resultado.append(id)
                currencies_nome = k[11:]
                resultado.append(currencies_nome)
                try:
                    currencies_result = extrair(currencies_dados[x+i])
                    i = 1+i
                except:
                    break

                resultado.append(currencies_result)
                spamwriter.writerows([resultado])


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
    data = []
    with open('indices.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for x in spamreader:
            data.append({
                "nome": x[0],
                "fechamento": x[1],
            })
    with open('cryptos.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for x in spamreader:
            data.append({
                "nome": x[0],
                "fechamento": x[1],
            })
    with open('currencies.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
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
