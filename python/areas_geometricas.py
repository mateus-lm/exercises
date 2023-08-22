from math import pi
def circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = pi * (raio ** 2)
    print(f"A área do cículo é {area:.2f}cm ")

def quadrado_dobrado():
    quadrado = float(input("Digite o lado do quadrado: "))
    quadrado_dobrado = (quadrado ** 2) * 2
    print(f"A área do quadrado é {quadrado_dobrado:.2f}cm ")

def main():
    if int(input("1 para calcular a área do círculo, 2 para calcular a área dobrada do quadrado")) == 1:
        circulo()
    else:
        quadrado_dobrado()

if __name__ == '__main__':
    main()