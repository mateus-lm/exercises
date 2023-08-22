def main():
    while True:
        peso_peixe = float(input("Quantidade de peixe em kg: "))
        if peso_peixe > 50:
            excedente = (peso_peixe - 50)
            multa_excedente =  excedente * 4
            print(f"Você excedeu {excedente} kg e a multa aplicada foi de {multa_excedente} R$")
        else:
            print('Valor dentro dos parâmtros aceitáveis')

if __name__ == '__main__':
    main()