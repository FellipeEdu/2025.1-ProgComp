lstNomes = list()

strNome = ''

while True:
    strNome = input('Digite um nome: ').strip()

    if strNome.lower() == 'fim': 
        break

    if len(strNome) > 0:
        lstNomes.append(strNome)

print(lstNomes)