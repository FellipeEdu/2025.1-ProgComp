'''
- Pesquisa e documentação:
- Informe o nome da API escolhida: https://openweathermap.org/
- Explique o que a API fornece (quais dados ou serviços): A API retorna previsão do tempo para até 5 dias.
- Indique a documentação consultada (link oficial ou repositório): https://openweathermap.org/forecast5

Descreva o objetivo do seu programa: o que ele fará utilizando essa API:

* O usuário poderá verificar a previsão do tempo para qualquer cidade no mundo (digitando o nome em português) (por ex: Natal), especificando com um 
código de país se preferir (ex: Londres GB; veja uma lista de códigos de países no link a seguir, selecionando a opção 'Country Codes'
no menu lateral à esquerda: https://www.iso.org/obp/ui/#search).

* Salvar e Carregar histórico de cada consulta realizada.
'''

import sys, locale; 
from datetime import datetime
from funcoes04 import *

locale.setlocale(locale.LC_ALL, '')

print(f"{'-' * 20} PREVISÃO DO TEMPO {'-' * 20}")

while True:
    historicoConsultas = lerHistorico()
    resultadoPrevisao = None

    # menu
    print("1. Fazer uma nova consulta de previsão do tempo")
    print("2. Ver o histórico de consultas")
    print("3. Sair do programa")
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        while True:
            try:
                cidade = input(f'\n{'*'*60}\nDigite o nome de uma cidade (ex.: Macaiba): ')
                numDias = int(input('\nConsultar Previsão de Hoje (1) a até (5) Dias\nEscolha de 1 a 5 dias: '))

                if 1 <= numDias <= 5: break
                else: print(f"ERRO: informe opção válida.")
            except ValueError:
                sys.exit('ERRO: digite um valor válido.')
            except Exception as erro:
                sys.exit(f'\nERRO: {erro}')

        resultadoPrevisao = obterPrevisao(cidade, numDias)
        print(f"\nPrevisão para Hoje e para o(s) Próximo(s) {numDias} Dia(s):\n{'-'*60}")
        for previsao in resultadoPrevisao:
            print(f"Data: {datetime.strptime(previsao['data_Previsao'], '%Y-%m-%d %H:%M:%S').strftime('%A, %d/%m')}")
            print(f"Temperatura: {previsao['temperatura']:.1f}°C")
            print(f"Descrição: {previsao['descricao'].capitalize()} | {previsao['icone']}")
            print(f"Umidade: {previsao['umidade']}%\n{'-'*60}")

        # salvando no histórico
        historicoConsultas.append(dadosPrevisoes(cidade, resultadoPrevisao))  
        salvarHistorico(historicoConsultas)
    elif opcao == 2:
        print(f'\nExibindo Histórico...\n{'*'*150}')
        for historico in historicoConsultas:
            # print(f'{historico}\n{'-'*150}')
            print(f'Horário da Consulta: {historico['data_hora']}')
            print(f'Localidade: {historico['localizacao'].capitalize()}')
            print(f'Previsões Selecionadas:\n{'*'*100}')
            for previsao in historico['previsoes_selecionadas']:
                print(f"Data: {datetime.strptime(previsao['data_Previsao'], '%Y-%m-%d %H:%M:%S').strftime('%A, %d/%m')}")
                print(f"Temperatura: {previsao['temperatura']:.1f}°C")
                print(f"Descrição: {previsao['descricao'].capitalize()} | {previsao['icone']}")
                print(f"Umidade: {previsao['umidade']}%\n{'-'*60}")
        print(f'Fim da Exibição do Histórico.\n{'*'*150}')        
    else:
        break