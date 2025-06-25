'''
Fazer um programa que solicite ao usuario nomes de pessoas.

O programa deverá parar de solicitar nomes quando o usuário digitar 'FIM'

No final o programa deverá listar os nomes informados em ordem alfabetica.
'''

lstNomes = list()

while True:
    strNome = input('Digite um nome: ').strip()

    if strNome.lower() == 'fim': 
        break

    if len(strNome) > 0:
        lstNomes.append(strNome)

#lstNomes.sort()
lstNomesOrdenados = sorted(lstNomes) # reverse = True

print(lstNomes)
print(lstNomesOrdenados)