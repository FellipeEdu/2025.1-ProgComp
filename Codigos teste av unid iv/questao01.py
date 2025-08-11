import requests; from datetime import datetime

strURLMoedas  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURLMoedas += '/Moedas?$top=100&$format=json'

dicMoedas = requests.get(strURLMoedas).json()

strURLCotacoes  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURLCotacoes += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURLCotacoes += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURLCotacoes += '@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&'
strURLCotacoes += '@dataFinalCotacao=%2712-31-2023%27&$format=json'

dicCotacoes = requests.get(strURLCotacoes).json()
print(dicCotacoes)