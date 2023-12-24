import java.util.Scanner;

public class Main {
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int n = scanner.nextInt();
        int res = 0;
        for(int i=0; i<n; i++) {
        int a = scanner.nextInt();
        int b = scanner.nextInt(); 
          res += a * b;
}
        if(res == x) {
            System.out.println("Yes");
        }  else System.out.println("No");
    }
}