def suma_pares(arr= [], k = 0):

    pares = ()
    lista_pares = []

    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[i] + arr[j+1] == k:
                pares = (arr[i], arr[j+1])
                lista_pares.append(pares)
            else:
                cambio = arr[j + 1]
                arr[j + 1] = cambio   
        
    return len(lista_pares)


print(suma_pares([-1, 1, -2, 2, 0], 0))
print(suma_pares([-1, 1, -2, 2, 0], 1))
print(suma_pares([-2, 2, 0, 0], -2))
print(suma_pares([-1, 1, -2, 2, 0], 10))
print(suma_pares([], 10))
