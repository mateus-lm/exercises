def main():
    n = int(input())
    m = int(input())
    listas_numeros = []
    for i in range(n):
        inteiros = list(map(int, input().strip().split()))[:m]
        print(inteiros, "DENTRO")
        listas_numeros.append(inteiros)
    print(inteiros, "FORA")
    print(listas_numeros, "LISTA COMPLETA")

if __name__ == '__main__':
    main()