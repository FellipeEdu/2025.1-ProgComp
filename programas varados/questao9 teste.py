strTexto = '''"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
anim id est laborum."'''

strCaracteres = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~'''
chaveAleatoria = '%_AC1D=RA1N%_8'
strCriptografada = ''

print(f'Texto original:\n{strTexto}\n')

indiceCripto = 0
for letra in range(len(strTexto)):
    if indiceCripto == len(strCaracteres) - 1: indiceCripto = 0
    strCriptografada += strCaracteres[indiceCripto]
    indiceCripto += 1

# criando alfabeto cifrado e criptografando
strCriptografadaChaveada = ''
for letra in strTexto:
    #letraTemporaria = strCaracteres.find(letra)
    letraTemporaria = strCriptografada.find(letra) 
    strAlfabeto = strCaracteres[letraTemporaria:] + strCaracteres[:letraTemporaria]

    segLetraTemporaria = strAlfabeto[strCaracteres.find(letra)]
    strCriptografadaChaveada += segLetraTemporaria

print(f'Texto criptografado:\n{strCriptografadaChaveada}\n')