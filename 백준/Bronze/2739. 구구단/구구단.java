import java.util.Scanner;
public class Main {
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i = 1; i <10; i++) {
            int res = n * i ;
            System.out.println(n + " * " + i + " = " + res);
        }
    }
}