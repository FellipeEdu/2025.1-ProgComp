strTexto = '''"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
anim id est laborum."'''

strCaracteres = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~'''
chaveAleatoria = '%_AC1D=RA1N%_8'
strCriptografada = ''
strCriptografadaChaveada = ''
strCriptografadaNova = ''
strCriptografadaChaveadaNova = ''
indiceCripto = 0 

print(f'Texto original:\n{strTexto}\n')

# criptografar com a primeira chave
for letra in range(len(strTexto)):
    if indiceCripto == len(chaveAleatoria): indiceCripto = 0
    strCriptografada += chaveAleatoria[indiceCripto]
    indiceCripto += 1
    if letra + 1 == len(strTexto): indiceCripto = 0

print(f'Texto criptografado com primeira chave:\n{strCriptografada}\n')

# criar alfabeto cifrado
for letra in range(len(strTexto)): # usando range(), pois strTexto e strCriptografada tem o mesmo tam
    letraTemporaria = strCaracteres.find(strTexto[letra])
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria]

    strTemporaria = strAlfabeto[strCaracteres.find(strCriptografada[letra])]
    strCriptografadaChaveada += strTemporaria

chaveNova = strCriptografadaChaveada[-9:]

print(f'Texto criptografado 1:\n{strCriptografadaChaveada}\n')

# criptografar com a segunda (nova) chave
for letra in range(len(strCriptografadaChaveada)):
    if indiceCripto == len(chaveNova): indiceCripto = 0
    strCriptografadaNova += chaveNova[indiceCripto]
    indiceCripto += 1
    if letra + 1 == len(strCriptografadaChaveada): indiceCripto = 0

print(f'Texto criptografado com nova chave:\n{strCriptografadaNova}\n')

# usando a chave nova em strTexto
for letra in range(len(strTexto)):
    letraTemporaria = strCaracteres.find(strTexto[letra])
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria]

    strTemporaria = strAlfabeto[strCaracteres.find(strCriptografadaNova[letra])]
    strCriptografadaChaveadaNova += strTemporaria

print(f'Criptografia com Nova chave:\n{strCriptografadaChaveadaNova}\n')