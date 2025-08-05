def mdc(numA:int, numB:int) -> int:
    if not isinstance(numA, int):
        raise ValueError ('argumento \'numA\' deve ser do tipo INT.')
    if not isinstance(numB, int):
        raise ValueError ('argumento \'numB\' deve ser do tipo INT.')

    if numA < numB:
        raise Exception ("'numA' deve ser maior que 'numB'.")

    dividendo = numB
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

        return resto_divisor