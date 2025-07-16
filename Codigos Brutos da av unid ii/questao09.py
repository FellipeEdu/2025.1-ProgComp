strTexto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
anim id est laborum."""

strCaracteres = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~'''
strCriptografada = ''
strCriptografadaChaveada = ''
strCriptografadaNova = ''
strCriptografadaChaveadaNova = ''
indiceCripto = 0 

print(f'Texto original:\n{strTexto}\n')

# criptografando a primeira chave
chaveCripto = ''
for letra in strTexto[-9:]: # ' laborum.'
    letraTemp = strCaracteres.find(letra) # ' '
    alfabetoTemp = strCaracteres[letraTemp:] + strCaracteres[:letraTemp]
    #print(f'{letraTemp:03d}; {alfabetoTemp}')
    chaveCripto += alfabetoTemp[strCaracteres.find(strCaracteres[letraTemp])]

#print(f'Texto criptografado com primeira chave:\n{strCriptografada}\n')'''
print(f'Primeira chave:\n{chaveCripto}\n')

# criar alfabeto cifrado
for letra in strTexto: # usando range(), pois strTexto e strCriptografada tem o mesmo tam
    if indiceCripto == len(chaveCripto): indiceCripto = 0
    letraTemporaria = strCaracteres.find(letra) # 'L'
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria] # 'LMNOPQR [...] EFGHIJK'
    # procura em strAlfabeto a letra do atual indiceCripto em chaveCripto
    # ex: strCriptografada = strAlfabeto[....find(Á)] = Ì
    strCriptografada += strAlfabeto[strCaracteres.find(chaveCripto[indiceCripto])]
    indiceCripto += 1
    if not strTexto: indiceCripto = 0

print(f'Texto criptografado 1:\n{strCriptografada}\n')

chaveNova = strCriptografada[-9:]
print(f'Segunda chave:\n{chaveNova}\n')

# criptografar com a segunda (nova) chave
for letra in strCriptografada:
    if indiceCripto == len(chaveNova): indiceCripto = 0
    letraTemp = strCaracteres.find(letra) # 'Ì'
    alfabetoTemp = strCaracteres[letraTemp:] + strCaracteres[:letraTemp]

    strCriptografadaNova += alfabetoTemp[strCaracteres.find(chaveNova[indiceCripto])]
    indiceCripto += 1
    if not strTexto: indiceCripto = 0

print(f'Texto criptografado com nova chave:\n{strCriptografadaNova}\n')