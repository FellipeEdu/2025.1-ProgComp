from datetime import datetime
from funcoes02 import *

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

escalacao, quantidades_atletas = escolher_escalacao_e_quantidades()

selecao_atletas, ordem = definir_selecao(dicCartola, quantidades_atletas)

salvar_exibir_selecao(selecao_atletas, ano, ordem)