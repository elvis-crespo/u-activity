package actividad2.FrequencyCharacter;

public class Frequency {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        String str = "This website is awesome.";
        char ch = 'e';
        int frequency = 0;

        for(int i = 0; i < str.length(); i++) {
            if(ch == str.charAt(i)) {
                ++frequency;
            }
        }

        System.out.println("Frequency of " + ch + " = " + frequency);
    
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        
        System.out.println("\nTiempo de ejecución: " + executionTime + " ms");
    }
}
