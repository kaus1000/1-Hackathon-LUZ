from requests_html import HTMLSession

function = input("Digite 1 para receber dados dos indices futuros ou Digite 2 para receber dados das moedas/ações: ")
print(function)
print("digite a url:")
url=input("")

def Captura_de_futuros_offshore(url):
    try:
        session = HTMLSession()
        
        resp = session.get(url)
        
        resp.html.render(sleep=1, keep_page=True)
        open_tags = resp.html.find(".js-symbol-open")

        open = [tag.text for tag in open_tags]
        open = open[0]

        last_tags = resp.html.find(".js-symbol-last")

        last = [tag.text for tag in last_tags]
        last = last[0]

        data_tags = resp.html.find(".tv-symbol-price-quote__data-mode")

        data_mode = [tag.text for tag in data_tags]
        data_mode = data_mode[0]

        currency_tags = resp.html.find(".js-symbol-currency")

        currency = [tag.text for tag in currency_tags]
        currency = currency[0]

        prev_tags = resp.html.find(".js-symbol-prev-close")

        prev = [tag.text for tag in prev_tags]
        prev = prev[0]

        volume_tags = resp.html.find(".js-symbol-volume")

        volume = [tag.text for tag in volume_tags]
        volume = volume[0]

        price_tags = resp.html.find(".js-symbol-change")

        price_change = [tag.text for tag in price_tags]
        price_change = price_change[0]

        price_tags2 = resp.html.find(".js-symbol-change-pt")

        price_quote = [tag.text for tag in price_tags2]
        price_quote = price_quote[0]
        
        name_tags = resp.html.find(".tv-symbol-header__first-line")

        name_active = [tag.text for tag in name_tags]
        name_active = name_active[0]
        
        market_status_tags = resp.html.find(".tv-symbol-price-quote__market-stat")

        market_status = [tag.text for tag in market_status_tags]
        market_status = market_status[0]
        
        
        print((' Paridade: {}\n Valor da quota: {}\n Tempo de atraso {}e aproximadamente: 10 minutos\n Moeda: {}\n Mudança no preço: {}\n Porcetagem de mudança: {}\n Valor anterior da paridade: {}\n Abertura da paridade: {}\n Volume: {}\n Estado do Mercado: {}'
            .format(name_active, last, data_mode, currency, price_change,price_quote,prev,open,volume, market_status)))
    except: 
        print("Error na função futuro offshore. Tentando novamente")
        Captura_de_futuros_offshore(url)
    


def Captura_de_moedas_offshore(url):
    try:
        
        session = HTMLSession()
        
        resp = session.get(url)
        
        resp.html.render(sleep=1, keep_page=True)
        
        eps_tags = resp.html.find(".js-symbol-eps")

        eps = [tag.text for tag in eps_tags]
        eps = eps[0]

        last_tags = resp.html.find(".js-symbol-last")

        last = [tag.text for tag in last_tags]
        last = last[0]

        market_cap_tags = resp.html.find(".js-symbol-market-cap")

        market_cap = [tag.text for tag in market_cap_tags]
        market_cap = market_cap[0]

        currency_tags = resp.html.find(".js-symbol-currency")

        currency = [tag.text for tag in currency_tags]
        currency = currency[0]

        next_earning_tags = resp.html.find(".js-symbol-next-earning")

        next_earning = [tag.text for tag in next_earning_tags]
        next_earning = next_earning[0]

        dividends_tags = resp.html.find(".js-symbol-dividends")

        dividends = [tag.text for tag in dividends_tags]
        dividends = dividends[0]

        price_tags = resp.html.find(".js-symbol-change")

        price_change = [tag.text for tag in price_tags]
        price_change = price_change[0]

        price_tags2 = resp.html.find(".js-symbol-change-pt")

        price_quote = [tag.text for tag in price_tags2]
        price_quote = price_quote[0]
        
        name_tags = resp.html.find(".tv-symbol-header__first-line")

        name_active = [tag.text for tag in name_tags]
        name_active = name_active[0]
        
        price_earnings_tags = resp.html.find(".js-symbol-pe")

        price_earnings = [tag.text for tag in price_earnings_tags]
        price_earnings = price_earnings[0]
        
        market_status_tags = resp.html.find(".tv-symbol-price-quote__market-stat")

        market_status = [tag.text for tag in market_status_tags]
        market_status = market_status[0]

        print(('\n Paridade: {}\n Valor da quota: {}\n Moeda: {}\n Mudança no preço: {}\n Porcetagem de mudança: {}\n Próximos ganhos: {}\n Lucro por ação: {}\n Capitalização de mercado: {}\n Rendimento Dividendo: {}\n Preço/Ganhos: {}\n Estado do mercado: {}'
            .format(name_active, last, currency,price_change, price_quote, next_earning, eps, market_cap, dividends, price_earnings, market_status)))
    except: 
        print("Error na função moeda offshore. Tentando novamente")
        Captura_de_moedas_offshore(url)
        
        
if int(function) == 1:
    Captura_de_futuros_offshore(url)
elif int(function) == 2:
    Captura_de_moedas_offshore(url)