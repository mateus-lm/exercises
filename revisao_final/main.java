package revisao_final;
import java.util.Scanner;

public class main {
    public static void main(String[] args){
        Scanner ler = new Scanner(System.in);
        // Q1
        // q2 formaGeometrica = new q2();
        // int arg1 = ler.nextInt();
        // int arg2 = ler.nextInt();
        // ler.nextLine();
        // String forma = ler.nextLine();
        // String result = formaGeometrica.area(arg1, arg2, forma);
        // System.out.println(result);
        //banner
        // Banner banner = new Banner();
        // int n = ler.nextInt();
        // System.out.println(banner.banner(n));
        fibonacci fibonacci = new fibonacci();
        int n = ler.nextInt();
        System.out.println(fibonacci.fib(n));
        
    }
}
