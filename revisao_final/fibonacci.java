package revisao_final;

public class fibonacci {
    public int fib(int n){
        if (n == 0) return 0;
        if (n == 1) return 1;
        int sequencia = fib(n-1) + fib(n-2);
        return sequencia;
    }
}
