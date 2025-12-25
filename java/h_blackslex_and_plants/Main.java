import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int times = input.nextInt();
        for (int i = 0; i < times; i++) {
            int[] plants = new int[input.nextInt()];
            int water_ops = input.nextInt();
            for (int j = 0; j < water_ops; j++) {
                int l = input.nextInt();
                int r = input.nextInt();
                for (int k = l; k <= r; k++) {
                    int func_number = k - l + 1;
                    plants[k - 1] += (func_number & -func_number) * func_number;
                }
            }
            for (int num : plants) {
                System.out.print(num + " ");
            }
            System.out.print("\n");
        }
    }
}
