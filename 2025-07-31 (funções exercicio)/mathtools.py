def mdc(numA:int, numB:int) -> int:
    if not isinstance(numA, int):
        raise ValueError ('argumento \'numA\' deve ser do tipo INT.')
    if not isinstance(numB, int):
        raise ValueError ('argumento \'numB\' deve ser do tipo INT.')

    if numA < numB:
        raise Exception ("'numA' deve ser maior que 'numB'.")

    while numB != 0:
        resto = numA % numB
        numA = numB
        numB = resto

    # retorna numA pois na ultima divisão numA recebe numB, que é o resto de acordo com o algoritmo
    return numA

    '''dividendo = numB
    resto_divisor = numA % numB
    resto_final = resto_divisor

    if resto_divisor == 0: 
        #return f'MDC de {numA} e {numB} = {numB}.'
        return numB
    else:
        while resto_final == 0:
            resto_final = dividendo % resto_divisor # 210 % 60 = 30 | 60 % 30 = 0
            dividendo = resto_divisor # div = 60
            resto_divisor = resto_final # resto_div = 30 

        return resto_divisor'''
    
def fatorial(num:int) -> int:
    if not isinstance(num, int):
        raise ValueError ('argumento \'num\' deve ser do tipo INT.')
    
    if num < 0:
        raise Exception ('\'num\' deve ser positivo.')