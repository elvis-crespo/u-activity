"""
    Pseudocódigo para mover todos los ceros al final de una lista de números
    Algoritmo MoverCerosAlFinal
    Definir lista Como Lista de Enteros
    Definir numero Como Entero
    Definir entrada Como Cadena
    Definir count Como Entero
    Definir i Como Entero

    // Crear una lista vacía
    lista <- Nuevo Lista de Enteros

    // Mensaje para el usuario
    Escribir "La lista de números debe tener al menos 7 números y como máximo 14"

    // Leer números del usuario
    count <- 0
    Mientras Verdadero Hacer
        count <- count + 1
        Escribir "Ingrese el número ", count, " (o escriba 'salir' para terminar): "
        Leer entrada

        Si entrada = "salir" Entonces
            Romper
        FinSi

        // Intentar convertir la entrada en un número entero
        Si EsNumero(entrada) = Verdadero Entonces
            numero <- ConvertirAEntero(entrada)
            lista.Agregar(numero)
        Sino
            Escribir "Por favor, ingrese solo enteros."
            lista.Limpiar() // Limpiar la lista en caso de error
            Romper
        FinSi
    FinMientras

    // Validar el tamaño de la lista
    Si lista.Longitud >= 7 Y lista.Longitud <= 14 Entonces
        Escribir "Lista de números: ", lista

        // Mover los ceros al final
        count <- 0
        Para i <- 0 Hasta lista.Longitud - 1 Hacer
            Si lista[i] <> 0 Entonces
                // Intercambiar los elementos
                numero <- lista[count]
                lista[count] <- lista[i]
                lista[i] <- numero
                count <- count + 1
            FinSi
        FinPara

        Escribir "Lista de números con ceros al final: ", lista
    Sino
        Escribir "La lista de números debe tener al menos 7 y como máximo 14 números."
    FinSi
FinAlgoritmo


    Paradigma de programación: Programación funcional, imperativa        
        -En este paradigma, defines explícitamente los pasos que el programa debe seguir para lograr un objetivo. 
         La función moveToEnd es un ejemplo de esto, ya que se ejecuta paso a paso para reorganizar los elementos 
         en la lista.  
           
    Método de implementación del lenguaje de programación utilizado: Python
        - Uso de la función `input()` para la entrada de datos del usuario.
        - Uso de una lista para almacenar y manipular la lista de números.
        - Función `moveToEnd()` para operaciones específicas como mover ceros al final de la lista.

"""

def moveToEnd(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[count], numbers[i] = numbers[i], numbers[count]
            count += 1


numbers = []
print("The list of numbers must have at least 7 numbers and at most 14")

while True:
    count = len(numbers) + 1
    input_str = input(f"Enter number {count}: ")

    if input_str.lower() == "salir":
        break

    try:
        number = int(input_str)
        numbers.append(number)
    except ValueError:
        print("Please enter only integers.")
        numbers.clear()
        continue

if 7 <= len(numbers) <= 14:
    print("List of numbers:", numbers)
    moveToEnd(numbers)
    print("List of numbers with trailing zeros:", numbers)
else:
    print("The list of numbers must have at least 7 and at most 14 numbers.")
