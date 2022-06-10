from requests_html import HTMLSession
import csv
import json



def Captura_de_dados(url):
    print(url)
    site="https://br.investing.com/"
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
        fechamento=json_string[81:89]
        if json_string[89] == "\\":
            fechamento = json_string[81:89]
        elif json_string[88] == "\\":
            fechamento = json_string[81:88]
        elif json_string[87] == "\\":
            fechamento = json_string[81:87]
        elif json_string[86] == "\\":
            fechamento = json_string[81:86]
       
        print(fechamento)

    if "crypto" in url:
        open_tags = resp.html.find("#curr_table")
        open = [tag.text for tag in open_tags]
        json_string = json.dumps(open)
        fechamento=json_string[81:89]
        if json_string[89] == "\\":
            fechamento = json_string[81:89]
        elif json_string[88] == "\\":
            fechamento = json_string[81:88]
        elif json_string[87] == "\\":
            fechamento = json_string[81:87]
        elif json_string[86] == "\\":
            fechamento = json_string[81:86]
            
        print(fechamento)

    if "currencies" in url:
        # open_tags = resp.html.find("tr td")
        # open = [tag.text for tag in open_tags]
        # open = open[31]
        # print(open)
        open_tags = resp.html.find("#curr_table")
        open = [tag.text for tag in open_tags]
        json_string = json.dumps(open)
        fechamento=json_string[75:81]
        # if json_string[91] == "\\":
        #     fechamento = json_string[83:91]
        # elif json_string[90] == "\\":
        #     fechamento = json_string[83:88]
        # elif json_string[89] == "\\":
        #     fechamento = json_string[83:89]
        # elif json_string[88] == "\\":
        #     fechamento = json_string[83:88]
            
        print(fechamento)
    
with open('ativos.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     lista= []
     for row in spamreader:
         ativos= ', '.join(row)
         lista.append(ativos)
         
         

for x in range(len(lista)):    
    Captura_de_dados(lista[0+x])