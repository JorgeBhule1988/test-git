from re import sub

def parentesis_coherentes(cadena=''):
    
    #balanceado = True # Pues por default la cadena vacia esta balanceada
    cadena = sub(r'[^\[\]\(\)\{\}]','', cadena)
    pila = []
    parentesis = {'{': '}', '[': ']', '(': ')'}

    for texto in cadena:
        if texto in parentesis:
            pila.append(texto)
        elif len(pila) == 0 or texto != parentesis[pila.pop()]:
            return False
    return len(pila) == 0


#print(parentesis_coherentes('[]'))


def respuesta_pares(arr=''):
    stack = []
    numeros = ['1', '0']
 

    for i in arr:
        if i in numeros:
            stack.append(i)

    for i in range(len(stack)-1, 0, -1):
        if stack[i] in stack[i-1]:
            stack.pop(i)
            stack.pop(i-1)
    
  # Condicion final
    if len(stack) > 0:
        return ''.join(stack)
    else:
        return 'Helado es el vacio'

print(respuesta_pares('1001'))
print(respuesta_pares('1'))
print(respuesta_pares(''))
print(respuesta_pares('101'))
print(respuesta_pares('11'))
print(respuesta_pares('10001'))
