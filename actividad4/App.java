// Pseudocódigo:
/*
 Algoritmo SockMerchant
    Definir n Como Entero
    Definir ar Como Lista de Enteros
    Definir sockCount Como Diccionario
    Definir i, sock, count, pairs Como Entero

    // Leer el tamaño de la lista
    Escribir "Ingresa el tamaño de la lista: "
    Leer n

    // Leer los elementos de la lista
    Escribir "Ingresa los elementos de la lista: "
    ar <- LeerListaEnteros(n)

    // Inicializar el diccionario para contar los calcetines
    sockCount <- CrearDiccionario()

    // Contar la cantidad de calcetines de cada color
    Para i <- 1 Hasta n
        sock <- ar[i]
        Si sockCount.Existe(sock) Entonces
            sockCount[sock] <- sockCount[sock] + 1
        Sino
            sockCount[sock] <- 1
        FinSi
    FinPara

    // Calcular el número de pares
    pairs <- 0
    Para Cada count En sockCount.Valores
        pairs <- pairs + (count // 2)
    FinPara

    // Mostrar el resultado
    Escribir "El número de pares es ", pairs

FinAlgoritmo
 
 */

// Paradigma de programación: Programación funcional e imperativa
// Método de implementación: Utiliza clases y métodos estáticos
// Tipo de traductor: Compilador

// Cómandos para ejecutar:
// javac App.java
// java App

/* Código fuente en Java */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el tamanio de la lista: ");
        int n = Integer.parseInt(ltrim(rtrim(scanner.nextLine())));

        System.out.print("Ingresa los elementos de la lista: ");
        String[] arTemp = ltrim(rtrim(scanner.nextLine())).split(" ");
        List<Integer> ar = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arTemp[i]);
            ar.add(arItem);
        }

        int result = sockMerchant(n, ar);

        System.out.println("\nEl número de pares es " + result);

        scanner.close();
    }

    public static int sockMerchant(int n, List<Integer> ar) {
        Map<Integer, Integer> sockCount = new HashMap<>();
        int pairs = 0;

        for (int i = 0; i < n; i++) {
            int sock = ar.get(i);
            sockCount.put(sock, sockCount.getOrDefault(sock, 0) + 1);
        }

        for (int count : sockCount.values()) {
            pairs += count / 2;
        }

        return pairs;
    }

    public static String ltrim(String str) {
        return str.replaceAll("^\\s+", "");
    }

    public static String rtrim(String str) {
        return str.replaceAll("\\s+$", "");
    }
}
