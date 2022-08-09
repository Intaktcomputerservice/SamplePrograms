// Dies ist eine der einfachsten Java-Implementierungen für den Primzahltest

public class Primzahltest {
    public static void main(String[] args) {
        int checkNumber = 0;
        try {
            checkNumber = Integer.parseInt(args[0]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("You have to pass one number as argument!");
        } catch (NumberFormatException e) {
            System.out.println("Your argument must be an integer value!");
        }

        if (checkNumber < 0) checkNumber /= -1;
        if (checkNumber <= 1) {
            System.out.println("Your number is not a prime number!");
            System.exit(0);
        }
        
        for (int i = 2; i * i <= checkNumber + 1; i++)
            if (checkNumber % i == 0) {
                System.out.println("Your number is not a prime number!");
                System.exit(0);
            }

        System.out.println("Your number is a prime number!");
    }
}