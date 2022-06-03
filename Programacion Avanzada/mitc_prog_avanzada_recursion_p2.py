# Escribe un programa con recursión que te permita calcular la diferencia entre la suma 
# de los primeros 100 números naturales al cuadrado y la suma de los cuadrados de los primeros 100 números naturales.

def cuadrado(n):

    if n == 1:
        return 1
    else:
        return n + cuadrado(n - 1)


def cuadrado2(n):
    
    return cuadrado(n) * cuadrado(n)


def cuadradosuma(n):
    
    if n == 1:
        return 1
    else:
        return (n * n) + cuadradosuma(n - 1)


def resultadofinal(n):

    return cuadrado2(n) - cuadradosuma(n)


print(resultadofinal(100))
