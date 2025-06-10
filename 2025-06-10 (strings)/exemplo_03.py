strTexto = input('Digite um texto: ')

strVogais = 'AEIOUÂÊÎÔÛÁÉÍÓÚÀÈÌÒÙÄËÏÖÜ'
intVogais = 0

for strLetra in strTexto:
    if strLetra == 'a' or strLetra == 'e' or strLetra == 'i' or strLetra == 'o' or strLetra == 'u':
