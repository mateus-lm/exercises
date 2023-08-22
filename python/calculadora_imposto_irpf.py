from pty import slave_open


def main():
    faixa_1 = 1903.98
    faixa_2 = 922.67
    faixa_3 = 924.40
    faixa_4 = 913.63
    #faixa_5 = excente
    imposto_faixa_1 = 0
    imposto_faixa_2 = 0.075
    imposto_faixa_3 = 0.15
    imposto_faixa_4 = 0.225
    imposto_faixa_5 = 0.275

    salario = float(input("Digite o salário: "))
    
    imposto_1 = 0
    imposto_2 = 0
    imposto_3 = 0
    imposto_4 = 0
    imposto_5 = 0

    if salario <= 1903.98:
        imposto_1 = salario * imposto_faixa_1
    elif salario > 1903.98 and salario <= 2826.65:
        imposto_2 = (salario - faixa_1) * imposto_faixa_2
    elif salario > 2826.65 and salario <= 3751.05:
        imposto_2 = faixa_2 * imposto_faixa_2
        imposto_3 = (salario - faixa_1 - faixa_2) * imposto_faixa_3
    elif salario > 3751.05 and salario <= 4664.68:
        imposto_2 = faixa_2 * imposto_faixa_2
        imposto_3 = faixa_3 * imposto_faixa_3
        imposto_4 = (salario - faixa_1 - faixa_2 - faixa_3) * imposto_faixa_4
    elif salario > 4664.68:
        imposto_2 = faixa_2 * imposto_faixa_2
        imposto_3 = faixa_3 * imposto_faixa_3
        imposto_4 = faixa_4 * imposto_faixa_4
        imposto_5 = (salario - faixa_1 - faixa_2 - faixa_3 - faixa_4) * imposto_faixa_5
    
    imposto_total = imposto_1 + imposto_2 + imposto_3 + imposto_4 + imposto_5

    print(imposto_total, salario)

if __name__ == '__main__':
    main()
    