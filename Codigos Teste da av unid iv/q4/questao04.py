import sys, locale; 
from datetime import datetime
from funcoes04 import *

locale.setlocale(locale.LC_ALL, '')

print(f"{'-' * 20} PREVISÃO DO TEMPO {'-' * 20}")
outraConsulta = None
while not outraConsulta == 'N':
    historicoConsultas = lerHistorico()
    #resultadoAtual = None
    resultado = None

    while True:
        try:
            cidade = input('\nDigite o nome de uma cidade (ex.: Macaiba): ')
            numDias = int(input('\nConsultar Previsão de Hoje (1) a até (5) Dias\nEscolha de 1 a 4 dias: '))
            if 1 <= numDias <= 5: break
            else: print(f"ERRO: informe opção válida.")
        except ValueError:
            sys.exit('ERRO: digite um valor válido.')
        except Exception as erro:
            sys.exit(f'\nERRO: {erro}')
    #previsaoClimaDias(cidade, opcao)  
    #resultadoAtual = previsaoClimaAtual(cidade)
    resultado = obterPrevisao(cidade, numDias)
    print(f"\nPrevisão para Hoje e para o(s) Próximo(s) {numDias} Dia(s):\n{'-'*40}")
    for previsao in resultado:
        print(f"Data: {previsao['data_Previsao']}") # {datetime.fromtimestamp(previsao['data_Previsao']).strftime('%A, %d/%m')}
        print(f"Temperatura: {previsao['temperatura']:.1f}°C")
        print(f"Descrição: {previsao['descricao'].capitalize()}")
        print(f"Umidade: {previsao['umidade']}%\n{'-'*40}")
    # salvando no histórico
    historicoConsultas.append(dadosPrevisoes(cidade, resultado))
    salvarHistorico(historicoConsultas)

    outraConsulta = input('\nDeseja fazer outra consulta?\nSim [S] ou Não [N]: ').upper()
    while not (outraConsulta == 'S' or outraConsulta == 'N'):
        outraConsulta = input('\nERRO: digite um valor válido.\nDeseja visualizar de novo? ').upper()