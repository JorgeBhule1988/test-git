def revertir(string=str(), a=int):
    
    if 0 == a:
        palabra = string[a]
    else:
        palabra = string[a] + revertir(string, a -1) 
        
    
    return palabra

string = 'Hola Mundo'
string = 'Hello World'
print(revertir(string, 9))
print(revertir(string, 10))
