def unbanda():
    n = int(input("Entradas: "))
    x = 0
    for i in range(n):
        soma = str(input())
        if '+' in soma:
            x += 1
        elif '-' or '@' or '!' in soma:
            x -= 1
    print (x)

def main():
    unbanda()

if __name__ == '__main__':
    main()