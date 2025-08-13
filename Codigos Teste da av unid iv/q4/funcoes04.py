import sys, requests, json, os
from datetime import datetime

diretorio = os.path.dirname(__file__)

'''
API Key abaixo, obtida criando uma conta no site da API: https://home.openweathermap.org/users/sign_up
'''
API_KEY = '76b7682ab999cc218154b6340a6f1451'

def obterPrevisao(cidade:str, numDias = 1) -> list: # 1 por padrão (clima do 'dia atual')
    '''
    Obtém previsão do tempo a partir dos parâmetros 'cidade' e 'numDias' (número de dias) para previsões dos próximos dias. 
    É limitado a 5 dias devido função gratuita da API. Retorna uma lista com um único elemento do tipo dicionário contendo a previsão
    do tempo.
    '''
    urlPrevisao = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        print(f"{'-'*40}\nRequisitando dados da API...")
        dadosPrevisao = requests.get(urlPrevisao).json()
        lstPrevisoesIniciais = []
        lstPrevisoesSelec = []
        dicPrevisoes = {}

        for previsao in dadosPrevisao['list']:
            testeData = datetime.strptime(previsao['dt_txt'], '%Y-%m-%d %H:%M:%S')
            if testeData.hour == 12:
                lstPrevisoesIniciais.append(previsao)

        for dicPrevisao in lstPrevisoesIniciais[:numDias]: # Percorre cada dia
            try:               
                previsaoDia = dicPrevisao # [i*8] # Pega a primeira previsão do dia
            except requests.RequestException as erro:
                print(f"ERRO: Falha na requisição à API: {erro}")
                return []
            except KeyError as erro:
                print(f"ERRO: {erro}. Nome da cidade incorreto ou cidade inexistente.")
                return []
            dataPrevisao = previsaoDia['dt_txt']
            tempDia = previsaoDia['main']['temp']
            descricaoDia = previsaoDia['weather'][0]['description']
            umidadeAtual = previsaoDia['main']['humidity']
            icone = previsaoDia['weather'][0]['icon']

            dicPrevisoes = {
                'data_Previsao': dataPrevisao,
                'temperatura': tempDia,
                'descricao': descricaoDia,
                'umidade': umidadeAtual,
                'icone': f'https://openweathermap.org/img/wn/{icone}@2x.png'
            }   

            lstPrevisoesSelec.append(dicPrevisoes)

        return lstPrevisoesSelec
    
    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição de Previsão: {erro}")

def dadosPrevisoes(cidade:str, previsaoDiarias):
    '''
    Cria um dicionário completo para adicionar ao histórico,
    usando apenas 'previsaoDiarias' (dados das previsões retornadas) e 'cidade'.
    '''
    if cidade and previsaoDiarias:
        nova_consulta = {
            'data_hora': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'localizacao': cidade,
            'previsoes_selecionadas': previsaoDiarias # Salva a lista de previsões
        }
        return nova_consulta
    
    return None

def salvarHistorico(historico, nomeArq="historico.json"):
    '''
    Salva uma lista de históricos de consulta em um arquivo JSON. 
    Recebe uma lista 'histórico' como parâmetro e retorna o JSON.
    '''
    try:
        with open(f'{diretorio}\\{nomeArq}', 'w', encoding='utf-8') as arquivo:
            json.dump(historico, arquivo, indent=4, ensure_ascii=False)
        print(f"\nHistórico salvo com sucesso em '{nomeArq}'.")
    except IOError as erro:
        print(f"\nErro ao salvar o arquivo: {erro}.")

def lerHistorico(nomeArq="historico.json"):
    '''
    Lê o histórico de consultas de um arquivo JSON para que, posteriormente no programa, adicione um novo histórico.
    Retorna uma lista vazia se o arquivo não existir.
    '''
    try:
        with open(f'{diretorio}\\{nomeArq}', 'r', encoding='utf-8') as f:
            historico = json.load(f)
        print(f"Histórico de consultas carregado de '{nomeArq}'.")
        return historico
    except FileNotFoundError:
        print(f"Arquivo '{nomeArq}' não encontrado. Iniciando um novo histórico.")
        return []
    except json.JSONDecodeError as erro:
        print(f"Erro ao ler o arquivo JSON: {erro}. O arquivo pode estar corrompido.")
        return []