import requests
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
from datetime import datetime

baseUrl = 'https://www.kabum.com.br/produto/'

# Inserir aqui os código de produtos que será feita a pesquisa de preço
products =['85196', '85197', '85198', '95217']
currentDate = datetime.date(datetime.now())

wb = Workbook()
worksheet = wb.worksheets[0]

worksheet['A1'] = "test"

for p in products:
  soup = requests.get(baseUrl+p)
  document = bs(soup.text, "html.parser")

  print('-------------------------')
  _description = document.find_all(class_="titulo_det")
  description = _description[0].text
  price = document.find_all(class_="preco_desconto_avista-cm")

  if not price: 
    price = document.find_all(class_="preco_desconto")
    print(f'{p}, {description}, {price[0].strong.text}, {currentDate}')
  else:
    print(f'{p}, {description}, {price[0].text}, {currentDate}')

wb.save('./test.xlsx')