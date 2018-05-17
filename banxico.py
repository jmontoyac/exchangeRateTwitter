import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import post_tweet

quote_page = ['http://www.banxico.org.mx/tipcamb/llenarTiposCambioAction.do?idioma=sp']
data = []
for pg in quote_page:
    page = urllib2.urlopen(pg)
    soup = BeautifulSoup(page, 'html.parser')
    price_box = soup.find('div', attrs={'id':'FIX_DATO'})
    price = price_box.text.strip()
    data.append((price))

with open('cambioDiario.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for price in data:
        writer.writerow([price, datetime.now()])

timestamp = datetime.now()
fecha_str = timestamp.strftime('%d %b %Y %H:%M:%S')
status_string = 'Tipo de cambio Peso/Dolar FIX: ' + price + '\n' + fecha_str + '\n***Fuente: www.banxico.org.mx'
print status_string

post_tweet.post(status_string)
