'''
Fazer umporgrama que solicite ao usuario nomes de pessoas.

O programa deverá parar de solicitar nomes quando o usuário digitar 'FIM'

No final o programa deverá listar os nomes informados.
'''

lstNomes = list()

while True:
    strNome = input('Digite um nome: ').strip()

    if strNome.lower() == 'fim': 
        break

    if len(strNome) > 0:
        lstNomes.append(strNome)

print(lstNomes)