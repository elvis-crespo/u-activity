# Pseudocódigo:
'''
    Algoritmo SockMerchant
    Definir n Como Entero
    Definir ar Como Lista de Enteros
    Definir sockCount Como Diccionario
    Definir sock, count, pairs Como Entero

    // Función para eliminar espacios a la izquierda
    Funcion ltrim(s)
        Devolver Reemplazar(s, "^\\s+", "")
    FinFuncion

    // Función para eliminar espacios a la derecha
    Funcion rtrim(s)
        Devolver Reemplazar(s, "\\s+$", "")
    FinFuncion

    // Leer el tamaño de la lista
    Escribir "Ingresa el tamaño de la lista: "
    Leer n

    // Leer los elementos de la lista
    Escribir "Ingresa los elementos de la lista: "
    ar_temp <- LeerLinea()
    ar_temp <- ltrim(rtrim(ar_temp))
    ar <- ConvertirAEnteros(Separar(ar_temp, " "))

    // Inicializar el diccionario para contar los calcetines
    sockCount <- CrearDiccionario()
    pairs <- 0

    // Contar la cantidad de calcetines de cada color
    Para Cada sock En ar
        Si sockCount.Existe(sock) Entonces
            sockCount[sock] <- sockCount[sock] + 1
        Sino
            sockCount[sock] <- 1
        FinSi
    FinPara

    // Calcular el número de pares
    Para Cada count En sockCount.Valores
        pairs <- pairs + (count // 2)
    FinPara

    // Mostrar el resultado
    Escribir "El número de pares es ", pairs

FinAlgoritmo

'''

# Paradigma de programación: Programación funcional e imperativa
# Método de implementación: Función definida por el usuario
# Tipo de traductor: Intérprete

# Cómandos para ejecutar:
# python App.py

''' Código fuente en Python '''

def ltrim(s):
    return s.lstrip()

def rtrim(s):
    return s.rstrip()

def sockMerchant(n,ar):
    sock_count = {}
    pairs = 0

    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    for count in sock_count.values():
        pairs += count // 2

    return pairs


print("Ingresa el tamanio de la lista: ", end="")
n = int(ltrim(rtrim(input().strip())))

print("Ingresa los elementos de la lista: ", end="")
ar_temp = ltrim(rtrim(input().strip())).split()
ar = [int(item) for item in ar_temp]

result = sockMerchant(n, ar)

print("\nEl número de pares es", result)
