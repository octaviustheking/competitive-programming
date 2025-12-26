package a_beautiful_average;
import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int times = input.nextInt();

        for (int i = 0; i < times; i++) {
            int numbers = input.nextInt();
            int[] array = new int[numbers];
            for (int j = 0; j < numbers; j++) {
                array[j] = input.nextInt();
            }
            Arrays.sort(array);
            System.out.println(array[array.length - 1]);
        }
    }
}
