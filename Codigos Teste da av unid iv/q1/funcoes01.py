import json, os
from codigos_http import *
from datetime import datetime

diretorio = os.path.dirname(__file__)

def moedaAno(ano:int, moeda:str) -> str:
    if not isinstance(ano, int):
        raise ValueError('Argumento \'ano\' deve ser do tipo INT')
    if not isinstance(moeda, str):
        raise ValueError('Argumento \'moeda\' deve ser do tipo STR')
    
    strURLCotacoes  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
    strURLCotacoes += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
    strURLCotacoes += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
    strURLCotacoes += f'@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&'
    strURLCotacoes += f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json'

    return strURLCotacoes

def calcMediasMensais(cotacao:dict) -> dict:
    if not isinstance(cotacao, dict):
        raise ValueError('Argumento \'cotacao\' deve ser do tipo DICT')
    
    lstMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    lstValueCotacao = [cot for cot in cotacao['value'] if cot['tipoBoletim'] == 'Fechamento']
    somaCompras = {}
    somaVendas = {}
    contMes = {}

    for valorCot in lstValueCotacao:
        data = datetime.strptime(valorCot['dataHoraCotacao'], '%Y-%m-%d %H:%M:%S.%f')
        mes = data.month

        if lstMeses[mes - 1] not in somaCompras:
            somaCompras[lstMeses[mes - 1]] = 0
            somaVendas[lstMeses[mes - 1]] = 0
            contMes[lstMeses[mes - 1]] = 0

        somaCompras[lstMeses[mes - 1]] += valorCot['cotacaoCompra']
        somaVendas[lstMeses[mes - 1]] += valorCot['cotacaoVenda']
        contMes[lstMeses[mes - 1]] += 1

    mediaMeses = {}
    # usando somaCompras aqui pois tem a mesma quantidade de itens que somaVendas
    for mes, somaCompra in somaCompras.items(): 
        mediaMeses[mes] = {
            'mediaCompra': round(somaCompra / contMes[mes], 3),
            'mediaVendas': round(somaVendas[mes] / contMes[mes], 3)
        }

    return mediaMeses       
    
def escreverJSONeCSV(ano:int, moeda:str, medias:dict) -> str:
    if not isinstance(ano, int):
        raise ValueError('Argumento \'ano\' deve ser do tipo INT')
    if not isinstance(moeda, str):
        raise ValueError('Argumento \'moeda\' deve ser do tipo STR')
    if not isinstance(medias, dict):
        raise ValueError('Argumento \'medias\' deve ser do tipo DICT')
    
    # json
    with open(f'{diretorio}\\medias_cotacoes_{moeda}_{ano}.json', 'w', encoding='utf-8') as arqJson:
        json.dump(medias, arqJson, ensure_ascii=False, indent=4)

    # csv
    mediasEscrita = open(f'{diretorio}\\medias_cotacoes_{moeda}_{ano}.csv', 'w', encoding='utf-8')
    
    lstMedias = [valores for valores in medias.items()]
    
    mediasEscrita.write('moeda;mes;mediaCompra;mediaVenda\n')
    for mes, valores in lstMedias:
        # lstTemporaria transforma cada chave dos meses e seus valores em lista
        lstTemporaria = [moeda, mes, valores['mediaCompra'], valores['mediaVendas']]
        linha = ';'.join(str(i) for i in lstTemporaria)
        mediasEscrita.write(f'{linha}\n')
    mediasEscrita.close()

    return f'{'-' * 50}\nArquivo \'medias_cotacoes_{moeda}_{ano}.json\' salvo com sucesso.\nArquivo \'medias_cotacoes_{moeda}_{ano}.csv\' salvo com sucesso.\n{'-' * 50}'