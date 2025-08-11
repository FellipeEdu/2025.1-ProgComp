from datetime import datetime
from funcoes02_v2 import *

ano_atual = datetime.now().year
while True:
    try:
        anoEscolhido = int(input(f"Informe o ano desejado [2021 a {ano_atual}]: "))
        if 2021 <= anoEscolhido <= ano_atual:
            break
        else:
            print(f"ERR0: informe um ano válido.")
    except ValueError:
        print('ERRO: Digite um número inteiro para o ano.')
    except Exception as e:
        print(f'ERR0: {e}')

ano, dicCartola = dados_cartola(anoEscolhido)

# exibir as escalações disponíveis do cartolaFC.
escalacoes = ['3-4-3', '3-5-2', '4-3-3', '4-4-2', '4-5-1', '5-3-2', '5-4-1']
print('Escolha uma das escalações disponíveis:')
for i, esc in enumerate(escalacoes, start=1):
    print(f'{i} - {esc}')

# solicitar a escalação desejada.
while True:
    try:
        escalacao = int(input('Defina uma escalação ( 1-7 ): '))
        if 1 <= escalacao <= 7:
            break
        else:
            print(f'ERR0: Escalação inválida.Escolha uma das opções: {escalacoes}')
    except ValueError:
        print('ERR0: Por favor, digite um número válido.')
    except Exception as e:
        print(f'ERR0: {e}')

quantidades_atletas = escolher_escalacao_e_quantidades(escalacao)

selecao_atletas, ordem = definir_selecao(dicCartola, quantidades_atletas)

salvar_exibir_selecao(selecao_atletas, ano, ordem)