# Escribe un programa con recursión que te permita calcular la suma 
# de los números naturales menores a 1000 (estrictamente) que sean múltiplos de 3 o 5.
       

def multiplos(numero, n):

    multiplo = int((n - 1) / numero)
    calculo = int(numero * (multiplo * (multiplo + 1)) / 2)
    return calculo


def multiplos_3_5(n):
    return multiplos(3, n) + multiplos(5, n)


print(multiplos_3_5(1000))
