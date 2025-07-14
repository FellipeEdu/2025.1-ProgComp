strTexto = '''"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
anim id est laborum."'''

strCaracteres = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~'''
chaveAleatoria = '%_AC1D=RA1N%_8'
strCriptografada = ''

print(f'Texto original:\n{strTexto}\n')

# criptografar com a primeira chave
indiceCripto = 0
for letra in range(len(strTexto)):
    if indiceCripto == len(chaveAleatoria): indiceCripto = 0
    strCriptografada += chaveAleatoria[indiceCripto]
    indiceCripto += 1

# criar alfabeto cifrado
strCriptografadaChaveada = ''
for letra in strTexto:
    letraTemporaria = strCaracteres.find(letra)
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria]

    strTemporaria = strAlfabeto[strCaracteres.find(letra)]
    strCriptografadaChaveada += strTemporaria

print(f'Texto criptografado:\n{strCriptografadaChaveada}\n')