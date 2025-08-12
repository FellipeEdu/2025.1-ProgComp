import sys, requests, json, os
from datetime import datetime

diretorio = os.path.dirname(__file__)

API_KEY = '76b7682ab999cc218154b6340a6f1451'

'''def previsaoClimaAtual(cidade:str):
    urlClimaAtual = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},br&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        print('\nRequisitando dados da API...')
        try:
            dadosAtuais = requests.get(urlClimaAtual).json()
        except requests.RequestException as erro:
            sys.exit(f"ERR0: Falha na requisição à API: {erro}")

        tempAtual = dadosAtuais['main']['temp']
        descricaoAtual = dadosAtuais['weather'][0]['description']
        umidadeAtual = dadosAtuais['main']['humidity']

        print("\n---------- Clima Atual ----------")
        print(f"Local: {dadosAtuais['name']}, {dadosAtuais['sys']['country']}")
        print(f"Clima: {descricaoAtual.capitalize()}")
        print(f"Temperatura: {tempAtual}°C")
        print(f"Umidade: {umidadeAtual}%")
        print("-" * 25)

    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição de Clima Atual: {erro}")
    
    return dadosAtuais'''

def obterPrevisao(cidade:str, numDias = 1): # 1 por padrão (clima do 'dia atual')
    urlPrevisao = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    try:
        print(f"{'-'*40}\nRequisitando dados da API...")
        try:
            dadosPrevisao = requests.get(urlPrevisao).json()
        except requests.RequestException as erro:
            sys.exit(f"ERRO: Falha na requisição à API: {erro}")
        except json.JSONDecodeError as erro:
            print(f"ERRO ao ler o arquivo JSON: {erro}. Provavelmente a cidade não existe, ou o nome inserido não é uma cidade.")
            return []

        lstPrevisoesSelec = []
        for i in range(numDias + 1): # Pega os próximos dias (ex: 1 + 1 = range 2, vai pegar a previsão até i = 1, que é amanhã)            
            previsaoDia = dadosPrevisao['list'][i+8] # Pega a primeira previsão do dia
            dataPrevisao = previsaoDia['dt_txt']
            tempDia = previsaoDia['main']['temp']
            descricaoDia = previsaoDia['weather'][0]['description']
            umidadeAtual = previsaoDia['main']['humidity']

            dicPrevisoes = {
                'data_Previsao': dataPrevisao,
                'temperatura': tempDia,
                'descricao': descricaoDia,
                'umidade': umidadeAtual
            }   
            '''print(f"Data: {datetime.fromtimestamp(dataPrevisao).strftime('%d/%m')}")
            print(f"  Descrição: {descricaoDia.capitalize()}")
            print(f"  Temperatura: {tempDia}°C")
            print(f"Umidade: {umidadeAtual}%")'''
            lstPrevisoesSelec.append(dicPrevisoes)

        return lstPrevisoesSelec
    
    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição de Previsão: {erro}")


#def dadosPrevisoes(previsaoAtual, previsaoDias):
def dadosPrevisoes(cidade:str, previsaoDiarias):
    '''
    Cria um dicionário completo para uma consulta de histórico,
    usando apenas os dados da previsão.
    '''
    if cidade and previsaoDiarias:
        nova_consulta = {
            # COMO CONVERTER UM datetime.now() em string
            'data_hora': datetime.now().strptime('%d/%m/%Y %H:%M:%S'), # datetime.fromtimestamp(previsaoDiarias[0]['data_Previsao']).strftime('%d/%m/%Y %H:%M:%S')
            'localizacao': cidade,
            'previsoes_selecionadas': previsaoDiarias # Salva a lista de previsões
        }
        return nova_consulta
    
    return None

def salvarHistorico(historico, nomeArq="historico.json"):
    '''
    Salva uma lista de históricos de consulta em um arquivo JSON.
    '''
    try:
        with open(f'{diretorio}\\{nomeArq}', 'w', encoding='utf-8') as arquivo:
            json.dump(historico, arquivo, indent=4, ensure_ascii=False)
        print(f"\nHistórico salvo com sucesso em '{nomeArq}'.")
    except IOError as erro:
        print(f"\nErro ao salvar o arquivo: {erro}.")

def lerHistorico(nomeArq="historico.json"):
    '''
    Lê o histórico de consultas de um arquivo JSON.
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