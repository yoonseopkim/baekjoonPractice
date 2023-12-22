import java.util.Scanner;
public class Main {
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);
        int hour = scanner.nextInt();
        int minute = scanner.nextInt();
        int hour1  = 0;
        int minute1 =0;
        if (minute >= 45) {
            minute1 = minute-45;
            System.out.print(hour + " " + minute1);
        }
        else if (hour >0 && minute <45 ) {
            minute1 = 60-(45-minute);
            hour1 = hour-1;
            System.out.print(hour1 + " " + minute1);
        }
        else {
            minute1 = 60-(45-minute);
            System.out.print(23 + " " + minute1);
        }
    }
}