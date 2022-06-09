from requests_html import HTMLSession

print("digite a url:")
url=input("")

if "crypto" in url:
    url = url + "/historical-data"
if "currencies" in url:
    url = url + "-historical-data"

if "indices" in url:
    url = url + "-historical-data"


print(url)
def Captura_de_dados(url):
    
    session = HTMLSession()
    
    resp = session.get(url)
    
    if "indices" in url:
        open_tags = resp.html.find(".float_lang_base_2.bold")
        open = [tag.text for tag in open_tags]
        open = open[1]
        print(open)
    if "crypto" in url:
        open_tags = resp.html.find("tr td")
        open = [tag.text for tag in open_tags]
        open = open[1]
        print(open)
    if "currencies" in url:
        open_tags = resp.html.find("tr td")
        open = [tag.text for tag in open_tags]
        open = open[31]
        print(open)
    

Captura_de_dados(url)