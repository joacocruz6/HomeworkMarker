import java.util.*;
class Fib{
     public static int fibs(int n){
          if(n == 0 || n == 1) return 1;
          else return fibs(n-1)+fibs(n-2);
     }
     public static void main(String[] args){
          Scanner sc = new Scanner(System.in);
          int n = sc.nextInt();
          int r = fibs(n);
          System.out.println(r);
     }
}