int fibonacci(n){
    if (n == 0) return 0;
    if (n == 1) return 1;
    int num_fib = fibonacci(n-1) + fibonacci(n-2);
    return num_fib;
}
int main(void){
    int n;
    scanf("%d", &n);
    printf("%d", fibonacci(n));
    return 0;
}