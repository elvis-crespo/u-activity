import java.util.Scanner;

public class App 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        int num1, num2, num3, num4;
        
        long startTime = System.currentTimeMillis();

        System.out.print("Ingrese cuatro números enteros separados por espacio: ");
        num1 = scanner.nextInt();
        num2 = scanner.nextInt();
        num3 = scanner.nextInt();
        num4 = scanner.nextInt();
        
        if ((num1 == num2 && num3 == num4) || (num1 == num3 && num2 == num4) || (num1 == num4 && num2 == num3)) {
            System.out.println("dos pares");
        } else {
            System.out.println("no dos pares");
        }
        scanner.close();

        long endTime = System.currentTimeMillis();
        
        long executionTime = endTime - startTime;
        System.out.println("\nTiempo de ejecución: " + executionTime + " ms");
    }
}
