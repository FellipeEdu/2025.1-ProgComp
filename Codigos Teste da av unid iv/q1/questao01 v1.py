import sys, requests; 
from datetime import datetime
from funcoes01 import *

strURLMoedas  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURLMoedas += '/Moedas?$top=100&$format=json'

try:    
    dicMoedas = requests.get(strURLMoedas).json()
except requests.RequestException as erro:
    sys.exit(f"ERR0: Falha na requisição à API: {erro}")

# listando moedas válidas
lstMoedas = [moeda['simbolo'] for moeda in dicMoedas['value']]

print('----- CONSULTA DE COTAÇÕES -----')
outraConsulta = None
while not outraConsulta == 'N':
    try:
        anoEscolhido = int(input('Digite o ano para consulta: '))
        while anoEscolhido > datetime.today().year or anoEscolhido < 1994:
            anoEscolhido = int(input('ERRO: Digite um ano válido\nDigite o ano: '))

        moedaEscolhida = input('Escolha uma das moedas abaixo (ex.: CAD)\n[AUD, CAD, CHF, DKK, EUR, GBP, JPY, NOK, SEK, USD]: ').upper()
        while not moedaEscolhida in lstMoedas:
            moedaEscolhida = input('ERRO: Escolha uma moeda válida.\nEscolha uma moeda: ').upper()

        nomeMoeda = [cot['nomeFormatado'] for cot in dicMoedas['value'] if cot['simbolo'] == f'{moedaEscolhida}']
        print(f'\nVocê escolheu {str(nomeMoeda[0]).title()}')

        reqHTTP = moedaAno(anoEscolhido, moedaEscolhida)

        try:
            dicCotacoes = requests.get(reqHTTP).json()
        except requests.RequestException as erro:
            sys.exit(f"\nERR0: Falha na requisição à API: {erro}")   
    except Exception as erro:
        sys.exit(f'\nERRO: {erro}')
    else:
        mediaMeses = calcMediasMensais(dicCotacoes)
        
        cotacaoCSV = escreverJSONeCSV( anoEscolhido, moedaEscolhida, mediaMeses)
        print(cotacaoCSV)

    outraConsulta = input('\nDeseja fazer outra consulta?\nSim [S] ou Não [N]: ').upper()
    while not (outraConsulta == 'S' or outraConsulta == 'N'):
        outraConsulta = input('\nERRO: digite um valor válido.\nDeseja visualizar de novo? ').upper()