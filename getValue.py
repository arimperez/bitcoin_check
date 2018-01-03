import locale
import requests
from bs4 import BeautifulSoup
import re

def getValue(value):

    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
    page = requests.get("https://finance.google.com/finance?q=currency:btc") # ("https://www.coindesk.com/price/")

    soup = BeautifulSoup(page.content, "html.parser")


    data = soup.find_all(class_ = "bld")[0].get_text()
    #perCoin = #soup.find("price", attrs = {'valued-in': 'CAD'})
    #soup.select_one('price.ng-binding ng-isolate-scope')#.get_text()
    getCoin = data.split(" ")

    perCoin = float(locale.atof(getCoin[0]))* value
    return("$"+str(perCoin)+" USD")
