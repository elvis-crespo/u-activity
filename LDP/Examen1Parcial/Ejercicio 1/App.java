import java.util.Scanner;

public class App 
{
    public static void main(String[] args) 
    {
        long startTime = System.currentTimeMillis();
        
        Scanner scanner = new Scanner(System.in);
        double cantGastada, valueDesc;
        double porcentajeCupon = 0.0;
        String valueDescFormatted;

        System.out.print("Please enter the cost of your groceries: ");
        cantGastada = scanner.nextDouble();
        
        if (cantGastada > 9 && cantGastada < 60) {
            porcentajeCupon = 8.0;
        }else if (cantGastada > 59 && cantGastada < 150) {
            porcentajeCupon = 10.0;
        } else if (cantGastada > 149 && cantGastada < 210) {
            porcentajeCupon = 12.0;
        } else if (cantGastada > 209) {
            porcentajeCupon = 14.0;
        }
        
        valueDesc = desc(cantGastada, porcentajeCupon);
        valueDescFormatted = String.format("%.2f", valueDesc);

        System.out.println("You win a discount coupon of: $ " + valueDescFormatted + 
            " (" + porcentajeCupon + "% of your purchase.)");
        scanner.close();

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;

        System.out.println("\nTiempo de ejecución: " + executionTime + " ms");

    }

    public static double desc(double cantGastada, double porcentajeCupon)
    {
        return (porcentajeCupon / 100) * cantGastada;
    }
}
