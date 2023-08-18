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

    salario = float(input("Digite o salário"))
    
    if salario <= 1903.98:
        imposto = salario * imposto_faixa_1
    elif salario > 1903.98 and salario <= 2826.65:
        imposto = (salario - faixa_1) * imposto_faixa_2
    elif salario > 2826.65 and salario <= 3751.05:
        imposto = (salario - faixa_1 + faixa_2) * imposto_faixa_3
    elif salario > 3751.05 and salario <= 4664.68:
        imposto = (salario - faixa_1 + faixa_2 + faixa_3) * imposto_faixa_4
    elif salario > 4664.68:



if __name__ == '__main__':
    main()
    