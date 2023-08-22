def main():
    numeros = []
    for i in range(10):
        num = int(input("Digite o valor: "))
        numeros.append(num)
    numeros.sort()

    print(numeros[0], numeros[-1])

if __name__ == '__main__':
    main()
    