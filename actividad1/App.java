import java.util.ArrayList;
import java.util.Scanner;

/**
 * Pseudocódigo para mover todos los ceros al final de una lista de números
 * Algoritmo MoverCerosAlFinal
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

 */

 /*
Paradigma de programación: Programación funcional, imperativa        
    - En este paradigma, defines explícitamente los pasos que el programa debe seguir para lograr un objetivo. 
    La función moveToEnd es un ejemplo de esto, ya que se ejecuta paso a paso para reorganizar los elementos 
    en la lista. 

Método de implementación del lenguaje de programación utilizado: Java
  - Uso de la clase 'Scanner' para la entrada de datos del usuario.
  - Uso de 'ArrayList' para almacenar y manipular la lista de números.
  - Métodos estáticos para operaciones específicas como 'moverZerosAlFinal'.
 */
public class App {

    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        int count = 0;

        System.out.println("The list of numbers must have at least 7 numbers and at most 14");

        while (true) 
        {
            // Increment the count
            count++;
            // Prompt the user to enter a number
            System.out.print("Enter numbers " + count + ": ");
            String input = scanner.nextLine();
            
            // Check if the user wants to exit the loop
            if (input.equalsIgnoreCase("salir")) 
            {
                break;
            }
            
            try {
                // Try to parse the input as an integer and add it to the ArrayList
                numbers.add(Integer.parseInt(input));
            } catch (NumberFormatException e) {
                // If the input is not a valid integer, print an error message and clear the ArrayList
                System.out.println("Please enter only integers.");
                numbers.clear();
                break;
            }
        }
            
       

        // Close the scanner
        scanner.close();

        // Validate the range of integers entered
        if (numbers.size() > 6 && numbers.size() < 15) 
        {
            // If the number of inputs is within the range, print the list of numbers and move zeros to the end
            System.out.println("List of numbers: " + numbers);
            moveToEnd(numbers);
            System.out.print("List of numbers with trailing zeros: " + numbers + "");
        } else {
            // If the number of inputs is not within the range, print an error message
            System.out.println("The list of numbers must have at least 7 and at most 14 numbers.");
        }
    }

    public static void moveToEnd(ArrayList<Integer> numbers) 
    {
        int count = 0;
        for (int i = 0; i < numbers.size(); i++) 
        {
            if (numbers.get(i) != 0) 
            {
                int temp = numbers.get(count);
                numbers.set(count, numbers.get(i));
                numbers.set(i, temp);
                count++;
            }
        }
    }


    // public static void list(int[] numbers) {
    //     int count = 0;
    //     for (int i = 0; i < numbers.length; i++) {
    //         if (numbers[i] != 0) {
    //             int temp = numbers[count];
    //             numbers[count] = numbers[i];
    //             numbers[i] = temp;
    //             count++;
    //         }
    //     }
    // }
}