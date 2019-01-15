package swexport.d3;

import java.util.Arrays;
import java.util.Scanner;

public class DigutSum {

    public static String solution(String x){
        while (true) {
            if (x.length() == 1) return x + "";
            int sumResult = Arrays.stream(x.split("")).mapToInt(Integer::parseInt).sum();
            x = sumResult + "";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++){
            String x = sc.nextLine();
            System.out.printf("%s %s\n", "#" + (i + 1), solution(x));
        }
    }
}
