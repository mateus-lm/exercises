def fibonacci(n):
    if (n == 0): 
        return 0
    if (n == 1):
        return 1
    num_fib = fibonacci(n-1) + fibonacci(n-2)
    return num_fib