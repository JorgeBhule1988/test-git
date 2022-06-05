# Escribe un programa con recursión que te permita calcular la secuencia de números que se generan 
# en una serie empezando con un número dado por el usuario. La serie se crea con las siguientes 2 reglas:
 
#            Regla 1: Si el número es par: dividir ese número entre 2
#            Regla 2: Si el número es impar: multiplicar ese número por 3 y sumar un 1
           
#            El último número en la serie creada es el 1.
 
 
#Por ejemplo: Si el número dado por el usuario es 5 entonces, el siguiente número en la serie se obtiene 
#ocupando la regla de impar -porque 5 es impar-, por lo que el siguiente elemento es 16. 
#Debido a que 16 es par, el siguiente elemento se obtiene al aplicar la regla 1, lo que genera el número 8. 
#Debido a que 8 es par, el siguiente elemento se obtiene al aplicar la regla 1, lo que genera el número 4. 
#Debido a que 4 es par, el siguiente elemento se obtiene al aplicar la regla 1, lo que genera el número 2. 
#Debido a que 2 es par, el siguiente elemento se obtiene al aplicar la regla 1, lo que genera el número 1. 
#Debido a que ya llegamos al número 1, hemos terminado de calcular la serie, por lo que regresamos la serie generada: 5, 16, 8, 4, 2, 1.

def parimpar(n):
 
    if n == 2:
        n = 1
        return n
    elif n % 2 == 0:
        n = n // 2
        print(n)
        return parimpar(n)
    else:
        n = (n * 3) + 1
        print(n)
        return parimpar(n)


if __name__ == '__main__':
    a = int(input('Dame un numero: '))
    print(a)
    print(parimpar(a))
