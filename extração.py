from requests_html import HTMLSession
import csv
import json

def main(url):
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
        open_tags = resp.html.find("#curr_table")
        open = [tag.text for tag in open_tags]
        json_string = json.dumps(open)
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
        open_tags = resp.html.find("#curr_table")
        open = [tag.text for tag in open_tags]
        json_string = json.dumps(open)
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
        open_tags = resp.html.find("#curr_table")
        open = [tag.text for tag in open_tags]
        json_string = json.dumps(open)
        fechamento_currencies = json_string[75:81]

        return fechamento_currencies

def lendo_ativos():
    global indices, crypto, currencies
    with open('input.csv', encoding='UTF8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        lista = []
        for row in spamreader:
            ativos = ', '.join(row)
            lista.append(ativos)
            
        
    indices=list(filter(lambda x: "indices" in x, lista))
    crypto=list(filter(lambda x: "crypto" in x, lista))
    currencies=list(filter(lambda x: "currencies" in x, lista))

def enviar_indice():
    i=0
    with open('indices.csv', 'w',encoding='UTF8') as csvfile:
        spamwriter = csv.writer(csvfile,delimiter=' ',lineterminator='\n')

        for x in range(len(indices)):
            for k in indices:
                
                resultado = []
                indices_nome=k[8:] 
                resultado.append(indices_nome)
                try:
                    indices_result=main(indices[x+i])
                    i= 1+i
                except:
                    break
                
                resultado.append(indices_result)
                spamwriter.writerows([resultado])
                
def enviar_crypto():
    i=0
    with open('crypto.csv', 'w',encoding='UTF8') as csvfile:
        spamwriter = csv.writer(csvfile,delimiter=' ',lineterminator='\n')

        for x in range(len(crypto)):
            for k in crypto:
                
                resultado = []
                indices_nome=k[7:] 
                resultado.append(indices_nome)
                try:
                    crypto_result=main(crypto[x+i])
                    i= 1+i
                except:
                    break
                
                resultado.append(crypto_result)
                print(resultado)
                spamwriter.writerows([resultado])


def enviar_currencies():
    i=0
    with open('currencies.csv', 'w',encoding='UTF8') as csvfile:
        spamwriter = csv.writer(csvfile,delimiter=' ',lineterminator='\n')
        for x in range(len(currencies)):
            for k in currencies:
                
                resultado = []
                currencies_nome=k[11:] 
                resultado.append(currencies_nome)
                try:
                    currencies_result=main(currencies[x+i])
                    i= 1+i
                except:
                    break
                
                resultado.append(currencies_result)
                print(resultado)
                spamwriter.writerows([resultado])


if __name__ == "__main__":
    lendo_ativos()
    enviar_indice()
    enviar_crypto()
    enviar_currencies()
    