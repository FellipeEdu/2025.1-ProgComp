import sys

angA = int(input('Digite o angulo A: '))
angB = int(input('Digite o angulo B: '))
angC = int(input('Digite o angulo C: '))

soma = int(angA + angB + angC)

if soma < 180 or soma > 180:
    sys.exit('digite valores compativeis com um triangulo')
elif angA == 90 or angB == 90 or angC == 90:    
    print('Triangulo Retangulo.')
elif angA >= 90 or angB >= 90 or angC >= 90:
    print('Obtusângulo.')
elif angA <= 90 or angB <= 90 or angC <= 90:
    print('Acutângulo.')