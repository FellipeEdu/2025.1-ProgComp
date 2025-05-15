import sys

angA = int(input('Digite o angulo A: '))
angB = int(input('Digite o angulo B: '))
angC = int(input('Digite o angulo C: '))

soma = int(angA + angB + angC)
if angA <= 0 or angB <= 0 or angC <= 0:
    sys.exit('ERRO: um ou mais angulos não sao positivos')
if soma < 180 or soma > 180:
    sys.exit('ERRO: digite valores compativeis com um triangulo, a soma deve ser igual a 180')
elif angA == 90 or angB == 90 or angC == 90:    
    print('Triangulo Retangulo.')
elif angA >= 90 or angB >= 90 or angC >= 90:
    print('Obtusângulo.')
elif angA <= 90 or angB <= 90 or angC <= 90:
    print('Acutângulo.')